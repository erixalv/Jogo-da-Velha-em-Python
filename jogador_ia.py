# -*- coding: utf-8 -*-
from random import randint

from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro : Tabuleiro, tipo : int):
        super().__init__(tabuleiro, tipo)
            

    def getJogada(self) -> (int, int):
        lista = []
        somaLinha = 0
        somaColuna = 0

        #Verificando R1

        for l in range(0,3):
            for c in range(0,3):
                somaLinha += self.matriz[l][c]
            if somaLinha == 2 or somaLinha == 8:
                for j in range(0,3):
                    if self.matriz[l][j] == Tabuleiro.DESCONHECIDO:
                        return (l, j)
            somaLinha = 0
        
        for c in range(0,3):
            for l in range(0,3):
                somaColuna += self.matriz[l][c]
            if somaColuna == 2 or somaColuna == 8:
                for j in range(0,3):
                    if self.matriz[j][c] == Tabuleiro.DESCONHECIDO:
                        return (j, c)
            somaColuna = 0
                    
        somaDiagonalUm = self.matriz[0][0] + self.matriz[1][1] + self.matriz[2][2]
        
        if somaDiagonalUm == 2 or somaDiagonalUm == 8:
            for i in range(0, 3):
                if self.matriz[i][i] == Tabuleiro.DESCONHECIDO:
                    return (i, i)

        somaDiagonalDois = self.matriz[0][2] + self.matriz[1][1] + self.matriz[2][0]
                
        if somaDiagonalDois == 2 or somaDiagonalDois == 8:
            for i in range(0, 3):
                if self.matriz[i][2-i] == Tabuleiro.DESCONHECIDO:
                    return(i, (2-i))
                
        #Verificando R2:
        for l in range(0,3):
            somal = 0
            for c in range(0,3):
                somal += self.matriz[l][c]
                if somal == 1:
                    linha = l
                    break
                
        for c in range(0,3):
            somac = 0
            for l in range(0,3):
                somac += self.matriz[l][c]
                if somac == 1:
                    coluna = c
                    
                    if linha != None and self.matriz[linha][coluna] == Tabuleiro.DESCONHECIDO:
                        return (linha, coluna)

        #Verificando R3:
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return(1, 1)

        #Verificando R4:
        if self.matriz[0][0] == 4 and self.matriz[2][2] == Tabuleiro.DESCONHECIDO:
            return (2, 2)
        if self.matriz[0][2] == 4 and self.matriz[2][0] == Tabuleiro.DESCONHECIDO:
            return(2, 0)
        if self.matriz[2][0] == 4 and self.matriz[0][2] == Tabuleiro.DESCONHECIDO:
            return (0, 2)
        if self.matriz[2][2] == 4 and self.matriz[0][0] == Tabuleiro.DESCONHECIDO:
            return (0, 0)
        
        #Verificando R5:
        if self.matriz[0][0] == Tabuleiro.DESCONHECIDO:
            return (0, 0)
        if self.matriz[0][2] == Tabuleiro.DESCONHECIDO:
            return(0, 2)
        if self.matriz[2][0] == Tabuleiro.DESCONHECIDO:
            return (2, 0)
        if self.matriz[2][2] == Tabuleiro.DESCONHECIDO:
            return (2, 2)
        

        #Verificando R6:
        for l in range(0,3):
            for c in range(0,3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))

                    
        if(len(lista) > 0):
            p = randint(0, len(lista)-1)
            return lista[p]
        else:
           return None