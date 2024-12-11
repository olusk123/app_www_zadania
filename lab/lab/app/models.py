from django.db import models
from django.utils.timezone import now
from django.core.exceptions import ValidationError
import re



def get_current_date():
    return now().date()


# Deklaracja statycznej listy wyboru do wykorzystania w klasie modelu
MONTHS = models.IntegerChoices('Miesiace',
                               'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
)


class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Coach(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)


class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=100, null=False, blank=False)
    opis = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nazwa


from django.contrib.auth.models import User

def get_default_user():
    return User.objects.first()



class Osoba(models.Model):
    class Plec(models.IntegerChoices):
        KOBIETA = 1, 'Kobieta'
        MEZCZYZNA = 2, 'Mężczyzna'
        INNE = 3, 'Inne'

    imie = models.CharField(max_length=50, null=False, blank=False)
    nazwisko = models.CharField(max_length=50, null=False, blank=False)
    plec = models.IntegerField(choices=Plec.choices, null=False, blank=False)
    stanowisko = models.ForeignKey('Stanowisko', on_delete=models.CASCADE)
    data_dodania = models.DateField(default=get_current_date)  # Użycie funkcji zamiast lambda
    wlasciciel = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name='osoby', null=True
    )

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

    class Meta:
        ordering = ['-nazwisko']
        permissions = [
            ("can_view_other_persons", "Can view other persons"),
        ]

    # Metoda walidacji
    def clean(self):
        # Walidacja pola 'imie' i 'nazwisko' - może zawierać tylko litery
        if not re.match(r'^[a-zA-ZĄĆĘŁŃÓŚŹŻąćęłńóśźż]+$', self.imie):
            raise ValidationError({'imie': 'Imię może zawierać tylko litery.'})

        if not re.match(r'^[a-zA-ZĄĆĘŁŃÓŚŹŻąćęłńóśźż]+$', self.nazwisko):
            raise ValidationError({'nazwisko': 'Nazwisko może zawierać tylko litery.'})

        # Walidacja pola 'data_dodania' - nie może być z przyszłości
        today = now().date()
        if self.data_dodania > today:
            raise ValidationError({'data_dodania': 'Data dodania nie może być z przyszłości.'})

    def save(self, *args, **kwargs):
        self.full_clean()  # Wywołanie metody clean przed zapisaniem
        super().save(*args, **kwargs)