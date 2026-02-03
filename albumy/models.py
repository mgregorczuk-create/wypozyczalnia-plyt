from django.db import models
from django.contrib.auth.models import User

# Model 1: Gatunek 
class Gatunek(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa

# Model 2: Artysta 
class Artysta(models.Model):
    pseudonim = models.CharField(max_length=100)
    opis = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.pseudonim

# Model 3: Album 
class Album(models.Model):
    tytul = models.CharField(max_length=200)
    artysta = models.ForeignKey(Artysta, on_delete=models.CASCADE)
    gatunek = models.ForeignKey(Gatunek, on_delete=models.SET_NULL, null=True)
    rok_wydania = models.IntegerField()
    okladka_url = models.URLField(blank=True, null=True) # Link do obrazka w necie
    dostepny = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tytul} - {self.artysta}"

# Model 4: Wypożyczenie
class Wypozyczenie(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    data_wypozyczenia = models.DateTimeField(auto_now_add=True)
    data_zwrotu = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.uzytkownik} -> {self.album}"

# Model 5: Ocena
class Ocena(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    gwiazdki = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    komentarz = models.TextField(blank=True)