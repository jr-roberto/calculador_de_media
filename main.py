# REGISTRO
# 1 - Registrar dados do aluno ( Matricula , Nome )
# 2 - Registrar notas AD1 e AD2 para cada aluno.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import os

base_avaliacao = [0]*2

base_aluno = []
base_notas = []

MENU_INICIAL = """
==================
    Menu Inicial

    1 - Adicionar aluno
    2 - Atualizar nota

    0 - Finalizar Programa    
==================
"""

MSG_ERRO = "\n\nOpção invalida ou Erro !\n[Press qualquer tecla p continuar !]\n\n"
MSG_FIM = "\n\nSistema finalizado\nBye bye!\n\n"

class Aluno:
    matricula:str   = None
    nome:str        = None
    avaliacao       = base_avaliacao

def novo_aluno( mat:str , nome:str ):

    for b in base_aluno:
        if b.matricula == mat:
            # Se ja existeir essa mat metodo reotrno False
            return False

    aluno           = Aluno()
    aluno.nome      = nome
    aluno.matricula = mat

    base_aluno.append(aluno)
    
    return True

def atualizar_nota( mat , qual_avaliacao , nota ):
    """qual_avaliacao = Qual a avaliação AD1 ou AD2 ?
    nota= Nota obtida"""

    for b in base_aluno:
        mat_aluno = b.matricula
        if mat_aluno == mat:
            
            if qual_avaliacao == "AD1":
                b.avaliacao[0] = nota

            elif qual_avaliacao == "AD2":
                b.avaliacao[1] = nota

            return True

    return False

def valida_mat():
    n = input('Matricula : ')

    if n.isnumeric():
        if int(n) < 1 or int(n) > 999:

            print("\nMat deve ser um numero valido de 1 a 999")
            return valida_mat()
        
        return "%03d" % int(n)
    
    print("\nMat deve ser um numero valido de 1 a 999")
    valida_mat()

# Tela menu Aluno
def listar_alunos():
    ls_alunos = []
    
    for aluno in base_aluno:
        mat = aluno.matricula
        nome = aluno.nome

        ls_alunos.append( " - ".join( [mat,nome] ) )

    ls = "\n    ".join(ls_alunos)

    menu_aluno = f"""
    ==================
    ====Menu Aluno====
        

    { ls }

    __________________________
        0 - Finalizar Programa

    ==================
    ==================
    """

    return menu_aluno

# Rodando o programa
while True:
    os.system("cls")

    print(MENU_INICIAL)

    try:
        opc_selecionada = int(
            input("Selecione uma opção : ")
        )

        if opc_selecionada == 1:
            mat = valida_mat()
            nome = input('Nome : ')

            result = novo_aluno(mat=mat , nome=nome)

            if result:
                for a in base_aluno:
                    input(a.__dict__)

                continue
            
            else:
                print("|__A mat informada ja existe no sistema !")
                input(MSG_ERRO)

        elif opc_selecionada == 2:
            os.system("cls")

            menu_aluno = listar_alunos()

            print(menu_aluno)

            input(MSG_ERRO)

        if opc_selecionada == 0:
            print(MSG_FIM)
            break

    except:
        input(MSG_ERRO)

# PROCESSO
# 3 - Calcular media AD1 e AD2
# 4 - Se media menor que 7 ( Solicitar ADF )
# 5 - Se ADF for menor que 5 ( reprovado )
# 6 - Se ADF for maior que 5 ( aprovado )

# FUNCOES DO PROGRAMA
# 7 - Possibiltar listar todos os alunos
# 8 - Permitir atualização da nota

# O sistema deve conter esses recursos
"""     
    Variáveis até                       1,0
    Expressões Aritméticas até          1,0
    Expressões Lógicas até              1,0
    Comandos de Entradas e Saídas até   1,0
    Estruturas de Repetição até         2,0
    Estruturas de Condição até          1,0
    Vetores ou Matrizes até             2,0
    Funções ou Classes até              1,0 
"""
