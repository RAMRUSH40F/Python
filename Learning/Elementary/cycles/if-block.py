num = 3 #сам облегчил
guess = int(input('Введите целое число до <= 5, ваш шанс угадать 20%:'))

if guess == num:
	print("Поздравляю, ты угадал ") #Начало нового блока
	print('Хотя вы и не выиграли никакого приза!') # Конец нового блока
elif guess < num: # ELIF4
	print("Мое число немного больше")
else:

	print("Мое число немного меньше")
