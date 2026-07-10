from __future__ import annotations

from dataclasses import dataclass
from concurrent.futures import ThreadPoolExecutor
from typing import Iterable


@dataclass(frozen=True)
class Coordenada:
    linha: int
    coluna: int


@dataclass(frozen=True)
class Direcao:
    nome: str
    delta_linha: int
    delta_coluna: int


@dataclass(frozen=True)
class Resultado:
    palavra: str
    encontrada: bool
    inicio: Coordenada | None = None
    fim: Coordenada | None = None
    direcao: str | None = None
    caminho: tuple[Coordenada, ...] = ()


DIRECOES = (
    Direcao("direita", 0, 1),
    Direcao("esquerda", 0, -1),
    Direcao("baixo", 1, 0),
    Direcao("cima", -1, 0),
    Direcao("diagonal baixo-direita", 1, 1),
    Direcao("diagonal baixo-esquerda", 1, -1),
    Direcao("diagonal cima-direita", -1, 1),
    Direcao("diagonal cima-esquerda", -1, -1),
)


class CacaPalavras:
    def __init__(self, matriz: list[list[str]]) -> None:
        self.matriz = self._normalizar_matriz(matriz)
        self.total_linhas = len(self.matriz)
        self.total_colunas = len(self.matriz[0]) if self.total_linhas else 0
        self._validar_matriz_retangular()

    def resolver_simultaneo(self, palavras: Iterable[str]) -> dict[str, Resultado]:
        """
        Busca todas as palavras no mesmo fluxo de varredura.

        Para cada celula da matriz, todas as palavras que ainda nao foram
        encontradas olham essa mesma celula como possivel inicio. Isso simula
        varias buscas acontecendo juntas, sem precisar criar threads.
        """
        palavras_normalizadas = [self._normalizar_palavra(palavra) for palavra in palavras]
        resultados = {
            palavra: Resultado(palavra=palavra, encontrada=False)
            for palavra in palavras_normalizadas
        }

        for linha in range(self.total_linhas):
            for coluna in range(self.total_colunas):
                atual = self.matriz[linha][coluna]

                for palavra in palavras_normalizadas:
                    if resultados[palavra].encontrada or not palavra:
                        continue

                    if palavra[0] != atual:
                        continue

                    resultado = self._tentar_palavra(palavra, Coordenada(linha, coluna))
                    if resultado.encontrada:
                        resultados[palavra] = resultado

        return resultados

    def resolver_paralelo(self, palavras: Iterable[str]) -> dict[str, Resultado]:
        """
        Busca cada palavra em uma thread.

        Para caca-palavras pequenos isso costuma ser mais didatico do que
        rapido, porque o custo de criar threads pode ser maior que a busca.
        """
        palavras_normalizadas = [self._normalizar_palavra(palavra) for palavra in palavras]

        with ThreadPoolExecutor() as executor:
            resultados = executor.map(self._resolver_uma_palavra, palavras_normalizadas)

        return {resultado.palavra: resultado for resultado in resultados}

    def _resolver_uma_palavra(self, palavra: str) -> Resultado:
        if not palavra:
            return Resultado(palavra=palavra, encontrada=False)

        for linha in range(self.total_linhas):
            for coluna in range(self.total_colunas):
                if self.matriz[linha][coluna] == palavra[0]:
                    resultado = self._tentar_palavra(palavra, Coordenada(linha, coluna))
                    if resultado.encontrada:
                        return resultado

        return Resultado(palavra=palavra, encontrada=False)

    def _tentar_palavra(self, palavra: str, inicio: Coordenada) -> Resultado:
        if len(palavra) == 1:
            return Resultado(
                palavra=palavra,
                encontrada=True,
                inicio=inicio,
                fim=inicio,
                direcao="unica letra",
                caminho=(inicio,),
            )

        for direcao in DIRECOES:
            caminho: list[Coordenada] = []
            encontrou = self._buscar_recursivo(
                palavra=palavra,
                indice=0,
                posicao=inicio,
                direcao=direcao,
                caminho=caminho,
            )

            if encontrou:
                return Resultado(
                    palavra=palavra,
                    encontrada=True,
                    inicio=caminho[0],
                    fim=caminho[-1],
                    direcao=direcao.nome,
                    caminho=tuple(caminho),
                )

        return Resultado(palavra=palavra, encontrada=False)

    def _buscar_recursivo(
        self,
        palavra: str,
        indice: int,
        posicao: Coordenada,
        direcao: Direcao,
        caminho: list[Coordenada],
    ) -> bool:
        """
        Verifica uma letra e chama a si mesma para a proxima letra.

        A pilha de chamadas guarda na memoria em que letra estamos, qual
        posicao da matriz estamos lendo e qual direcao deve ser mantida.
        """
        if not self._esta_dentro_da_matriz(posicao):
            return False

        letra_esperada = palavra[indice]
        letra_encontrada = self.matriz[posicao.linha][posicao.coluna]

        if letra_encontrada != letra_esperada:
            return False

        caminho.append(posicao)

        if indice == len(palavra) - 1:
            return True

        proxima_posicao = Coordenada(
            linha=posicao.linha + direcao.delta_linha,
            coluna=posicao.coluna + direcao.delta_coluna,
        )

        encontrou = self._buscar_recursivo(
            palavra=palavra,
            indice=indice + 1,
            posicao=proxima_posicao,
            direcao=direcao,
            caminho=caminho,
        )

        if not encontrou:
            caminho.pop()

        return encontrou

    def _esta_dentro_da_matriz(self, posicao: Coordenada) -> bool:
        return (
            0 <= posicao.linha < self.total_linhas
            and 0 <= posicao.coluna < self.total_colunas
        )

    def _validar_matriz_retangular(self) -> None:
        if not self.matriz:
            raise ValueError("A matriz nao pode estar vazia.")

        for linha in self.matriz:
            if len(linha) != self.total_colunas:
                raise ValueError("Todas as linhas da matriz devem ter o mesmo tamanho.")

    @staticmethod
    def _normalizar_matriz(matriz: list[list[str]]) -> list[list[str]]:
        return [[letra.strip().upper() for letra in linha] for linha in matriz]

    @staticmethod
    def _normalizar_palavra(palavra: str) -> str:
        return palavra.strip().upper()


