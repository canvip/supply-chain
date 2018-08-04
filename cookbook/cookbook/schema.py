import graphene

import ingredients.schema, shortener.schema,links.schema

class Query(ingredients.schema.Query,links.schema.Query,
            shortener.schema.Query,
            graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

class Mutation(
                shortener.schema.Mutation,
                links.schema.Mutation,
                graphene.ObjectType,
                ):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)