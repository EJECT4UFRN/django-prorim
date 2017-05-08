from app.serializers import (
    ManutencaoCorretivaSerializer,
    ErroSerializer,
    EstadiaSerializer,
    TurnoSerializer,
)
from app.models import (
    ManutencaoCorretiva,
    Erro,
    Estadia,
    Turno,
)
from djangorestframework_camel_case.render import CamelCaseJSONRenderer

xs = Estadia.objects.all()
x = xs[0]
serie = EstadiaSerializer(instance=x)
# print(CamelCaseJSONRenderer().render(serie.data))
print(serie.data)
