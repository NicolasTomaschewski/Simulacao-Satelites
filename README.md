# Simulação Computacional sobre a Troca de Órbitas de um Satélite Artificial

Resumo:

Este trabalho apresenta o desenvolvimento de simulações computacionais que
auxiliam nos estudos sobre órbitas descritas por satélites artificiais, com foco na
manobra de Hohmann, uma técnica fundamental para a transferência eficiente de
satélites entre órbitas circulares. Além das aplicações práticas na indústria
aeroespacial, este artigo contribui para o desenvolvimento contínuo dos estudos sobre
órbitas, um tema essencial e relevante da física, especialmente em sua área que lida
com simulações computacionais. O objetivo central do trabalho é construir programas
robustos e otimizados desenvolvidos utilizando a linguagem Python, com auxílio de
suas bibliotecas, capazes de representar, com a maior precisão possível, a manobra,
descrita matematicamente em detalhes ao longo dos tópicos do projeto. Durante o
desenvolvimento, diversas ideias foram colocadas em prática, o que é útil para
acompanhar as diferentes versões e a evolução do projeto. O estudo foi bem-sucedido
em demonstrar a eficiência da manobra de Hohmann, bem como sua importância na
indústria. A versão do código desenvolvida para simular as múltiplas trocas em uma
única manobra merece atenção, pois se trata de uma prática real da indústria
aeroespacial que o trabalho conseguiu contemplar com sucesso, além de apresentar
exemplos de órbitas realmente utilizadas na prática. A pesquisa abrange diferentes
versões da manobra de Hohmann, com foco especial em uma representação
bidimensional do sistema, enquanto considera brevemente as possibilidades e
limitações de estudos tridimensionais. Os resultados obtidos não apenas confirmam a
eficiência da manobra de Hohmann, mas também destacam sua relevância prática na
dinâmica orbital e sua aplicação na indústria aeroespacial moderna.



## Arquivos do Projeto
1. Protótipo Inicial
O primeiro passo foi desenvolver um protótipo que realiza os cálculos de troca de órbita e imprime os resultados no terminal. O foco nesta etapa foi garantir a precisão dos cálculos físicos e matemáticos.

2. Simulação em Coordenadas Cartesianas
Após o protótipo, desenvolvemos uma simulação em coordenadas cartesianas que visualiza o movimento do satélite ao longo da troca de órbita. O objetivo foi fornecer uma representação gráfica simples do fenômeno.

3. Simulação em Coordenadas Polares
A simulação foi aprimorada para coordenadas polares, proporcionando uma representação mais precisa dos movimentos orbitais. Este código também foi capaz de resolver automaticamente as equações do protótipo, permitindo uma simulação mais realista e eficiente.

4. Tentativa de Simulação de Órbita em 3D
Uma tentativa de simular a troca de órbitas em 3D foi realizada para fornecer uma visualização espacial mais complexa, levando em consideração fatores como a inclinação e a variação de altitude durante a troca de órbitas.

5. Simulação de Múltiplas Trocas de Órbita
Por fim, o projeto culminou com a criação de um código que simula múltiplas trocas de órbitas, semelhante ao que é feito na indústria aeroespacial, permitindo a visualização de diversas manobras orbitais consecutivas.

## Bibliotecas Utilizadas

Este projeto utiliza diversas bibliotecas do Python para realizar cálculos matemáticos, criar animações e interfaces gráficas. Abaixo estão as bibliotecas usadas e como instalá-las:

1. **NumPy** (`numpy`): Biblioteca para operações matemáticas avançadas, especialmente manipulação de arrays e cálculos numéricos.
   - Instalação:
     ```bash
     pip install numpy
     ```

2. **Matplotlib** (`matplotlib`): Usada para criar gráficos e visualizações, incluindo animações que representam a troca de órbitas.
   - Instalação:
     ```bash
     pip install matplotlib
     ```

3. **Tkinter** (`tkinter`): Biblioteca padrão para criar interfaces gráficas (GUIs) no Python, utilizada para entrada de dados e exibição de mensagens interativas.
   - Esta biblioteca já vem instalada por padrão com o Python em muitos sistemas operacionais. Não há necessidade de instalação adicional. 

4. **mpl_toolkits.mplot3d**: Submódulo do `matplotlib` utilizado para criar gráficos em 3D, permitindo a visualização espacial das órbitas.
   - Ele é instalado junto com `matplotlib`, então não é necessário um comando separado.

5. **Math** (`math`): Biblioteca padrão do Python para operações matemáticas básicas, como trigonometria e exponenciais.
   - Também não requer instalação adicional.

## Artigo Desenvolvido:

Ao final do estudo um artigo foi escrito visando sintetizar e apresentar todos os resultados. 
