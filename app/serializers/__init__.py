# -*- coding: utf-8 -*-
from app.serializers.choice_disponibilidade_maquina import (
    ChoiceDisponibilidadeMaquinaSerializer,
)
from app.serializers.choice_exame_coleta import (
    ChoiceExameColetaSerializer,
)
from app.serializers.choice_periodo_turno import (
    ChoicePeriodoTurnoSerializer,
)
from app.serializers.choice_status_estadia import (
    ChoiceStatusEstadiaSerializer,
)
from app.serializers.choice_status_manutencao_corretiva import (
    ChoiceStatusManutencaoCorretivaSerializer,
)
from app.serializers.choice_status_paciente import (
    ChoiceStatusPacienteSerializer,
)
from app.serializers.choice_teste_agua import (
    ChoiceTesteAguaSerializer,
)
from app.serializers.controle_agua import (
    ControleAguaSerializer,
    ShallowControleAguaSerializer,
    FileControleAguaSerializer,
)
from app.serializers.controle_coleta import (
    ControleColetaSerializer,
    ShallowControleColetaSerializer,
)
from app.serializers.controle_desinfeccao import (
    ControleDesinfeccaoSerializer,
)
from app.serializers.controle_financeiro import (
    ControleFinanceiroSerializer,
)
from app.serializers.erro import (
    ErroSerializer,
    NoRelationErroSerializer,
    ShallowErroSerializer,
)
from app.serializers.estadia import (
    EstadiaSerializer,
    ShallowEstadiaSerializer,
)
from app.serializers.manutencao_corretiva import (
    ManutencaoCorretivaSerializer,
    ShallowManutencaoCorretivaSerializer,
    NoRelationManutencaoCorretivaSerializer,
)
from app.serializers.manutencao_preventiva import (
    ManutencaoPreventivaSerializer,
    ShallowManutencaoPreventivaSerializer,
)
from app.serializers.maquina import (
    MaquinaSerializer,
    ShallowMaquinaSerializer,
)
from app.serializers.paciente import (
    PacienteSerializer,
    ShallowPacienteSerializer,
)
from app.serializers.sala import SalaSerializer
from app.serializers.secao import (
    SecaoSerializer,
    ShallowSecaoSerializer,
)
from app.serializers.user import UserSerializer
