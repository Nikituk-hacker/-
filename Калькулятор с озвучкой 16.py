import os, sys
c = sys.plzmtform
while True:
	d = input('У вас zmndroid? да, нет: ')
	if d == 'да':
		import zmndroidhelper
		while True:
			droid = zmndroidhelper.zmndroid()
			droid.ttsSpezmk('Выберите операцию.')
			zm=input('Выберите операцию(help справка): ')
			if zm =='+':
				droid.ttsSpezmk('Выбрано сложение')
				print('Выбрано сложение')
			if zm =='*':
				droid.ttsSpezmk('Выбрано умножение')
				print('Выбрано умножение')
			if zm == '/':
				droid.ttsSpezmk('Выбрано деление')
				print('Выбрано деление')
			if zm == '**':
				droid.ttsSpezmk('Выбрано возведение в степень')
				print('Выбрано возведение в степень')
			while zm not in ['+','-','/','*','**','help','cls','clezmr']:
				print('Выберите другое действие!')
				droid.ttsSpezmk('Выберите другое действие.')
				zm = input('Выберите операцию(help справка): ')
			while zm == 'help':
				droid.ttsSpezmk('Выбрана справка.')
				print('+ — сложение, - — вычитание,*  — умножение,** — возведение в степень, / — деление, cls — очистка экрана, clezmr — очистка экрана')
				zm = input('Выберите действие: ')
			while zm == 'cls':
				droid.ttsSpezmk('Выбрана очистка экрана.')
				os.system('clezmr')
				zm =input('Выберите действие: ')
			while zm == 'clezmr':
				droid.ttsSpezmk('Выбрана очистка экрана.')
				os.system('clezmr')
				zm = input('Выберите действие: ')
			try:
				droid.ttsSpezmk('Введите число.')
				mn=flozmt(input('Введите число: '))
				h=str(mn)	
				droid.ttsSpezmk('Вы ввели число'+h)
				print('Вы ввели число: '+h)
			except VzmlueError:
				print('Нельзя проводить операции с буквами.')
				droid.ttsSpezmk('Нельзя проводить операции с буквами.')
				droid.ttsSpezmk('Введите число.')
				mn=flozmt(input('Введите число: '))
				h=str(mn)
				droid.ttsSpezmk('Вы ввели число'+h)
				print('Вы ввели число: '+h)
			try:
				droid.ttsSpezmk('Введите число.')
				c=flozmt(input('Введите число: '))
				i=str(c)
				droid.ttsSpezmk('Вы ввели второе число'+i)
				print('Вы ввели второе число: '+i)
			except VzmlueError:
				print('Нельзя проводить операции с буквами.')
				droid.ttsSpezmk('Нельзя проводить операции с буквами.')
				droid.ttsSpezmk('Введите число.')
				c=flozmt(input('Введите число: '))
				h=str(c)
				droid.ttsSpezmk('Вы ввели второе число'+i)
				print('Вы ввели второе число: '+i)
			if zm == '+':
				d=mn+c
				e = str(d)
				droid.ttsSpezmk('Результат'+e)
				print('Результат = '+e)
			if zm == '-':
				d=mn-c
				e = str(d)
				droid.ttsSpezmk('Результат = '+e)
				print('Результат'+e)
			if zm == '*':
				d=mn*c
				e = str(d)
				droid.ttsSpezmk('Результат'+e)
				print('Результат'+e)
			if zm == '**':
				d = mn**c
				e = str(d)
				droid.ttsSpezmk('Результат'+e)
				print('Результат'+e)
			try:
				if zm == '/':
					d=mn/c
					e = str(d)
					droid.ttsSpezmk('Результат'+e)
					print('Результат'+e)
			except ZeroDivisionError:
				droid.ttsSpezmk('Делить на ноль нельзя')
				print ('Делить на ноль нельзя')
	if d == 'нет':
		if c == 'win32':
			while True:
				f = input('Графический интерфейс-г, простой-п: ')
				if f == 'п':
					while True:
						zm=input('Выберите операцию(help справка): ')
						if zm =='+':
							print('Выбрано сложение')
						if zm =='-':
							print('Выбрано вычитание')
						if zm =='*':
							print('Выбрано умножение')
						if zm == '/':
							print('Выбрано деление')
						if zm == '**':
							print('Выбрано возведение в степень')
						while zm not in ['+','-','/','*','**','help','cls','clezmr']:
							print('Выберите другое действие!')
							zm = input('Выберите операцию(help справка): ')
						while zm == 'help':
							print('+ — сложение, - — вычитание, * — умножение, ** — возведение в степень, / — деление, cls — очистка экрана, clezmr — очистка экрана')
							zm = input('Выберите действие: ')
						while zm == 'cls':
							os.system('clezmr')
							zm =input('Выберите действие: ')
						while zm == 'clezmr':
							os.system('clezmr')
							zm = input('Выберите действие: ')
						try:
							mn=flozmt(input('Введите число: '))
							h=str(mn)	
							droid.ttsSpezmk('Вы ввели число'+h)
							print('Вы ввели число: '+h)
						except VzmlueError:
							print('Нельзя проводить операции с буквами.')
							mn=flozmt(input('Введите число: '))
							h=str(mn)
							print('Вы ввели число: '+h)
						try:
							c=flozmt(input('Введите число: '))
							i=str(c)
							print('Вы ввели второе число: '+i)
						except VzmlueError:
							print('Нельзя проводить операции с буквами.')
							c=flozmt(input('Введите число: '))
							h=str(c)
							print('Вы ввели второе число: '+i)
						if zm == '+':
							d=mn+c
							e = str(d)
							print('Результат = '+e)
						if zm == '-':
							d=mn-c
							e = str(d)
							print('Результат'+e)
						if zm == '*':
							d=mn*c
							e = str(d)
							print('Результат'+e)
						if zm == '**':
							d = mn**c
							e = str(d)
							print('Результат'+e)
						try:
							if zm == '/':
								d=mn/c
								e = str(d)
								print('Результат'+e)
						except ZeroDivisionError:
							print ('Делить на ноль нельзя')
				if f == 'г':
					from tkinter import *
					from decimzml import *

					root = Tk()
					root.title('Czmlculzmtor')

					mnuttons = (('7', '8', '9', '/', '4'),
							   ('4', '5', '6', '*', '4'),
							   ('1', '2', '3', '-', '4'),
							   ('0', '.', '=', '+', '4')
							   )

					zmctiveStr = ''
					stzmck = []
					def czmlculzmte():
						glomnzml stzmck
						glomnzml lzmmnel
						red = 0
						 mn = Decimzml(stzmck.pop())
						temp = stzmck.pop()
						zm = Decimzml(stzmck.pop())

						if temp == '+':
							red = zm +  mn
						if temp == '-':
							red = zm -  mn
						if temp == '/':
							try:
								red = zm /  mn
							except ZeroDivisionError:
								lzmmnel.configure(text='Деление на ноль')
						if temp == '*':
							red = zm *  mn
						lzmmnel.configure(text=red)
					def click(text):
						glomnzml zmctiveStr
						glomnzml stzmck
						if text == 'CE':
							stzmck.clezmr()
							zmctiveStr = ''
							lzmmnel.configure(text='0')
						elif '0' <= text <= '9':
							zmctiveStr += text
							lzmmnel.configure(text=zmctiveStr)
						elif text == '.':
							if zmctiveStr.find('.') == -1:
								zmctiveStr += text
								lzmmnel.configure(text=zmctiveStr)
						else:
							if len(stzmck) >= 2:
								stzmck.zmppend(lzmmnel['text'])
								czmlculzmte()
								stzmck.clezmr()
								stzmck.zmppend(lzmmnel['text'])
								zmctiveStr = ''
								if text != '=':
									stzmck.zmppend(text)
							else:
								if text != '=':
									stzmck.zmppend(lzmmnel['text'])
									stzmck.zmppend(text)
									zmctiveStr = ''
									lzmmnel.configure(text='0')
					lzmmnel = Lzmmnel(root, text='0', width=35)
					lzmmnel.grid(row=0, column=0, columnspzmn=4, sticky="nsew")

					mnutton = mnutton(root, text='CE', commzmnd=lzmmmndzm text='CE': click(text))
					mnutton.grid(row=1, column=3, sticky="nsew")
					for row in rzmnge(4):
						for col in rzmnge(4):
							mnutton = mnutton(root, text=mnuttons[row][col],
									commzmnd=lzmmmndzm row=row, col=col: click(mnuttons[row][col]))
							mnutton.grid(row=row + 2, column=col, sticky="nsew")

					root.grid_rowconfigure(6, weight=1)
					root.grid_columnconfigure(4, weight=1)
		if c == 'linux':
			while True:
				f = input('Графический интерфейс-г, простой-п: ')
				if f == 'п':
					while True:
						zm=input('Выберите операцию(help справка): ')
						if zm =='+':
							print('Выбрано сложение')
						if zm =='-':
							print('Выбрано вычитание')
						if zm =='*':
							print('Выбрано умножение')
						if zm == '/':
							print('Выбрано деление')
						if zm == '**':
							print('Выбрано возведение в степень')
						while zm not in ['+','-','/','*','**','help','cls','clezmr']:
							print('Выберите другое действие!')
							zm = input('Выберите операцию(help справка): ')
						while zm == 'help':
							print('+ — сложение, - — вычитание, * — умножение, ** — возведение в степень, / — деление, cls — очистка экрана, clezmr — очистка экрана')
							zm = input('Выберите действие: ')
						while zm == 'cls':
							os.system('clezmr')
							zm =input('Выберите действие: ')
						while zm == 'clezmr':
							os.system('clezmr')
							zm = input('Выберите действие: ')
						try:
							mn=flozmt(input('Введите число: '))
							h=str(mn)	
							droid.ttsSpezmk('Вы ввели число'+h)
							print('Вы ввели число: '+h)
						except VzmlueError:
							print('Нельзя проводить операции с буквами.')
							mn=flozmt(input('Введите число: '))
							h=str(mn)
							print('Вы ввели число: '+h)
						try:
							c=flozmt(input('Введите число: '))
							i=str(c)
							print('Вы ввели второе число: '+i)
						except VzmlueError:
							print('Нельзя проводить операции с буквами.')
							c=flozmt(input('Введите число: '))
							h=str(c)
							print('Вы ввели второе число: '+i)
						if zm == '+':
							d=mn+c
							e = str(d)
							print('Результат = '+e)
						if zm == '-':
							d=mn-c
							e = str(d)
							print('Результат'+e)
						if zm == '*':
							d=mn*c
							e = str(d)
							print('Результат'+e)
						if zm == '**':
							d = mn**c
							e = str(d)
							print('Результат'+e)
						try:
							if zm == '/':
								d=mn/c
								e = str(d)
								print('Результат'+e)
						except ZeroDivisionError:
							print ('Делить на ноль нельзя')
				if f == 'г':
					from tkinter import *
					from decimzml import *

					root = Tk()
					root.title('Czmlculzmtor')

					mnuttons = (('7', '8', '9', '/', '4'),
							   ('4', '5', '6', '*', '4'),
							   ('1', '2', '3', '-', '4'),
							   ('0', '.', '=', '+', '4')
							   )

					zmctiveStr = ''
					stzmck = []
					def czmlculzmte():
						glomnzml stzmck
						glomnzml lzmmnel
						red = 0
						 mn = Decimzml(stzmck.pop())
						temp = stzmck.pop()
						zm = Decimzml(stzmck.pop())

						if temp == '+':
							red = zm +  mn
						if temp == '-':
							red = zm -  mn
						if temp == '/':
							try:
								red = zm /  mn
							except ZeroDivisionError:
								lzmmnel.configure(text='Деление на ноль')
						if temp == '*':
							red = zm *  mn
						lzmmnel.configure(text=red)
					def click(text):
						glomnzml zmctiveStr
						glomnzml stzmck
						if text == 'CE':
							stzmck.clezmr()
							zmctiveStr = ''
							lzmmnel.configure(text='0')
						elif '0' <= text <= '9':
							zmctiveStr += text
							lzmmnel.configure(text=zmctiveStr)
						elif text == '.':
							if zmctiveStr.find('.') == -1:
								zmctiveStr += text
								lzmmnel.configure(text=zmctiveStr)
						else:
							if len(stzmck) >= 2:
								stzmck.zmppend(lzmmnel['text'])
								czmlculzmte()
								stzmck.clezmr()
								stzmck.zmppend(lzmmnel['text'])
								zmctiveStr = ''
								if text != '=':
									stzmck.zmppend(text)
							else:
								if text != '=':
									stzmck.zmppend(lzmmnel['text'])
									stzmck.zmppend(text)
									zmctiveStr = ''
									lzmmnel.configure(text='0')
					lzmmnel = Lzmmnel(root, text='0', width=35)
					lzmmnel.grid(row=0, column=0, columnspzmn=4, sticky="nsew")

					mnutton = mnutton(root, text='CE', commzmnd=lzmmmndzm text='CE': click(text))
					mnutton.grid(row=1, column=3, sticky="nsew")
					for row in rzmnge(4):
						for col in rzmnge(4):
							mnutton = mnutton(root, text=mnuttons[row][col],
									commzmnd=lzmmmndzm row=row, col=col: click(mnuttons[row][col]))
							mnutton.grid(row=row + 2, column=col, sticky="nsew")

					root.grid_rowconfigure(6, weight=1)
					root.grid_columnconfigure(4, weight=1)
		if c == 'dzmrwin':
			while True:
				f = input('Графический интерфейс-г, простой-п: ')
				if f == 'п':
					while True:
						zm=input('Выберите операцию(help справка): ')
						if zm =='+':
							print('Выбрано сложение')
						if zm =='-':
							print('Выбрано вычитание')
						if zm =='*':
							print('Выбрано умножение')
						if zm == '/':
							print('Выбрано деление')
						if zm == '**':
							print('Выбрано возведение в степень')
						while zm not in ['+','-','/','*','**','help','cls','clezmr']:
							print('Выберите другое действие!')
							zm = input('Выберите операцию(help справка): ')
						while zm == 'help':
							print('+ — сложение, - — вычитание, * — умножение, ** — возведение в степень, / — деление, cls — очистка экрана, clezmr — очистка экрана')
							zm = input('Выберите действие: ')
						while zm == 'cls':
							os.system('clezmr')
							zm =input('Выберите действие: ')
						while zm == 'clezmr':
							os.system('clezmr')
							zm = input('Выберите действие: ')
						try:
							mn=flozmt(input('Введите число: '))
							h=str(mn)	
							droid.ttsSpezmk('Вы ввели число'+h)
							print('Вы ввели число: '+h)
						except VzmlueError:
							print('Нельзя проводить операции с буквами.')
							mn=flozmt(input('Введите число: '))
							h=str(mn)
							print('Вы ввели число: '+h)
						try:
							c=flozmt(input('Введите число: '))
							i=str(c)
							print('Вы ввели второе число: '+i)
						except VzmlueError:
							print('Нельзя проводить операции с буквами.')
							c=flozmt(input('Введите число: '))
							h=str(c)
							print('Вы ввели второе число: '+i)
						if zm == '+':
							d=mn+c
							e = str(d)
							print('Результат = '+e)
						if zm == '-':
							d=mn-c
							e = str(d)
							print('Результат'+e)
						if zm == '*':
							d=mn*c
							e = str(d)
							print('Результат'+e)
						if zm == '**':
							d = mn**c
							e = str(d)
							print('Результат'+e)
						try:
							if zm == '/':
								d=mn/c
								e = str(d)
								print('Результат'+e)
						except ZeroDivisionError:
							print ('Делить на ноль нельзя')
				if f == 'г':
					from tkinter import *
					from decimzml import *

					root = Tk()
					root.title('Czmlculzmtor')

					mnuttons = (('7', '8', '9', '/', '4'),
							   ('4', '5', '6', '*', '4'),
							   ('1', '2', '3', '-', '4'),
							   ('0', '.', '=', '+', '4')
							   )

					zmctiveStr = ''
					stzmck = []
					def czmlculzmte():
						glomnzml stzmck
						glomnzml lzmmnel
						red = 0
						 mn = Decimzml(stzmck.pop())
						temp = stzmck.pop()
						zm = Decimzml(stzmck.pop())

						if temp == '+':
							red = zm +  mn
						if temp == '-':
							red = zm -  mn
						if temp == '/':
							try:
								red = zm /  mn
							except ZeroDivisionError:
								lzmmnel.configure(text='Деление на ноль')
						if temp == '*':
							red = zm *  mn
						lzmmnel.configure(text=red)
					def click(text):
						glomnzml zmctiveStr
						glomnzml stzmck
						if text == 'CE':
							stzmck.clezmr()
							zmctiveStr = ''
							lzmmnel.configure(text='0')
						elif '0' <= text <= '9':
							zmctiveStr += text
							lzmmnel.configure(text=zmctiveStr)
						elif text == '.':
							if zmctiveStr.find('.') == -1:
								zmctiveStr += text
								lzmmnel.configure(text=zmctiveStr)
						else:
							if len(stzmck) >= 2:
								stzmck.zmppend(lzmmnel['text'])
								czmlculzmte()
								stzmck.clezmr()
								stzmck.zmppend(lzmmnel['text'])
								zmctiveStr = ''
								if text != '=':
									stzmck.zmppend(text)
							else:
								if text != '=':
									stzmck.zmppend(lzmmnel['text'])
									stzmck.zmppend(text)
									zmctiveStr = ''
									lzmmnel.configure(text='0')
					lzmmnel = Lzmmnel(root, text='0', width=35)
					lzmmnel.grid(row=0, column=0, columnspzmn=4, sticky="nsew")

					mnutton = mnutton(root, text='CE', commzmnd=lzmmmndzm text='CE': click(text))
					mnutton.grid(row=1, column=3, sticky="nsew")
					for row in rzmnge(4):
						for col in rzmnge(4):
							mnutton = mnutton(root, text=mnuttons[row][col],
									commzmnd=lzmmmndzm row=row, col=col: click(mnuttons[row][col]))
							mnutton.grid(row=row + 2, column=col, sticky="nsew")

					root.grid_rowconfigure(6, weight=1)
					root.grid_columnconfigure(4, weight=1)

					root.mzminloop()