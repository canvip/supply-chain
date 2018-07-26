import graphene

from graphene_django.types import DjangoObjectType

from shortener.models import Shortener



class ShortenerType(DjangoObjectType):
    class Meta:
        model = Shortener


class Query(object):
    all_Shortener = graphene.List(ShortenerType)
    def resolve_all_Shortener(self, info, **kwargs):
        return all_Shortener.objects.all()
