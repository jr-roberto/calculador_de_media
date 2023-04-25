# REGISTRO
# 1 - Registrar dados do aluno ( Matricula , Nome )
# 2 - Registrar notas AD1 e AD2 para cada aluno.

import os

base_avaliacao = [0]*2

base_aluno = []
base_notas = []

MAIN_MENU = """
==================
    Menu Inicial

    1 - Adicionar aluno
    2 - Atualizar nota

    0 - Finalizar Programa    
==================
"""

MSG_ERRO = "Opção invalida !"

class Aluno:
    matricula:int   = None
    nome:str        = None
    avaliacao       = base_avaliacao

def novo_aluno( mat:int , nome:str ):

    for b in base_aluno:
        if b.matricula == mat:
            return "A matricula informada ja existe !"

    aluno           = Aluno()
    aluno.nome      = nome
    aluno.matricula = mat
    
    return  base_aluno.append(aluno)

def atualizar_nota( mat , qual_avaliacao , nota ):
    "qual_avaliacao = Qual a avaliação AD1 ou AD2 ?\nnota= Nota obtida"

    for b in base_aluno:
        mat_aluno = b.matricula
        if mat_aluno == mat:
            
            if qual_avaliacao == "AD1":
                b.avaliacao[0] = nota

            elif qual_avaliacao == "AD2":
                b.avaliacao[1] = nota

            return True

    return False

def valida_nota():
    
    
    input()

# Rodando o programa
while True:
    os.system("cls")

    print(MAIN_MENU)

    try:
        opc_selecionada = int(
            input("Selecione uma opção : ")
        )

        if opc_selecionada == 1:
            
            result = novo_aluno()

        if opc_selecionada == 0:
            print("\n\nPrograma finalizado !\nBye Bye.")
            break
    except:
        print("\n" + MSG_ERRO + "\n")

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
