def afd_M(state=None,  # Estado inicial
          rules=[],  # Regras de transição
          tape=[],      #Fita de input
          final=None,  # Estado final
          pos=0):  # Posição seguinte da maquina

    st = state  # seta o estado inicial
    if pos < 0: pos += len(tape)
    if pos >= len(tape) or pos < 0: raise EOFError("Possição inicial invalida")

    rules = dict(((s0, v0), (v1)) for (s0, v0, v1) in rules)
    """
Estado	 Símbolo lido	 Estado que vai	    
  p(s0)	       1(v0)	         p(v1)         	     
"""
    while True:
        print(st, '\t', end=" ")  # estado incial
        for i, v in enumerate(tape):
            if i == pos:
                print("[%s]" % (v,), end=" ")
            else:
                print(v, end=" ")
        print()

        if st == final and pos == len(tape):
            k = ''.join([str(item) for item in tape])
            with open("output.txt", "a") as resultado:
                resultado.write("A;"+k+"\n")
            break

        if st != final and pos == len(tape):
            k = ''.join([str(item) for item in tape])
            with open("output.txt", "a") as resultado:
                resultado.write("R;"+k+"\n")
            break

        if (st, tape[pos]) not in rules:
            k = ''.join([str(item) for item in tape])
            with open("output.txt", "a") as resultado:
                resultado.write("R;"+k+"\n")
            break

        v1 = rules[(st, tape[pos])]

        st = v1
        pos += 1