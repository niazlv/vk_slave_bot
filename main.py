import time
import requests
import random

from slaves_lib import Slaves
from config import settings

token = settings['TOKEN']
local_id = int(requests.post("https://api.vk.com/method/users.get?v=5.130&access_token="+token).json()['response'][0]['id'])
steal = settings['STEAL']
targets = settings['TARGETS']
price = settings['MAX_PRICE']

client = Slaves(token)

jobs = ['Гном', 'лом', 'лол', ')', 'Дилер', 'Хайдарщик', 'Трейдер', 'Инвестор', 'Молодчина', 'Халявщик', 'IT', '.', 'хе', 'не повезло', 'спидранер','кто-то там','ХЫЫЫЫЫЫ','ъеъ','Это бот','Это не бот', 'slave','Дурачек(нет)','хто це','s','ркагц','h','лп','dg','г',')','(','&&&',"'error_steal':'5'",'t']


def update_slave_to_1000(id):
    res=client.user(id)
    while res['price']<27000:
        print(res['price'])
        client.sale_slave(idz)
        time.sleep(1+random.random()+random.random()+random.random())
        client.buy_slave(idz)
        time.sleep(random.random()+random.random()+random.random())
        res=client.user(id)
        pass

def autobuyBots(idz, autoUpdate=False):
    print(idz)
    time.sleep(random.random())
    try:
        res=client.buy_slave(idz)
    except Exception as e:
        print(e)

    time.sleep(random.random()+random.random()+random.random())
    if autoUpdate:
        update_slave_to_1000(idz)
    client.buy_fetter(idz)
    time.sleep(random.random()+random.random()+random.random())
    client.job_slave(idz, jobs[int(random.random()*len(jobs))])
    print(f'Fettered')

if __name__ == '__main__':
    # start
    client.start()
    idz=int((random.random()*6700000)+1)    #случайный id среди всех пользователей ВКонтакте!

    f=0
    runs=True
    while True:
        runs=True
        res=client.user(idz)    #Запрос информации о рабе
        #print(res)
        if(res['fetter_to']==0 and res['sale_price']<=40000):


            try:
                print(res['error'])
                if res['error']['code']==422:
                    print("opps, timing ",idz)
                    runs=False
            except KeyError as e:
                pass
            if runs:
                autobuyBots(idz,True)   #Если вторым параметром вписать True, то бдует производиться закупка и прокачка рабов до прибыльности 1к в минуту

                idz+=1
        else:
            f+=1

            if(f>=10):  # если более 10 пустых итераций(т.е раб в оковах или стоит более 40 000рублей, то мы меняем idz)
                f=0
                idz=int((random.random()*6700000)+1)
                
                
        try:
            if steal:   #Внимание!!! бот скупает всех рабов. Это было сделано для меня. Мне все равно на баланс. Так что это требует доработки, добавления 1-2 условий
                for j in range (len(targets)):
                    user_info=client.user(targets[j])
                    time.sleep(random.random()*2)
                    rez=client.slave_list(targets[j])
                    time.sleep(random.random()*3)
                    for i in range(user_info['slaves_count']):
                        if(rez['slaves'][i]['fetter_to']==0):
                            try:
                                client.buy_slave(rez['slaves'][i]['id'])
                            except Exception as e:
                                raise
                            time.sleep(random.random()*3)   #Случайные тайминги для обхода автобана
                            client.buy_fetter(rez['slaves'][i]['id'])                       #Покупаем оковы
                            time.sleep(random.random()*3)   #Случайные тайминги для обхода автобана 
                            client.job_slave(rez['slaves'][i]['id'], jobs[int(random.random()*len(jobs))])  #Даём работу
                            time.sleep(random.random()*3)
                            print(i,"tic")  #индикация о том, что 1 итерация совершена.
        except Exception as e:
            print("opps, except: ",e)
            # \n
        print('')

        
        # тихий час
        time.sleep(random.random()*5)
