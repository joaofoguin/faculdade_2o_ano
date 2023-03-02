def turing_M(state=None,  # Estados da maquina
             blank=None,  # Simbolo vazio do alfabeto
             rules=[],  # Regras de transição
             tape=[],  # Fita
             final=None,  # Estado final
             pos=0):  # Posição seguinte da maquina

    st = state
    if not tape: tape = [blank]
    if pos < 0: pos += len(tape)
    if pos >= len(tape) or pos < 0: raise EOFError("Posição inicial invalida")

    rules = dict(((s0, v0), (v1, dr, s1)) for (s0, v0, v1, dr, s1) in rules)
    """
Estado	Símbolo lido	Símbolo escrito	       Mov. 	Estado sig.
  p(s0)	       1(v0)	         x(v1)         R(dr)	     p(s1)
"""



    while True:
        print(st, '\t', end=" ")
        for i, v in enumerate(tape):
            if i == pos:
                print("[%s]" % (v,), end=" ")
            else:
                print(v, end=" ")
        print()

        if st == final:
            print(tape)
            break

        if (st, tape[pos]) not in rules:
            k = ''.join([str(item) for item in tape])
            with open("output.txt", "a") as resultado:
                if "x" in k:
                    resultado.write(" A;"+k+ "\n")
                else:
                    resultado.write(" R;"+k+ "\n")
            break

        (v1, dr, s1) = rules[(st, tape[pos])]
        tape[pos] = v1  # Reescreve na fita


        # Movimento da cabeça de leitura
        if dr == 'L':
            if pos > 0:
                pos -= 1
            else:
                tape.insert(0, blank)
        if dr == 'R':
            pos += 1
            if pos >= len(tape): tape.append(blank)
        st = s1