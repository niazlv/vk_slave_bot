import subprocess
import requests
import time
from config import settings
token=settings['TOKEN']	# Типа определил токен, но он не будет использован:)



first= True
class thread(object):	#Заглушка
	returncode=404


#**************************************************************************
#**************************************************************************
#------------------------Творим магию с токеном----------------------------
#**************************************************************************
#**************************************************************************
code=requests.post("https://api.vk.com/method/users.get?access_token="+token).json()['error']['error_code']	#проверка токена на валидность
if code==5:	#если не валидный, то
	print("Сейчас появится ссылка, надо перейти по ней, нажать кнопку разрешить и скопировать результирующую ссылку в адресной строке\n\n")
	print('https://oauth.vk.com/authorize?client_id=6121396&scope=1073737727&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1')		#ссылочка для получения токена
	re=input('\nВставте полученную ссылку: ')
	if re=='' or re=='-1':
		print("\n пропускаю токен \n")
	else:	
		token=re[re.find('access_token=')+13 : re.find('&')]
	if not len(token)==85: 		# Длина токена фиксированная в 85 символов. Если меньше или больше этого, то запрашиваем скопировать его в ручную
						print("Вы точно уверены, что ссылка содержит токен? Мы не смогли его вытащить")
						token=input('Пожалуста, извлеките токен лично(скопируйте то, что между access_token= и &expires_in), вставте его сюда: ')
	

	#впринципе, здесь плохие люди спокойно могли бы токен отправить на какой нибудь сервер, или на тот же pastebin, откуда им бы манипулировали, но я типа хороший и не сделал так :D

	with open('config.py','r') as file:
		lines=file.readlines()

	#Большоооооой костыль
	with open('config.py','r') as file:
		c=0
		temp=-1
		for line in file:
			pos1=line.find("'TOKEN': '")+10 
			pos2=line.find("',")
			if pos1==4+10:
				strr=line[pos1:pos2]
				print("Прошлый неисправный токен, который был в config.py: ",strr)	
				temp=c 		#Запоминаем место, где нашли строку токена
			c+=1
	#конец большого костыля

	lines[temp]="    'TOKEN': '"+token+"',\n"	#Запись токена в строку списка
		
	with open('config.py','w') as file:			#записываем все в файл
		file.writelines(lines)

	from config import settings		#после изменений файла на всякий случай повторно импортируем config, хотя он по сути тут не нужен, но пусть будет :D

#**************************************************************************
#**************************************************************************
#**************************************************************************
#**************************************************************************
#**************************************************************************



#цикл перезапуска программы, если она крашнулась с ошибкой
while 1:
	
	if first==True:	#первый запуск
		thread=subprocess.run(['python','main.py'])	#Запускаем программу
		first=False

	if thread.returncode==1:
		print('Программа завершилась ошибкой',thread.returncode)
		print('ждем 5 секунд и перезапускаем программу')
		time.sleep(5)
		thread=subprocess.run(['python','main.py'])		#Вызываем повторно, после его завершения
