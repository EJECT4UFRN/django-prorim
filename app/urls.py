from django.conf.urls import url, include
from app.views import (
    ChoiceDisponibilidadeMaquinaView,
    ChoiceExameColetaView,
    ChoicePeriodoTurnoView,
    ChoiceStatusPacienteView,
    ChoiceTesteAguaView,
    ControleAguaView,
    FileControleAguaView,
    ControleColetaView,
    ControleDesinfeccaoView,
    ControleFinanceiroView,
    EnfermeiroView,
    ErroView,
    EstadiaView,
    ManutencaoCorretivaView,
    ManutencaoPreventivaView,
    MaquinaView,
    PacienteView,
    SalaView,
    SecaoView,
    TecnicoView,
)
from rest_framework.routers import DefaultRouter

ROUTER = DefaultRouter()
ROUTER.register(r'choice-disponibilidade-maquina', ChoiceDisponibilidadeMaquinaView)
ROUTER.register(r'choice-exame-coleta', ChoiceExameColetaView)
ROUTER.register(r'choice-periodo-turno', ChoicePeriodoTurnoView)
ROUTER.register(r'choice-status-paciente', ChoiceStatusPacienteView)
ROUTER.register(r'choice-teste-agua', ChoiceTesteAguaView)
ROUTER.register(r'controle-agua', ControleAguaView)
ROUTER.register(r'controle-agua/file', FileControleAguaView)
ROUTER.register(r'controle-coleta', ControleColetaView)
ROUTER.register(r'controle-desinfeccao', ControleDesinfeccaoView)
ROUTER.register(r'controle-financeiro', ControleFinanceiroView)
ROUTER.register(r'enfermeiro', EnfermeiroView)
ROUTER.register(r'erro', ErroView)
ROUTER.register(r'estadia', EstadiaView)
ROUTER.register(r'manutencao-corretiva', ManutencaoCorretivaView)
ROUTER.register(r'manutencao-preventiva', ManutencaoPreventivaView)
ROUTER.register(r'maquina', MaquinaView)
ROUTER.register(r'paciente', PacienteView)
ROUTER.register(r'sala', SalaView)
ROUTER.register(r'secao', SecaoView)
ROUTER.register(r'tecnico', TecnicoView)

urlpatterns = [
    url(r'^api/', include(ROUTER.urls))
]
