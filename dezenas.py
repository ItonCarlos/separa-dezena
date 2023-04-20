# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 00:16:23 2023

@author: iton C.Sangaletti
"""
numero_str = input ('Digite um número inteiro:')
numero = int(numero_str)
dezena = numero % 100
resto_dezena = dezena // 10
print('O dígito das dezenas é',resto_dezena)
