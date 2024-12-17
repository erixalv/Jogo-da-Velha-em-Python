# -*- coding: utf-8 -*-

class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [ [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO], 
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
                        [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO]]
       
        
    def tem_campeao(self):
        for i in range(3):
            if self.matriz[i] == [1, 1, 1]:
                return Tabuleiro.JOGADOR_0
            if self.matriz[0][i] == 1 and self.matriz[1][i] == 1 and self.matriz[2][i] == 1:
                return Tabuleiro.JOGADOR_0
        if self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] == 1:
            return Tabuleiro.JOGADOR_0     
        if self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0] == 1:
            return Tabuleiro.JOGADOR_0  
        
        for i in range(3):
            if self.matriz[i] == [4, 4, 4]:
                return Tabuleiro.JOGADOR_X
            if self.matriz[0][i] == 4 and self.matriz[1][i] == 4 and self.matriz[2][i] == 4:
                return Tabuleiro.JOGADOR_X
        if self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] == 4:
            return Tabuleiro.JOGADOR_X    
        if self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0] == 4:
            return Tabuleiro.JOGADOR_X  
                   
        return Tabuleiro.DESCONHECIDO