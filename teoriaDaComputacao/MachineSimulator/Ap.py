def Ap(state=None,  # Estado inicial
       rules=[],  # Regras de transição
       tape=[],  # Fita de input
       final=None,  # Estado final
       pos=0):  # Posição seguinte da maquina

    st = state
    des = 0
    emp = 0
    cont = 0
    if pos < 0: pos += len(tape)
    if pos >= len(tape) or pos < 0: raise EOFError("Possição inicial invalida")

    rules = dict(((s0, v0), (v1,v2, s1)) for (s0, v0, v1, v2, s1) in rules)
    """
  Estado inicial	Símbolo lido na fita	Símbolo lido na pilha   simbolo escrito na pilha	  Estado sig.
  p(s0)	                1(v0)	                x(v1)                     x(v2)                   p(s1)
"""
    k=str(tape)
    kcerto=k.replace("\'", '').replace(",", " ").replace(";", " ").replace("[", "").replace("]", "").replace(" ", "")

    while True:
        print(st, '\t', end=" ")
        for i, v in enumerate(tape):
            if i == pos:
                print("[%s]" % (v,), end=" ")
            else:
                print(v, end=" ")
        print()


        if st == final and cont==len(tape):

            with open("output.txt", "a") as resultado:
                resultado.write("A;"+kcerto+"\n")
            break

        if (st, tape[pos]) not in rules:
            with open("output.txt", "a") as resultado:
                resultado.write("R;"+kcerto+"\n")
            break

        (v1,v2, s1) = rules[(st, tape[pos])]
        st = s1

        if v2 == "_":
            tape[cont] = v2
            tape[pos] = v2
            des+=1
            pos+=1
            cont+=1

            if des > emp and v1!="Z":
                with open("output.txt", "a") as resultado:
                    resultado.write("R;" + kcerto + "\n")
                break

            if pos == len(tape):
                pos=cont

        else:
            emp += 1
            tape[pos] = v2
            pos += 1

            if pos == len(tape):
                pos=0