from django.contrib import admin
from .models import Osoba, Stanowisko


class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ('nazwa','opis')
    search_fields = ('nazwa',)

class OsobaAdmin(admin.ModelAdmin):
    list_display = ('imie','nazwisko','plec','stanowisko_display','data_dodania',)
    list_filter =['stanowisko','data_dodania',]
    search_fields = ('imie','nazwisko',)

    @admin.display(description='stanowisko')
    def stanowisko_display(self,obj):
        return f"{obj.stanowisko.nazwa}({obj.stanowisko.id})" if obj.stanowisko else "brak"

admin.site.register(Stanowisko, StanowiskoAdmin)
admin.site.register(Osoba,OsobaAdmin)
