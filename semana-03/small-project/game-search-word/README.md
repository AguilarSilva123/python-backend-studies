# Resolvedor de caca-palavras

Projeto didatico em Python para encontrar palavras em uma matriz de letras.

## Ideia principal

Cada palavra pode aparecer em 8 direcoes:

- direita
- esquerda
- baixo
- cima
- diagonais nos quatro sentidos

O algoritmo faz uma varredura da matriz da esquerda para a direita e de cima
para baixo. Em cada celula, ele verifica todas as palavras ainda nao
encontradas. Se a primeira letra da palavra combina com a letra da celula, ele
tenta continuar a palavra em cada uma das 8 direcoes.

## Onde entra a recursividade

A funcao `_buscar_recursivo` verifica uma letra por vez:

1. Confere se a posicao esta dentro da matriz.
2. Compara a letra da matriz com a letra esperada da palavra.
3. Guarda a coordenada no caminho.
4. Se ainda faltam letras, chama a si mesma para a proxima coordenada.

Essa pilha de chamadas guarda o estado da busca na memoria: palavra, indice da
letra atual, posicao atual, direcao e caminho percorrido.

## Simultaneo vs paralelo

O metodo `resolver_simultaneo` simula buscas simultaneas: a matriz e percorrida
uma unica vez e, em cada celula, todas as palavras ainda pendentes sao testadas.

O metodo `resolver_paralelo` usa `ThreadPoolExecutor` para procurar cada palavra
em uma thread separada. Para matrizes pequenas, isso e mais util para estudo do
que para desempenho.

## Como executar

```bash
python cacapalavras.py
```

Com a matriz grande usada no exemplo, o retorno atual e:

- `VIDA`: encontrada para a direita.
- `MORCEGO`: encontrada para baixo.
- `LUA`: encontrada para baixo.
- `CASA`: nao encontrada.
- `OSTENTACAO`: nao encontrada.
- `CABIDE`: nao encontrada.

As palavras nao encontradas nao aparecem nessa matriz de forma continua em
nenhuma das 8 direcoes.

## Como testar as 8 direcoes

```bash
python -m unittest -v
```

O arquivo `test_cacapalavras.py` tem um teste didatico com uma palavra em cada
direcao possivel.

## Exemplo de uso

```python
from cacapalavras import CacaPalavras

matriz = [
    ["P", "Y", "T", "H", "O", "N"],
    ["A", "B", "C", "D", "E", "F"],
]

palavras = ["python", "java"]

jogo = CacaPalavras(matriz)
resultados = jogo.resolver_simultaneo(palavras)
```
