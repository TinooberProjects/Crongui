"""
Este módulo visa facilitará a  criação de tarefas agendadas


COMO UTILIZAR O MÓDULO:
========


FONTES DE PESQUISA
=

https://docs.python.org/3/library/subprocess.html

https://e-tinet.com/linux/crontab/#

https://linux.die.net/man/5/crontab

https://pt.stackoverflow.com/questions/2818/como-agendar-uma-tarefa-recorrente-no-linux

https://www.horadecodar.com.br/2020/04/28/executar-comando-do-linux-com-python/

https://www.youtube.com/watch?v=EgrpfvBc7ks

https://www.youtube.com/watch?v=TG--rQkZvGc

"""
#biblioteca de interface gráfica
import subprocess
import tkinter as tk

from pathlib import Path


#Declarando a classe crongui
class crongui:
    """ Classe de tarefas
    """
    #construtor
    def __init__(self):
        self.minutos="0"
        self.hora="0"
        self.dia="1"
        self.mes="1"
        self.dia_semana="0"
        self.comando="criado"

   


        
            
