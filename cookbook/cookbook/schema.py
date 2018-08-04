import graphene

import ingredients.schema, shortener.schema


class Query(ingredients.schema.Query,
            graphene.ObjectType,
            shortener.schema.Query):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass



class Mutation(shortener.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query,mutation=Mutation)
