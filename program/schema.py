import graphene
from core import ExtendedConnection, prefix_filterset
from core.schema import OrderedDjangoFilterConnectionField, DjangoObjectType
from program.models import Program

class ProgramGQLType(DjangoObjectType):
    class Meta:
        model = Program
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            "nameProgram": ["exact", "icontains"]
        }
        connection_class = ExtendedConnection


class Query(graphene.ObjectType):
    program = OrderedDjangoFilterConnectionField(
        ProgramGQLType,
        diagnosisVariance=graphene.Int(),
        code_is_not=graphene.String(),
        orderBy=graphene.List(of_type=graphene.String),
        items=graphene.List(of_type=graphene.String),
        services=graphene.List(of_type=graphene.String),
    )