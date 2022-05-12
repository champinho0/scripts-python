#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = float(input('Digite um ângulo qualquer: '))
sen = math.sin(math.radians(ang)) #por padrão o parametro é graus centigridos, por isso temos que converter para radiano
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('Para o ângulo {:.2f} temos \nSeno {:.2f} \nCosseno {:.2f} \nTangante {:.2f}'.format(ang,sen,cos,tang))
