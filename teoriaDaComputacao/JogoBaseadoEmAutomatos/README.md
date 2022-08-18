# Labirinto Game

![Union](https://user-images.githubusercontent.com/62312787/185272191-fd7a68de-3668-408b-94f2-d57fef128bfa.png)


<h2>Um protótipo desenvolvido através do Figma utilizando Automatos Finitos para o trabalho de Teoria da Computação.</h2>

# Implementação

O jogo é baseado em cliques, ou seja, é possível joga-lo apenas com o mouse. Foi construído com imagens retiradas do jogo Minecraft da Majong, onde um labirinto foi contruído baseando-se no mapa a seguir. Além de edições produzidas em Photoshop, o protótipo foi montado no software web Figma para desktop.

![WhatsApp Image 2022-08-17 at 11 33 00](https://user-images.githubusercontent.com/62312787/185281389-9b2526d0-a745-481e-84e4-65c764e5a99d.jpeg)

# Inicialização e execução

Para visualização do protótipo recomenda-se o uso de um computador para uma melhor experiência. O uso da internet é necessário para a execução do mesmo.
No primeiro link abaixo, você pode acessar contrução do projeto com as fotos, caminhos e edições prontas. No segundo link, a execução do jogo.

- Link 1: https://www.figma.com/file/mFm18aQYPWecCqj9LBSQNK/Jogo-Com-Automatos?node-id=1%3A41
- Link 2: https://www.figma.com/proto/mFm18aQYPWecCqj9LBSQNK/Jogo-Com-Automatos?node-id=30%3A703&scaling=contain&page-id=0%3A1&starting-point-node-id=30%3A703

# Funcionamento

Na tela inicial é apresentado a capa do jogo, dispondo o nome "LABIRINTO GAME" e o botão "JOGAR". Em seguida, apresenta uma pequena apresentação explicativa do jogo. Assim que é iniciado, o protótipo mostra uma tela com o primeiro frame. Cada frame possui comandos no lado inferior da tela, dentre eles: "ESQUERDA", "SEGUIR", "VOLTAR", "DIREITA" e "ABRIR". bDe acordo com cada cenário, indicadores acima das palavras mostram quais comandos estão disponíveis para a movimentação do jogador. Se em um cenário, não houver bifurcações ou interações de "ABRIR', os comandos "SEGUIR" e "VOLTAR" Como nos exemplos abaixo:

![MacBook Pro 14_ - 10](https://user-images.githubusercontent.com/62312787/185281611-58bdca87-4586-40b2-866c-0a48010e6e4d.png)

![MacBook Pro 14_ - 14](https://user-images.githubusercontent.com/62312787/185281615-f52bd20e-c5c1-41d3-b3b8-1a2afcaa356a.png)

O objetivo do jogo é sair de um labirinto, e para isso é necessário, primeiramente, encontrar uma chave que abrirá a porta de saída dele.

# Embasamento e solução

Para a lógica do protótipo, utilizamos como base um modelo de Linguagem Regular, os Automatos Finitos Determinísticos. Você pode acessar o pdf do mapa abaixo.

[Jogo Com Automatos.pdf](https://github.com/joaofoguin/faculdade_2o_ano/files/9367174/Jogo.Com.Automatos.pdf)

No mapa, é usado as siglas de referência:
- E -> ESQUERDA
- S -> SEGUIR
- V -> VOLTAR
- D -> DIREITA
- A -> ABRIR

Assim como na produção do jogo, os comandos seguem as mesmas ordens. Para uma partida perfeita, você deve seguir a seguinte sequência:

S > D > S > D > S > S > S > S > D > S > A > V > V > E > S > S > E > S > S > E > S > S > S > S > D > S > E > D > A > S.

# Considerações

Não foi possível no momento a implementação em código pela complexidade e tamanha dificuldade de jogo. Porém, seu protótipo já demonstra como seria sua jogabilidade.
<h2>Divirta-se!</h2>
