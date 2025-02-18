import random
import time

list = ['PEDRA', 'PAPEL', 'TESOURA']

computador = random.choice(list)

escolha = str(input('Digite Pedra, Papel ou Tesoura: ')).upper().strip()
print('\033[1:37mJOKENPO...\033[m')
time.sleep(1)

if escolha == 'PEDRA' and computador == 'PEDRA':
    print(f'\033[1:34mEMPATOU!! \033[m\033[1:33mVocê -> {escolha}\033[m x \033[1:35mComputador -> {computador}\033[m')
elif escolha == 'PAPEL' and computador == 'PAPEL':
    print(f'\033[1:34mEMPATOU!! \033[m\033[1:33mVocê -> {escolha}\033[m x \033[1:35mComputador -> {computador}\033[m')
elif escolha == 'TESOURA' and computador == 'TESOURA':
    print(f'\033[1:34mEMPATOU!! \033[m\033[1:33mVocê -> {escolha}\033[m x \033[1:35mComputador -> {computador}\033[m')
elif escolha == 'PEDRA' and computador == 'PAPEL':
    print(f'\033[1:31mPERDEU!!! \033[m\033[1:33mVocê -> {escolha}\033[m x \033[1:35mComputador -> {computador}\033[m')
elif escolha == 'TESOURA' and computador == 'PEDRA':
    print(f'\033[1:31mPERDEU!!! \033[m\033[1:33mVocê -> {escolha}\033[m x \033[1:35mComputador -> {computador}\033[m')
elif escolha == 'PAPEL' and computador == 'TESOURA':
    print(f'\033[1:31mPERDEU!!! \033[m\033[1:33mVocê -> {escolha}\033[m x \033[1:35mComputador -> {computador}\033[m')
elif escolha == 'PEDRA' and computador == 'TESOURA':
    print(f'\033[1:36mGANHOU!!! \033[m\033[1:33mVocê -> {escolha}\033[m x \033[1:35mComputador -> {computador}\033[m')
elif escolha == 'PAPEL' and computador == 'PEDRA':
    print(f'\033[1:36mGANHOU!!! \033[m\033[1:33mVocê -> {escolha}\033[m x \033[1:35mComputador -> {computador}\033[m')
elif escolha == 'TESOURA' and computador == 'PAPEL':
    print(f'\033[1:36mGANHOU!!! \033[m\033[1:33mVocê -> {escolha}\033[m x \033[1:35mComputador -> {computador}\033[m')
