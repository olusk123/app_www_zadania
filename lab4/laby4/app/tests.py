from django.test import TestCase
from .models import Osoba, Stanowisko

class OsobaModelTest(TestCase):
    def test_osoba_str(self):
        stanowisko = Stanowisko.objects.create(nazwa="Programista")
        osoba = Osoba.objects.create(imie="Jan", nazwisko="Kowalski", plec=2, stanowisko=stanowisko)
        self.assertEqual(str(osoba), "Jan Kowalski")  # Sprawdzenie metody __str__()

    def test_create_osoba(self):
        stanowisko = Stanowisko.objects.create(nazwa="Programista")
        osoba = Osoba.objects.create(imie="Jan", nazwisko="Kowalski", plec=2, stanowisko=stanowisko)
        self.assertEqual(Osoba.objects.count(), 1)
        self.assertEqual(osoba.imie, "Jan")
        self.assertEqual(osoba.nazwisko, "Kowalski")
