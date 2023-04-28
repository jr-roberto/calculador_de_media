import os
import time

class Aluno:
    mat = None
    nome = None
    nota_ad1 = 0
    nota_ad2 = 0
    nota_adf = 0
    media = 0.0
    ficou_adf = False

    # Index
    id_na_lista = None

    def calcular_media(self):
        # Soma de AD1 e AD2
        soma_notas = self.nota_ad1 + self.nota_ad2

        # Media
        self.media = soma_notas / 2

    def atualizar_nota( self , qual_avaliacao:str , nota:int ):
        if qual_avaliacao == "AD1":
            self.nota_ad1 = nota
        
        elif qual_avaliacao == "AD2":
            self.nota_ad2 = nota
        
        elif qual_avaliacao == "ADF":
            self.nota_adf = nota

    def lancar_nota_ad1( self , nota:int ):
        if self.nota_ad1 == 0:
            self.nota_ad1 = nota
            return True
        
        else:
            return False

    def lancar_nota_ad2( self , nota:int ):
        if self.nota_ad2 == 0:
            self.nota_ad2 = nota
            return True
        
        else:
            return False

base_alunos = []

opc_menu = [0,1,2]
MENU_INICIAL = """
Menu Inicial

    1 - Cadastrar Aluno    
    2 - Listar alunos cadastrados

    _____________________
    0 - FINALIZAR SISTEMA
"""

MSG_ERRO = """
Opção Invalida
[Pressione Qualquer Tecla para Reiniciar]
"""

def comando_limp_tela():
    return os.system("cls")

def cadastrar_aluno():
    comando_limp_tela()

    print("""
    Cadatrando novo Aluno

    """)

    try:
        mat = int(input("Mat do Aluno : "))

        if mat < 1:
            print("Matricula deve ser um numero Válido maior que 0 !")
            time.sleep(3)
            return cadastrar_aluno()

        nome = input("Nome do Aluno : ")

        aluno = Aluno()
        aluno.nome = nome
        aluno.mat = "%04d" % mat

        base_alunos.append(aluno)

        print("\n\nAluno cadastrado !")
        time.sleep(1)
        return True
    except:
        input(MSG_ERRO)
        return cadastrar_aluno()

opc_lista = []
def listar_alunos():
    comando_limp_tela()
    opc_lista.clear()

    ls_alunos = []

    print(" id| Mat    Nome")
    for i,al in enumerate(base_alunos):
        al.id_na_lista = i + 1

        opc_lista.append(i + 1)

        n = "%02d" % al.id_na_lista

        str_ls = f" { n }| { al.mat } - { al.nome }"

        print(str_ls)

        ls_alunos.append(str_ls)

    if len(base_alunos) == 0:
        print("\n\n     Ainda nao Existe dados !")

    return

def menu_aluno(id):
    print("------------")

    for al in base_alunos:
        if al.id_na_lista == id:
            
            print(f"    Mat    : {al.mat}")
            print(f"    Nome   : {al.nome}\n\n\n")
            print(f"    Menu opçoes p o Aluno")
            print(f"    -----------------")
            print(f"    1 - Atualizar AD1")
            print(f"    2 - Atualizar AD2")
            print(f"    3 - Atualizar AD1 e AD2\n")
            print(f"    4 - Resultado média")
            result = int(input(f"\n    Selecione uma opcao : "))

            break

    return result

def atualiza_ad1(id):
    for al in base_alunos:
        if al.id_na_lista == id:
            nota = int(input("  Informe a nota AD1 : "))
            al.nota_ad1 = nota


while True:
    comando_limp_tela()

    # Menu Inicial
    print(MENU_INICIAL)

    try:
        # Usuario
        res_usuario = int(input("\n\nSelecionar uma opção : "))

        # Se opção valida vai entrar nessa condição
        if res_usuario in opc_menu:

            if res_usuario == 0:
                break

            elif res_usuario == 1:
                cadastrar_aluno()

            elif res_usuario == 2:
                listar_alunos()

                res_lista = int(input("\n\nSelecionar aluno por ID : "))

                if res_lista in opc_lista:
                    res_menu_al = menu_aluno(res_lista)

                    if res_menu_al == 1:
                        atualiza_ad1(res_lista)



    except:
        input(MSG_ERRO)

comando_limp_tela()
print("\n\n Sistema Finalizado !\n  Bye bye.\n\n")

time.sleep(3)