import unittest

from cacapalavras import CacaPalavras


class TestCacaPalavras(unittest.TestCase):
    def test_encontra_palavras_em_todas_as_direcoes(self) -> None:
        matriz = [
            ["V", "I", "D", "A", "L", "L", "X"],
            ["A", "S", "A", "C", "U", "O", "X"],
            ["D", "E", "S", "C", "A", "S", "X"],
            ["X", "R", "U", "X", "X", "X", "M"],
            ["X", "E", "I", "X", "Z", "A", "X"],
            ["C", "X", "X", "O", "R", "A", "X"],
            ["X", "X", "X", "X", "X", "X", "P"],
        ]
        palavras = ["vida", "casa", "lua", "sol", "rio", "mar", "ceu", "paz"]

        resultados = CacaPalavras(matriz).resolver_simultaneo(palavras)

        self.assertEqual(resultados["VIDA"].direcao, "direita")
        self.assertEqual(resultados["CASA"].direcao, "esquerda")
        self.assertEqual(resultados["LUA"].direcao, "baixo")
        self.assertEqual(resultados["SOL"].direcao, "cima")
        self.assertEqual(resultados["RIO"].direcao, "diagonal baixo-direita")
        self.assertEqual(resultados["MAR"].direcao, "diagonal baixo-esquerda")
        self.assertEqual(resultados["CEU"].direcao, "diagonal cima-direita")
        self.assertEqual(resultados["PAZ"].direcao, "diagonal cima-esquerda")

    def test_matriz_do_exemplo_do_usuario(self) -> None:
        matriz = [
            ['V','I','D','A','Q','M','H','R','K','L','P','N','B','C','D','E','F','G','H','I'],
            ['X','Y','Z','T','U','O','A','M','N','P','Q','R','S','T','U','V','W','X','Y','Z'],
            ['L','K','J','C','F','R','B','O','P','Q','R','S','T','U','V','W','X','Y','Z','A'],
            ['P','O','N','M','A','C','I','R','D','E','F','G','H','I','J','K','L','M','N','O'],
            ['A','S','D','F','G','E','D','L','Q','R','S','T','U','V','W','X','Y','Z','A','B'],
            ['Q','W','E','R','T','G','E','U','A','B','C','D','E','F','G','H','I','J','K','L'],
            ['Z','X','C','V','B','O','F','A','D','E','F','G','H','I','J','K','L','M','N','O'],
            ['A','B','C','D','E','R','G','L','H','I','J','K','L','M','N','O','P','Q','R','S'],
            ['T','S','R','Q','P','C','H','X','I','J','K','L','M','N','O','P','Q','R','S','T'],
            ['U','V','W','X','Y','E','I','J','C','K','L','M','N','O','P','Q','R','S','T','U'],
            ['A','C','A','T','N','E','T','S','O','L','M','N','A','O','P','Q','R','S','T','V'],
            ['V','W','X','Y','Z','G','J','K','L','A','N','B','C','P','Q','R','S','T','U','W'],
            ['A','B','C','D','E','O','L','M','N','O','B','Q','R','S','T','U','V','W','X','X'],
            ['F','G','H','I','J','M','N','O','P','Q','R','I','S','T','U','V','W','X','Y','Y'],
            ['K','L','A','M','N','Z','O','P','Q','R','S','T','D','U','V','W','X','Y','Z','Z'],
        ]
        palavras = ["vida", "morcego", "casa", "lua", "ostentacao", "cabide"]

        resultados = CacaPalavras(matriz).resolver_simultaneo(palavras)

        self.assertTrue(resultados["VIDA"].encontrada)
        self.assertTrue(resultados["MORCEGO"].encontrada)
        self.assertTrue(resultados["LUA"].encontrada)
        self.assertFalse(resultados["CASA"].encontrada)
        self.assertFalse(resultados["OSTENTACAO"].encontrada)
        self.assertFalse(resultados["CABIDE"].encontrada)


if __name__ == "__main__":
    unittest.main()
