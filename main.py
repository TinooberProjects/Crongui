"""

FONTES DE PESQUISA


https://docs.python.org/3/library/subprocess.html

https://e-tinet.com/linux/crontab/#

https://linux.die.net/man/5/crontab

https://pt.stackoverflow.com/questions/2818/como-agendar-uma-tarefa-recorrente-no-linux

https://www.horadecodar.com.br/2020/04/28/executar-comando-do-linux-com-python/

https://www.youtube.com/watch?v=EgrpfvBc7ks

https://www.youtube.com/watch?v=TG--rQkZvGc

"""





#zona de importacao

import subprocess

import tkinter as tk
from tkinter.constants import DISABLED, END
from typing import Text

import tkinter.filedialog
from tkinter import messagebox












#def agendar_tarefa(self,minutos,hora,dia,mes,dia_semana,comando):
def agendar_tarefa():
        '''
        Função configurar tarefa
        '''
    
    
    
               
        
        minutos=tx_minuto.get()
        hora=tx_hora.get()
        dia=tx_dia.get()
        mes=tx_mes.get()
        dia_semana=tx_dia_semana.get()
        comando=tx_arquivo.get("1.0",tk.END)

        if tx_dia.get() == "" or tx_hora.get() == "" or tx_dia_semana.get() == "" or tx_mes.get() == "" or tx_arquivo.get("1.0",tk.END) == "" or tx_minuto.get() == "" :
            messagebox.showinfo("ERRO","EXISTEM CAMPOS EM BRANCO")

        else:
            
            #periodo=minutos+hora+dia+mes+dia_semana+comando
            periodo= "{} {} {} {} {} {}\n".format(minutos,hora,dia,mes,dia_semana,comando)
            with open("tarefas.txt","a") as arquivo:
                arquivo.write(periodo)
            arquivo.close()
            subprocess.run(["crontab","tarefas.txt"])
     
            messagebox.showinfo("Cron-gui","Tarefa gravada com sucesso")



def apagar():
    subprocess.run(["rm","tarefas.txt"])
    subprocess.run(["crontab","-r"])
    messagebox.showinfo("Cron-gui","Tarefa(s) apagada(s) com sucesso") 




     
#instanciando a janela principal
janela=tk.Tk()


#icone da janela


#título da janela
janela.title("Agendador de Tarefas Cron")
janela.geometry("300x350")
janela.config(bg="white")
janela.resizable(False,False)

#título
titulo=tk.Label(text="Agendador de tarefas:",bg="white",height=2)
titulo.grid(row=0,column=1, sticky="NESW")


l_minuto=tk.Label(text="Minutos:",bg="white",height=1)
l_minuto.grid(row=1,column=0, sticky="NESW")

l_minuto_dicas=tk.Label(text=" 0 - 59 | *",bg="white",height=1)
l_minuto_dicas.grid(row=1,column=2, sticky="NESW")



tx_minuto=tk.Entry()
tx_minuto.grid(row=1,column=1,sticky="NESW")

l_hora=tk.Label(text="Hora:",bg="white",height=1)
l_hora.grid(row=2,column=0, sticky="NESW")

l_hora_dicas=tk.Label(text="0 - 23 | *",bg="white",height=1)
l_hora_dicas.grid(row=2,column=2, sticky="NESW")




tx_hora=tk.Entry()
tx_hora.grid(row=2,column=1,sticky="NESW")

l_dia=tk.Label(text="Dia:",bg="white",height=1)
l_dia.grid(row=3,column=0, sticky="NESW")


l_dia_dicas=tk.Label(text="0 - 31| *",bg="white",height=1)
l_dia_dicas.grid(row=3,column=2, sticky="NESW")

tx_dia=tk.Entry()
tx_dia.grid(row=3,column=1,sticky="NESW")

l_mes=tk.Label(text="Mes:",bg="white",height=1)
l_mes.grid(row=4,column=0, sticky="NESW")

l_mes_dicas=tk.Label(text="1 - 12| *",bg="white",height=1)
l_mes_dicas.grid(row=4,column=2, sticky="NESW")


tx_mes=tk.Entry()
tx_mes.grid(row=4,column=1,sticky="NESW")

l_dia_semana=tk.Label(text="Nome dia:",bg="white",height=1)
l_dia_semana.grid(row=5,column=0, sticky="NESW")

l_dia_semana_dicas=tk.Label(text="0 - 7 |*",bg="white",height=1)
l_dia_semana_dicas.grid(row=5,column=2, sticky="NESW")

tx_dia_semana=tk.Entry()
tx_dia_semana.grid(row=5,column=1,sticky="NESW")

l_comando=tk.Label(text="Comando:",bg="white",height=1)
l_comando.grid(row=6,column=0, sticky="NESW")


tx_arquivo=tk.Text(height=5, width=5)
tx_arquivo.grid(row=6,column=1,sticky="NESW")




bt_gravar=tk.Button(text="Gravar",command=agendar_tarefa)
bt_gravar.grid(row=7,column=1,sticky="NESW")

bt_gravar=tk.Button(text="Apagar",command=apagar)
bt_gravar.grid(row=8,column=1,sticky="NESW")

janela.mainloop()





