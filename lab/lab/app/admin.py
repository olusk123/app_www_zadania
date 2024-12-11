from django.contrib import admin
from .models import Person, Team, Coach, Osoba, Stanowisko

class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ('data_dodania',)
    list_display = ['imie', 'nazwisko', 'plec', 'stanowisko_display', 'wlasciciel', 'data_dodania']
    list_filter = ['stanowisko', 'data_dodania', 'wlasciciel']
    search_fields = ['imie', 'nazwisko', 'stanowisko__nazwa', 'wlasciciel__username']
    actions = ['reset_stanowisko']

    @admin.display(description='Stanowisko')
    def stanowisko_display(self, obj):
        return f"{obj.stanowisko.nazwa} ({obj.stanowisko.id})"

    @admin.action(description='Usuń stanowisko z wybranych osób')
    def reset_stanowisko(self, request, queryset):
        queryset.update(stanowisko=None)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.wlasciciel = request.user
        super().save_model(request, obj, form, change)

class StanowiskoAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'opis', 'liczba_osob']
    list_filter = ['nazwa']

    @admin.display(description='Liczba osób')
    def liczba_osob(self, obj):
        return obj.osoba_set.count()

admin.site.register(Person)
admin.site.register(Team)
admin.site.register(Coach)
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko, StanowiskoAdmin)