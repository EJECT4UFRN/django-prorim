# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from dateutil.parser import parse
from datetime import datetime, timedelta
from app.models import *
from django.contrib.auth.models import User


class ReportView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, format=None):
        # filtro = self.request.query_params
        filtro = request.query_params
        inicial = None
        final = None
        if filtro:
            if 'inicial' in filtro:
                inicial = parse(filtro['inicial'])
                inicial = inicial.replace(hour=0)
                inicial = inicial.replace(minute=0)
                inicial = inicial.replace(second=0)
            if 'final' in filtro:
                final = parse(filtro['final'])
                final = final.replace(hour=23)
                final = final.replace(minute=59)
                final = final.replace(second=59)
        if not (final and inicial):
            return Response(
                {'erro': 'Data inicial e final não foram informadas.'}
            )
        # valores para testes
        # inicial = parse('2017-08-14T00:00:00')
        # final = parse('2017-08-14T00:00:00')
        # queries para ControleAgua
        controle_coleta = ControleAgua.objects.filter(criado__range=(inicial, final))
        # queries para ControleColeta
        controle_agua_created =  ControleColeta.objects.filter(criado__range=(inicial, final))
        exames = ChoiceExameColeta.objects.all()
        controle_agua_created_exames = []
        for exame in exames:
            count = controle_agua_created.filter(exame=exame).count()
            if count > 0:
                controle_agua_created_exames.append({
                    'nome': exame.nome,
                    'count': count,
                })
        controle_agua_realizados =  ControleColeta.objects.filter(data_realizado__range=(inicial, final))
        controle_agua_enviados =  ControleColeta.objects.filter(data_envio__range=(inicial, final))
        controle_agua_resultados =  ControleColeta.objects.filter(data_resultado__range=(inicial, final))
        resultados = ChoiceTesteAgua.objects.all()
        controle_agua_resultados_status = []
        for resultado in resultados:
            count = controle_agua_resultados.filter(resultado=resultado).count()
            if count > 0:
                controle_agua_resultados_status.append({
                    'nome': resultado.nome,
                    'count': count,
                })
        # queries para ControleDesinfeccao
        controle_desinfeccao = ControleDesinfeccao.objects.filter(criado__range=(inicial, final))
        # queries para paciente
        pacientes = Paciente.objects.filter(criado__range=(inicial, final))
        # queries para Estadia
        estadias = Estadia.objects.filter(secao__data__range=(inicial, final))
        periodos = ChoicePeriodoTurno.objects.all()
        estadias_periodos = []
        for periodo in periodos:
            count = estadias.filter(secao__periodo=periodo).count()
            if count > 0:
                estadias_periodos.append({
                    'nome': periodo.nome,
                    'count': count,
                })
        salas = Sala.objects.all()
        estadias_salas = []
        for sala in salas:
            count = estadias.filter(secao__sala=sala).count()
            if count > 0:
                estadias_salas.append({
                    'nome': sala.identificador,
                    'count': count,
                })
        choices_status_estadia = ChoiceStatusEstadia.objects.all()
        estadias_status = []
        for choice in choices_status_estadia:
            count = estadias.filter(status=choice).count()
            if count > 0:
                estadias_status.append({
                    'nome': choice.nome,
                    'count': count,
                })
        # Queries para Erro
        erros = Erro.objects.filter(estadia__secao__data__range=(inicial, final))
        maquinas = Maquina.objects.all()
        erros_maquinas = []
        for maquina in maquinas:
            count = erros.filter(maquina=maquina).count()
            if count > 0:
                erros_maquinas.append({
                    'nome': maquina.numero,
                    'count': count,
                })
        # queries para ManutencaoCorretiva
        manutencao_corretiva = ManutencaoCorretiva.objects.filter(data__range=(inicial, final))
        tecnicos = User.objects.filter(groups__name__in=['Técnico'])
        manutencao_corretiva_tecnicos = []
        for tecnico in tecnicos:
            count = manutencao_corretiva.filter(tecnico=tecnico).count()
            if count > 0:
                manutencao_corretiva_tecnicos.append({
                    'count': count,
                    'nome': tecnico.first_name,
                })
        report = {
            'controle_coleta': {
                'created': {
                    'total': controle_coleta.count(),
                    'satisfatorios': controle_coleta.filter(resultado=True).count(),
                },
            },
            'controle_agua': {
                'created': {
                    'total': controle_agua_created.count(),
                    'exames': controle_agua_created_exames,
                },
                'realizados': controle_agua_realizados.count(),
                'enviados': controle_agua_enviados.count(),
                'resultados': {
                    'total': controle_agua_resultados.count(),
                    'status': controle_agua_resultados_status,
                },
            },
            'controle_desinfeccao': {
                'created': {
                    'total': controle_desinfeccao.count(),
                    'realizados': controle_desinfeccao.filter(realizado=True).count(),
                },
            },
            'pacientes': {
                'created': pacientes.count(),
            },
            'estadias': {
                'total': estadias.count(),
                'periodos': estadias_periodos,
                'salas': estadias_salas,
                'status': estadias_status
            },
            'erros': {
                'total': erros.count(),
                'maquinas': erros_maquinas,
                'manutencao_corretiva': erros.exclude(manutencao_corretiva__acao=None).count()
            },
            'manutencao_corretiva': {
                'total': manutencao_corretiva.count(),
                'tecnicos': manutencao_corretiva_tecnicos,
            },
        }
        return Response(report)
