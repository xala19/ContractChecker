import requests
import json
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/c47443a98e05433f9ddc98f20701c341'))
apiEth = '2AMSM6WUU5HUGRJK8VWIKYUYM9CI25AM48'
apiPolygon = '83QXGMNPSB74DSHTGFUQZX1TFKX22AMB42'
apiBsc = 'R8V9CCAGNTFJ45CNSGITEWWJUUPDUWDF4S'
apiOpti = '7BNRJ5GCKFT4KY7Q5GUB2GHJ9H4KZ3G5KF'
apiArbi = 'C3Y1Y9J51ISTRKIVY7S39X111MP4766BA1'
counter = 0


def check_wallet_contract_interaction_ether(wallet_address, contract_address):
    global counter
    
    
    response = requests.get(f'https://api.etherscan.io/api?module=account&action=txlist&address={wallet_address}&sort=desc&apikey={apiEth}')
    data = json.loads(response.text)
    
    
    for tx in data['result']:
       
        
        if (tx['to']) == contract_address:
            counter += 1
    
    if counter > 0:
        with open('result.txt','a') as file:
            file.write(f'{wallet_address};{counter}' + "\n")
    else:
        with open('result.txt','a') as file:
            file.write(f'{wallet_address};{counter}' + "\n")
    
    counter = 0


def check_wallet_contract_interaction_polygon(wallet_address, contract_address):
    global counter
    response = requests.get(f'https://api.polygonscan.com/api?module=account&action=txlist&address={wallet_address}&sort=desc&apikey={apiPolygon}')
    data = json.loads(response.text)
    for tx in data['result']:

        if tx['to'] == contract_address:
            counter += 1

    if counter > 0:
        with open('result.txt','a') as file:
            file.write(f'{wallet_address};{counter}' + "\n")

    else:
        with open('result.txt','a') as file:
            file.write(f'{wallet_address};{counter}' + "\n")
    counter = 0

def check_wallet_contract_interaction_bsc(wallet_address, contract_address):
    global counter
    response = requests.get(f'https://api.bscscan.com/api?module=account&action=txlist&address={wallet_address}&sort=desc&apikey={apiBsc}')
    data = json.loads(response.text)
    for tx in data['result']:

        if tx['to'] == contract_address:
            counter += 1

    if counter > 0:
        with open('result.txt','a') as file:
            file.write(f'{wallet_address};{counter}' + "\n")

    else:
        with open('result.txt','a') as file:
            file.write(f'{wallet_address};{counter}' + "\n")
    counter = 0

def check_wallet_contract_interaction_Optimism(wallet_address, contract_address):
        global counter
        response = requests.get(f'https://api-optimistic.etherscan.io/api?module=account&action=txlist&address={wallet_address}&sort=desc&apikey={apiOpti}')
        data = json.loads(response.text)
        for tx in data['result']:

            if tx['to'] == contract_address:
                counter += 1

        if counter > 0:
            with open('result.txt','a') as file:
                file.write(f'{wallet_address};{counter}' + "\n")

        else:
            with open('result.txt','a') as file:
                file.write(f'{wallet_address};{counter}' + "\n")
        counter = 0

def check_wallet_contract_interaction_Arbi(wallet_address, contract_address):
        global counter
        response = requests.get(f'https://api.arbiscan.io/api?module=account&action=txlist&address={wallet_address}&sort=desc&apikey={apiArbi}')
        data = json.loads(response.text)
        for tx in data['result']:

            if (tx['to']) == contract_address:
                counter += 1

        if counter > 0:
            with open('result.txt','a') as file:
                file.write(f'{wallet_address};{counter} ' + "\n")

        else:
            with open('result.txt','a') as file:
                file.write(f'{wallet_address};{counter}' + "\n")
        counter = 0



    
 

    
def main():
    chose = input('Выберите цифру соответствующую сеть для проверки контракта: Ether - 1\n BSC - 2\n Polygon - 3\n Optimistic - 4\n Arbiscan - 5\n')
    contract_address = input('Введите адресс контракта ').lower()
    if chose == '1':
        with open('wallets.txt', encoding='utf-8') as file:
            wallets = [line.strip() for line in file.readlines()]
            for string in wallets:
                check_wallet_contract_interaction_ether(string,contract_address)
                
                    

    elif chose == '2':
        with open('wallets.txt', encoding='utf-8') as file:
            wallets = [line.strip() for line in file.readlines()]
            for string in wallets:
                try:
                    check_wallet_contract_interaction_bsc(string,contract_address)
                except:
                    print('Ошибка,проверьте правильно ли ввели контракт,сеть либо кошельки')

    elif chose == '3':
        with open('wallets.txt', encoding='utf-8') as file:
            wallets = [line.strip() for line in file.readlines()]
            for string in wallets:
                try:
                 check_wallet_contract_interaction_polygon(string,contract_address)
                except:
                    print('Ошибка,проверьте правильно ли ввели контракт,сеть либо кошельки')
    
    elif chose == '4':
        with open('wallets.txt', encoding='utf-8') as file:
            wallets = [line.strip() for line in file.readlines()]
            for string in wallets:
                try:
                    check_wallet_contract_interaction_Optimism(string,contract_address)
                except:
                    print('Ошибка,проверьте правильно ли ввели контракт,сеть либо кошельки')
    elif chose == '5':
        with open('wallets.txt', encoding='utf-8') as file:
            wallets = [line.strip() for line in file.readlines()]
            for string in wallets:
                try:
                    check_wallet_contract_interaction_Arbi(string,contract_address)
                except:
                    print('Ошибка,проверьте правильно ли ввели контракт,сеть либо кошельки')




if __name__ == '__main__':
    main()


       

            
