from django.conf.urls import url, include
from django.conf import settings
from app.views import (
    IndexView,
    ChoiceDisponibilidadeMaquinaView,
    ChoiceExameColetaView,
    ChoicePeriodoTurnoView,
    ChoiceTesteAguaView,
    ControleAguaView,
    ControleColetaView,
    ControleDesinfeccaoView,
    # ControleFinanceiroView,
    EnfermeiroView,
    ErroView,
    EstadiaView,
    ManutencaoCorretivaView,
    ManutencaoPreventivaView,
    MaquinaView,
    SalaView,
    TecnicoView,
    TurnoView,
)
from rest_framework.routers import DefaultRouter

ROUTER = DefaultRouter()
ROUTER.register(r'choice-disponibilidade-maquina', ChoiceDisponibilidadeMaquinaView)
ROUTER.register(r'choice-exame-coleta', ChoiceExameColetaView)
ROUTER.register(r'choice-periodo-turno', ChoicePeriodoTurnoView)
ROUTER.register(r'choice-teste-agua', ChoiceTesteAguaView)
ROUTER.register(r'controle-agua', ControleAguaView)
ROUTER.register(r'controle-coleta', ControleColetaView)
ROUTER.register(r'controle-desinfeccao', ControleDesinfeccaoView)
# ROUTER.register(r'controle-financeiro', ControleFinanceiroView)
ROUTER.register(r'enfermeiro', EnfermeiroView)
ROUTER.register(r'erro', ErroView)
ROUTER.register(r'estadia', EstadiaView)
ROUTER.register(r'manutencao-corretiva', ManutencaoCorretivaView)
ROUTER.register(r'manutencao-preventiva', ManutencaoPreventivaView)
ROUTER.register(r'maquina', MaquinaView)
ROUTER.register(r'sala', SalaView)
ROUTER.register(r'tecnico', TecnicoView)
ROUTER.register(r'turno', TurnoView)


urlpatterns = [
    url(r'^api/', include(ROUTER.urls)),
    url(
        r'^',
        IndexView.as_view(),
        name='index'
    ),
]
