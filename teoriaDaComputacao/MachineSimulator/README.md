# Simulador de Máquinas de estados


### Nesse simulador desenvolvemos as três principais máquina:
* Automato Finito Determinísticos(Linguagens Regulares) - AFD 
  * Recebe a entradas e troca pro proximo estado 
* Automato de Pilha(Linguagens Livre de Contexto) - AP
  * Recebe a entrada, lê algo da pilha, escreve alguma coisa e troca pro proxima estado
* Máquina de Turing(Linguagens Recursivas) - MT
  * Recebe a entrada, anda a direita e a esquerda conforme o problema e troca de estado


### Funcionamento

<p>Esse simulador primeiro lê o arquivo specs.txt para identificar qual a máquina 
e suas propriedades, depois recebe um arquivo input.txt para reconhecer as entradas.
Ao final ele gera um arquivo output.txt que informa se as entradas foram ou aceitam ou rejeitadas 
</p>



### AFND

#### specs.txt
    1 F (tipo da máquina [T/P/F])
    2 I (estado inicial (número))
    3 F1,F2,F3 (estados finais (número))
    4 F,COND,T
    5 ()
    ...
    N ()

#### input.txt
    1 a
    2 b
    3 ab
    4 ba

#### output.txt
    1 R;a (R - Rejeita)
    2 A;b (A - Aceita)
    3 A;ab
    4 R;ba

### AP

#### specs.txt
    1 P (tipo da máquina [T/P/F])
    2 I (estado inicial (número))
    3 F1,F2,F3 (estados finais (número))
    4 F,COND,T
    5 ()
    ...
    N ()

#### input.txt
    1 aabb
    2 aaabb
    3 aabbb
    4 aaabbb
    5 ab
    6 aaaaabbbbb
    7 abbaaabbbbaaababbaba

#### output.txt
    1 A;aabb
    2 R;aaabb
    3 R;aabbb
    4 A;aaabbb
    5 A;ab
    6 A;aaaaabbbbb
    7 R;abbaaabbbbaaababbaba

### MT

#### specs.txt
    1 T (tipo da máquina [T/P/F])
    2 I (estado inicial (número))
    3 F1,F2,F3 (estados finais (número))
    4 F,COND,T
    5 ()
    ...
    N ()

#### input.txt
    1 ab
    2 aabb
    3 aaabbb
    4 abbb

#### output.txt
    1  A;ABx
    2  A;AABBx
    3  A;AAABBBx
    4  R;ABbb



    


### Como utilizar


     Altere os aqrquivos "specs.txt" e "input.txt" de acordo com a maquina que deseja usar e em seguida execute o arquivo main 
