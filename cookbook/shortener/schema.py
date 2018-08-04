import graphene

from graphene_django.types import DjangoObjectType

from shortener.models import Shortener



class ShortenerType(DjangoObjectType):
    class Meta:
        model = Shortener


class Query(object):
    all_Shortener = graphene.List(ShortenerType)

    #category = graphene.Field(CategoryType,
    #                          id=graphene.Int(),
    #                          name=graphene.String())
    #all_categories = graphene.List(CategoryType)
    def resolve_all_Shortener(self, info, **kwargs):
        return Shortener.objects.all()


class CreateShortener(graphene.Mutation):
    id          =  graphene.Int()
    url         =  graphene.String()
    shortcode   =  graphene.String()
    updated     =  graphene.String()
    timestamp   =  graphene.String()

    #2
    class Arguments:
        url          = graphene.String()
        shortcode    = graphene.Int()
        #description = graphene.String()

    #3
    def mutate(self, info, url, shortcode):
        link = Link(url=url, shortcode=shortcode)
        link.save()

        return CreateShortener(
            url=link.url,
            shortcode=link.shortcode,
            
        )


#4
class Mutation(graphene.ObjectType):
    create_Shortener = CreateShortener.Field()