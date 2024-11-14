from rest_framework import serializers
from .models import Osoba, Stanowisko

class OsobaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(max_length=50)
    nazwisko = serializers.CharField(max_length=50)
    plec = serializers.ChoiceField(choices=[(1, 'Kobieta'), (2, 'Mężczyzna'), (3, 'Inne')])
    stanowisko = serializers.PrimaryKeyRelatedField(queryset=Stanowisko.objects.all())
    data_dodania = serializers.DateField(read_only=True)

    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.plec = validated_data.get('plec', instance.plec)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.save()
        return instance

class StanowiskoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = '__all__'