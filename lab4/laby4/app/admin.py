from django.contrib import admin
from .models import Person, Team, Coach, Osoba, Stanowisko

# Register your models here.

class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ('data_dodania',)
    list_display = ['imie', 'nazwisko', 'plec', 'stanowisko_display', 'data_dodania']
    list_filter = ['stanowisko', 'data_dodania']

    @admin.display(description='Stanowisko')
    def stanowisko_display(self, obj):
        return f"{obj.stanowisko.nazwa} ({obj.stanowisko.id})"

class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'opis']
    list_filter = ['nazwa']

admin.site.register(Person)
admin.site.register(Team)
admin.site.register(Coach)
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko, StanowiskoAdmin)