import graphene
from graphene_django.types import DjangoObjectType
from .models import Shortener

class ShortenerType(DjangoObjectType):
    class Meta:
        model = Shortener


class Query(graphene.ObjectType):
    Shorteners = graphene.List(ShortenerType)

    def resolve_Shorteners(self, info, **kwargs):
        return Shortener.objects.all()

##########################################
class CreateShortener(graphene.Mutation):
    id          =  graphene.Int()
    url         =  graphene.String()
    #shortcode   =  graphene.String()
    #updated     =  graphene.String()
    #timestamp   =  graphene.String()

    #2
    class Arguments:
        url          = graphene.String()
        #shortcode    = graphene.String()
        #description = graphene.String()

    #3
    def mutate(self, info, url,): #, shortcode):
        shortener = Shortener(url=url,)#, shortcode=shortcode)
        shortener.save()

        return CreateShortener(
            url         =shortener.url,
            id          =shortener.id,
            #shortcode   =shortener.shortcode,
            #updated     =shortener.updated  ,
            #timestamp   =shortener.timestamp,
        )


#4
class Mutation(graphene.ObjectType):
    create_Shortener = CreateShortener.Field()