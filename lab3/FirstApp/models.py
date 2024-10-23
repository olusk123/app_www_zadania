from django.db import models

class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=100,blank=True,null=True)
    opis = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nazwa

class Osoba(models.Model):

    class plec(models.IntegerChoices):
        KOBIETA = 1,"KOBIETA"
        MEZCZYZNA = 2, "MEZCZYZNA"

    imie = models.CharField(max_length=60,blank=False,null=False)
    nazwisko = models.CharField(max_length=60,blank=False,null=False)
    plec = models.IntegerField(choices=plec.choices)
    stanowisko = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)
    data_dodania = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['nazwisko']

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"