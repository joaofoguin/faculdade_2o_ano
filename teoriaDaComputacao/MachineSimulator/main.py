import Turing
import Afnd
import Ap


# leitura das specs
def leitorEspec(arquivo):
    with open("especs.txt", "r") as leitor:
        maquina = leitor.readline().rstrip()
        estadoInicial = leitor.readline().rstrip()
        estadosFinais = leitor.readline().rstrip().split(",")
        condicoes = leitor.read().splitlines()
    return maquina, estadoInicial, estadosFinais, condicoes


maquina, estadoInicial, estadosFinais, condicoes = leitorEspec('especs.txt')
for i in range(len(condicoes)):
    condicoes[i] = condicoes[i].replace(",", " ").replace(";", " ").split()


# leitura dos inputs
def leitorInput(arquivo):
    with open("input.txt", "r") as leitor:
        inputi = leitor.read().splitlines()
    return inputi


inputi = leitorInput('input.txt')

if maquina == 'T':
    with open("output.txt", 'w') as f:
        pass

    for i in range(len(inputi)):
        Turing.turing_M(state=estadoInicial,
                        blank='x',
                        tape=list(inputi[i]),
                        final=estadosFinais,
                        rules=condicoes
                        )

if maquina == 'F':
    with open("output.txt", 'w') as f:
        pass

    for i in range(len(estadosFinais)):
        estf = estadosFinais[i]

    for i in range(len(inputi)):
        Afnd.afd_M(state=estadoInicial,
                   tape=list(inputi[i]),
                   rules=condicoes,
                   final=estf
                   )

if maquina == 'P':
    with open("output.txt", 'w') as f:
        pass

    for i in range(len(estadosFinais)):
        estf = estadosFinais[i]

    for i in range(len(inputi)):
        Ap.Ap(state=estadoInicial,
              tape=list(inputi[i]),
              rules=condicoes,
              final=estf
              )
