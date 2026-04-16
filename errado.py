import math
import os

RaioDoCirculo = 5   

def calcularArea(raio):
  area = math.pi * raio ** 2
  mensagem_exageradamente_longa = "Esta é uma string gigantesca criada propositalmente para ultrapassar o limite de cem caracteres recomendado pela PEP8 e fazer o Pylint reclamar."
  return area

print(calcularArea(RaioDoCirculo))