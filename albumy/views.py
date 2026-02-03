from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm 
from .models import Album, Wypozyczenie
import datetime

# Widok 1: Lista
def lista_albumow(request):
    wszystkie_albumy = Album.objects.all()
    return render(request, 'albumy/lista_albumow.html', {'albumy': wszystkie_albumy})

# Widok 2: Szczegóły 
def szczegoly_albumu(request, id):
    
    album = get_object_or_404(Album, pk=id)
    
    return render(request, 'albumy/szczegoly_albumu.html', {'album': album})


@login_required  
def wypozycz_album(request, id):
    album = get_object_or_404(Album, pk=id)

    if request.method == "POST":
        if album.dostepny:
            # 1. Tworzymy wpis o wypożyczeniu
            Wypozyczenie.objects.create(
                uzytkownik=request.user,
                album=album,
                
            )
            # 2. Zmieniamy status płyty
            album.dostepny = False
            album.save()
            
            # 3. Wracamy na listę
            return redirect('lista_albumow')
    
    return redirect('szczegoly_albumu', id=id)



@login_required
def moje_wypozyczenia(request):
    wypozyczenia = Wypozyczenie.objects.filter(uzytkownik=request.user, data_zwrotu__isnull=True)
    return render(request, 'albumy/moje_wypozyczenia.html', {'wypozyczenia': wypozyczenia})

@login_required
def zwroc_album(request, id):
    wypozyczenie = get_object_or_404(Wypozyczenie, pk=id, uzytkownik=request.user)
    
    if request.method == "POST":
        # 1. Ustawiamy datę zwrotu 
        wypozyczenie.data_zwrotu = datetime.datetime.now()
        wypozyczenie.save()
        
        # 2. Płyta znowu jest dostępna
        album = wypozyczenie.album
        album.dostepny = True
        album.save()
        
        return redirect('moje_wypozyczenia')

    return redirect('moje_wypozyczenia')

def rejestracja(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') # Po sukcesie idź do logowania
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})