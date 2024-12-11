from .models import Osoba, Stanowisko
import graphene
from graphene_django import DjangoObjectType

# GraphQL Types
class OsobaType(DjangoObjectType):
    class Meta:
        model = Osoba
        fields = ("id", "imie", "nazwisko", "plec", "stanowisko", "data_dodania")

class StanowiskoType(DjangoObjectType):
    class Meta:
        model = Stanowisko
        fields = ("id", "nazwa", "opis")

# GraphQL Query
class Query(graphene.ObjectType):
    all_stanowiska = graphene.List(StanowiskoType)
    stanowisko_by_id = graphene.Field(StanowiskoType, id=graphene.Int(required=True))
    all_osoby = graphene.List(OsobaType)
    osoba_by_id = graphene.Field(OsobaType, id=graphene.Int(required=True))
    osoby_by_nazwisko = graphene.List(OsobaType, nazwisko=graphene.String(required=True))
    osoby_by_fragment_nazwiska = graphene.List(OsobaType, fragment=graphene.String(required=True))
    count_osoby_by_shirt_size = graphene.Int(shirt_size=graphene.String(required=True))
    count_osoby_by_team = graphene.Int(team_id=graphene.Int(required=True))

    def resolve_all_stanowiska(root, info):
        return Stanowisko.objects.all()

    def resolve_stanowisko_by_id(root, info, id):
        return Stanowisko.objects.get(pk=id)

    def resolve_all_osoby(root, info):
        return Osoba.objects.select_related("stanowisko").all()

    def resolve_osoba_by_id(root, info, id):
        return Osoba.objects.get(pk=id)

    def resolve_osoby_by_nazwisko(root, info, nazwisko):
        return Osoba.objects.filter(nazwisko__icontains=nazwisko)

    def resolve_osoby_by_fragment_nazwiska(root, info, fragment):
        return Osoba.objects.filter(nazwisko__icontains=fragment)

    def resolve_count_osoby_by_shirt_size(root, info, shirt_size):
        return Osoba.objects.filter(shirt_size=shirt_size).count()

    def resolve_count_osoby_by_team(root, info, team_id):
        return Osoba.objects.filter(stanowisko_id=team_id).count()

schema = graphene.Schema(query=Query)