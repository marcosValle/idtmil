#!/usr/bin/env python

from random import randint
from math import ceil
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--random", help="Gera idt válida aleatória",
                action="store_true")
parser.add_argument("-t", "--todas", help="Gera todas as idts com a gir e série selecionadas",
                action="store_true")
parser.add_argument("-g", "--gir", help="Gera idts apenas deste GIR", type=int, default=None)
parser.add_argument("-s", "--serie", help="Gera idts apenas desta serie", type=int, default=None)
parser.add_argument("-q", "--qnt", help="Quantidade de idts aleatórias a serem geradas", type=int, default=1)
args = parser.parse_args()

print("""

***************************************
*                    ,----,           *
*                  ,/   .`|           *
*   .--.--.      ,`   .'  :   ,---,.  *
*  /  /    '.  ;    ;     / ,'  .' |  *
* |  :  /`. /.'___,/    ,',---.'   |  *
* ;  |  |--` |    :     | |   |   .'  *
* |  :  ;_   ;    |.';  ; :   :  |-,  *
*  \  \    `.`----'  |  | :   |  ;/|  *
*  ` ----.   \   '   :  ; |   :   .'  *
*   __ \  \  |   |   |  ' |   |  |-,  *
*  /  /`--'  /   '   :  | '   :  ;/|  *
* '--'.     /    ;   |.'  |   |    \  *
*   `--'---'     '---'    |   :   .'  *
*                         |   | ,'    *
*                         `----'      *
***************************************
* Gerador Idt Mil EB Ver. 0.0.1       *
* Coded by Sec Tec Esp                *
***************************************
        """)

class Idt():
    def __init__(self, gir=None, serie=None):
        self.gir = gir
        self.serie = serie
        self.checkGirSerie()

    def checkGirSerie(self):
        if self.gir!=None:
            if not (self.gir>=1 and self.gir<=12):
                args = parser.print_help()
                exit(1)

        if self.serie!=None:
            if not (self.serie>=0 and self.serie<=9):
                args = parser.print_help()
                exit(1)

    def genRand(self):
        gir = self.gir
        serie = self.serie

        if not gir:
            gir = randint(1, 12)

        if not serie:
            serie = randint(0, 9)

        registro = randint(1, 999999)

        idtNaoVerificada = '{:02d}{:06d}{}'.format(gir, registro, serie)

        verificador =  self.genVerificador(idtNaoVerificada)

        return idtNaoVerificada + str(verificador)

    def genVerificador(self, idtNaoVerificada):
        verificador = 0

        for i in idtNaoVerificada[::2]:
            verificador += 2*int(i)

        for i in idtNaoVerificada[1::2]:
            verificador += int(i)

        return int(ceil(verificador / 10.0)) * 10 - verificador

    def genTodas(self):
        gir = self.gir
        serie = self.serie
        if not gir:
            if not serie:
                for i in range(1,13):
                    for j in range(0,10):
                        for k in range(1,1000000):
                            idtNaoVerificada = str(i).zfill(2)+str(k).zfill(6)+str(j)
                            print(idtNaoVerificada + str(self.genVerificador(idtNaoVerificada)))
            else:
                for i in range(1,13):
                    for k in range(1,1000000):
                        idtNaoVerificada = str(i).zfill(2)+str(k).zfill(6)+str(serie)
                        print(idtNaoVerificada + str(self.genVerificador(idtNaoVerificada)))
        elif serie:
            for k in range(1,1000000):
                idtNaoVerificada = str(gir).zfill(2)+str(k).zfill(6)+str(serie)
                print(idtNaoVerificada + str(self.genVerificador(idtNaoVerificada)))

        elif not serie:
            for j in range(1,9):
                for k in range(1,1000000):
                    idtNaoVerificada = str(gir).zfill(2)+str(k).zfill(6)+str(j)
                    print(idtNaoVerificada + str(self.genVerificador(idtNaoVerificada)))

def menu():

    if not len(sys.argv) > 1:
        parser.print_help()
        exit(1)

    idt = Idt(args.gir, args.serie)

    if args.random:
        for i in range(args.qnt):
            print("Idt gerada >> " + idt.genRand())
    elif args.todas:
        print(idt.genTodas())
    else:
        parser.print_help()
menu()
