import graphene
from core import ExtendedConnection, prefix_filterset
from core.schema import OrderedDjangoFilterConnectionField, DjangoObjectType
from program.models import Program
import graphene_django_optimizer as gql_optimizer
from insuree import models as insuree_models
from policy import models as policy_models

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
        insureeId=graphene.Int(),
        visitDateFrom=graphene.Date(),
    )

    def resolve_program(self, info, **kwargs):
        query = Program.objects
        insuree_id = kwargs.get("insureeId", None)
        visit_date_from = kwargs.get("visitDateFrom", None)
        if insuree_id and visit_date_from:
            hfid = info.context.user.health_facility_id
            program_facilies_ids = []
            program_facilies = Program.objects.filter(
                healthfacility=hfid)
            for program_facility in program_facilies:
                program_facilies_ids.append(program_facility.idProgram)

            insuree = insuree_models.Insuree.objects.get(id=insuree_id)
            family_id = insuree.family_id
            policies = policy_models.Policy.objects.filter(
                family_id=family_id).filter(expiry_date__gte=visit_date_from).filter(
                    start_date__lte=visit_date_from).filter(status=2)
            products_for_program = []
            for policy in policies:
                if policy.product:
                    if policy.product.program_id:
                        products_for_program.append(policy.product.program_id)
            intersect = list(set(products_for_program) & set(program_facilies_ids))
            query=query.filter(idProgram__in=intersect)
        return gql_optimizer.query(query.all(), info)
