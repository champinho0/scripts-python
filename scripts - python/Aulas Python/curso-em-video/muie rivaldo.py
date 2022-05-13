from time import sleep
muie = str(input('\033[1:35:40mDigite um nome para a muie de Rivaldo:\033[m  '))
print('\033[1:36:40m-=-\033[m'*31)
print('\033[1:36:40mEstamos processando perguntas para identificar a mulher perfeita para Kondovaldo, aguarde... \033[m')
print('\033[1:36:40m-=-\033[m'*31)
sleep(2)
print('\033[1:31:40mDigite apenas "sim" ou "não"\033[m')
sleep(1)
bate = str(input('\033[1:33:40mA {} vai bater em Bivaldo?\033[m  '.format(muie))).upper()
sair = str(input('\033[1:33:40mA {} vai proibir Linvaldo de sair com os amigos?\033[m  '.format(muie))).upper()
briga = str(input('\033[1:33:40mA {} vai fazer Rifalfo ficar brigado com a familia?\033[m  '.format(muie))).upper()
aluguel = str(input('\033[1:33:40mA {} vai fazer Zivaldo pagar um aluguel maior que o salário?\033[m  '.format(muie))).upper()
fuga = str(input('\033[1:33:40mA {} vai fazer Crodovaldo mudar de cidade fugindo do agiota?\033[m  '.format(muie))).upper()
if bate and sair and briga and aluguel and fuga == 'SIM':
    print('\033[1:32:40mEncontramos a mulher perfeita para o Senhor Lindovaldo.\033[m  ')
else:
    print('\033[1:31:40mInfelizmente {} não é a mulher perfeita para Gigovaldo\033[m  '.format(muie))