def imprimir_resultados(resultados: dict[str, Resultado]) -> None:
    for palavra, resultado in resultados.items():
        if not resultado.encontrada:
            print(f"{palavra}: nao encontrada")
            continue

        caminho = " -> ".join(
            f"({coordenada.linha}, {coordenada.coluna})"
            for coordenada in resultado.caminho
        )
        print(
            f"{palavra}: encontrada | "
            f"inicio={resultado.inicio} | "
            f"fim={resultado.fim} | "
            f"direcao={resultado.direcao} | "
            f"caminho={caminho}"
        )


if __name__ == "__main__":
    matriz_exemplo = [
        ['V','I','D','A','Q','M','T','Y','U','I','O','P','A','S','D','F','G','H','J','K'],
        ['L','P','O','I','U','O','C','R','E','W','Q','A','S','D','F','G','H','J','K','L'],
        ['Z','X','C','A','V','R','B','N','M','Q','W','E','R','T','Y','U','I','O','P','A'],
        ['Q','W','E','R','S','C','T','Y','U','I','O','P','A','S','D','F','G','H','J','K'],
        ['A','S','D','F','G','E','A','P','Q','W','E','R','T','Y','U','I','O','P','A','S'],
        ['Z','X','C','V','B','G','R','L','K','J','H','G','F','D','S','A','Q','W','E','R'],
        ['Q','W','E','R','T','O','A','U','P','O','I','U','Y','T','R','E','W','Q','A','S'],
        ['A','S','D','F','G','M','Q','L','Z','X','C','V','B','N','M','L','K','L','H','G'],
        ['Q','W','C','R','T','Y','U','I','O','A','A','S','D','F','G','H','J','U','L','Z'],
        ['X','C','V','A','Y','U','I','O','S','L','K','J','H','G','F','D','S','A','Q','W'],
        ['A','C','A','T','B','E','T','A','E','T','S','O','L','M','N','B','V','C','X','Z'],
        ['Q','W','E','R','T','I','Y','U','I','O','P','A','S','D','F','G','H','J','K','L'],
        ['Z','X','C','V','B','N','D','M','Q','W','E','R','T','Y','U','I','O','P','A','S'],
        ['A','S','D','F','G','H','J','E','K','L','Z','X','C','V','B','N','M','Q','W','E'],
        ['Q','W','E','R','T','Y','U','P','I','O','A','O','S','T','E','N','T','A','R','M']
]

    palavras_exemplo = ["vida", "morcego", "cabide", "casa", "lua", "ostentar"]

    jogo = CacaPalavras(matriz_exemplo)
    resultados_simultaneos = jogo.resolver_simultaneo(palavras_exemplo)

    imprimir_resultados(resultados_simultaneos)
