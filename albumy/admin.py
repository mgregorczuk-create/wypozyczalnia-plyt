from django.contrib import admin
from .models import Gatunek, Artysta, Album, Wypozyczenie, Ocena

admin.site.register(Gatunek)
admin.site.register(Artysta)
admin.site.register(Album)
admin.site.register(Wypozyczenie)
admin.site.register(Ocena)