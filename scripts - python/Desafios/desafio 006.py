#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
n = int(input('Digte um número: '))
d = n*2
t = n*3
rq = float(pow(n,1/2)) #raiz quadrada pode ser o número elevado a ele msm divido por 1/2 (** - tbm calcula potencia)
print('O dobro de {} é {} \nO seu triplo é {} \nA sua raiz quadrada é {}'.format(n,d,t,rq))