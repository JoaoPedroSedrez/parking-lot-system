import random
import numpy as np

# Initialize the parking sectors
setores = np.array(['' for _ in range(16)], dtype=object)

# Function to enter the parking lot
def entrarNoEstacionamento():
    placaDoCarro = input('Enter your car license plate: ')
    if verificar_placa(placaDoCarro):
        posicao = np.where(setores == placaDoCarro)[0][0]
        print(f'You are already in the parking lot! Your spot is {posicao}.')
        sair = input('Do you want to leave? [s/n]: ')
        if sair == 's':
            setores[posicao] = ''
            print(f'The vehicle with license plate {placaDoCarro} has left the parking lot.')
        else:
            print(f'OK! Your spot remains {posicao}')
    else:
        try:
            vagas_vazias = np.where(setores == '')[0]
            arrVagasVazias = np.array(vagas_vazias)

            if len(arrVagasVazias) > 0:
                vaga_escolhida = np.random.choice(arrVagasVazias)
                setor = ''
                if vaga_escolhida <= 4:
                    setor = 'A'
                elif vaga_escolhida <= 9:
                    setor = 'B'
                elif vaga_escolhida <= 14:
                    setor = 'C'
                print(f'The chosen spot is {vaga_escolhida}{setor}')
                setores[vaga_escolhida] = placaDoCarro
                print(f'Vehicle with license plate {placaDoCarro} parked in spot {vaga_escolhida}{setor}.')
                print(setores)
            else:
                raise Exception('Parking Lot Full')
        except Exception as e:
            print(f'Unfortunately, the parking lot is full! {e}')

# Function to check if the license plate is already in the parking lot
def verificar_placa(placa):
    return np.any(setores == placa)

# Function to leave the parking lot
def sairDoEstacionamento():
    placaDoCarro = input('Enter your car license plate: ')
    if verificar_placa(placaDoCarro):
        posicao = np.where(setores == placaDoCarro)[0][0]
        setores[posicao] = ''
        print(f'The vehicle with license plate {placaDoCarro} has left spot {posicao}.')
    else:
        print(f'The vehicle with license plate {placaDoCarro} is not in the parking lot.')

# Function to check available spots
def verificarVagas():
    vagas_vazias = np.where(setores == '')[0]
    if len(vagas_vazias) > 0:
        print(f'Available spots: {vagas_vazias}')
    else:
        print('There are no available spots.')

# Function to check if a vehicle is in the parking lot
def verificarVeiculo():
    placaDoCarro = input('Enter the license plate of the vehicle you want to check: ')
    if verificar_placa(placaDoCarro):
        posicao = np.where(setores == placaDoCarro)[0][0]
        print(f'The vehicle with license plate {placaDoCarro} is in spot {posicao}.')
    else:
        print(f'The vehicle with license plate {placaDoCarro} is not in the parking lot.')

# Main function that offers options to the user
def iniciar():
    while True:
        escolha = input('\n\n\nWhat would you like to do?\n1. Enter the parking lot\n2. Leave the parking lot\n3. Check available spots\n4. Check vehicle\n0. Exit\nChoose: ')
        if escolha == '1':
            entrarNoEstacionamento()
        elif escolha == '2':
            sairDoEstacionamento()
        elif escolha == '3':
            verificarVagas()
        elif escolha == '4':
            verificarVeiculo()
        elif escolha == '0':
            print('Exiting the program.')
            break
        else:
            print('Choose a valid option.')

# Start the program
iniciar()
