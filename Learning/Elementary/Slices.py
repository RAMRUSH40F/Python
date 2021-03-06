#Работа со списками и строками
shoplist = ['грибы','апельсины','груши','яблоки']
print('С 1 по 3 ',shoplist[1:3])
print('С 1 до конца',shoplist[1:])
print('Весь список', shoplist[:])
print('Третий элемент с конца - ',shoplist[-3])
print('Берем каждый третий элемент(увеличиваем шаг):', shoplist[::3])

#Строки - объекты класса str #Строки - это, например, aaa = 'Кричит от боли!'
help(str)
name = 'Swaroop' # Это объект строки
if name.startswith('Swa'): 
	print('Да, строка начинается на "Swa"')
if 'a' in name:
	print('Да, она содержит строку "a"')
if name.find('war') != -1:
	print('Да, она содержит строку "war"')

delimiter = '_*_'
mylist = ['Бразилия', 'Россия', 'Индия', 'Китай']
print(delimiter.join(mylist))

#Кортеж (нельзя изменять)
zoo = ('питон','лев','обезьяна')
print('Количество животных в старом зоопарке -', len(zoo))
print( 'Это - ', zoo)

new_zoo = 'антилопа', 'зебра', zoo
print('Количество животных в новом зоопарке ', len(new_zoo) -1)  #старый закрывается, их перевозят в новый

print('Перевезем жителей первого зоопарка в новый')
print('Старые жители второго зоопарка:', new_zoo[0],new_zoo[1], end= ',')  
#индексирование - обращение к элементам кортежа через квадратные скобки
print('Привезенные жители:', zoo)									#!!! доступ к элементам кортежа внутри кортежа через две кобки [][]
print('Количество животных в новом зоопарке -', len(new_zoo)-1 + \
len(new_zoo[2]))

# МНОЖЕСТВА
bri = set(['Решка','Решка','Орёл'])
print('Орёл' in bri)

bri2 = bri.copy()
bri2.add('Грань')
print('Является ли bri2 одмножеством bri?',bri2.issuperset(bri))



#НЕОЧЕВИДНЫЕ ВЕЩИ ПРО ПЕРЕМЕННЫЕ
	'''Они ссылаются на объекты, поэтому:
	'''
shoplist = [1,2,3,4,5,6] # Создаем ссылку на объект(список)
mylist = shoplist # Теперь mylist тоже ссылается на объект
#Если удалить из mylist объект, он удалится и из shoplist

#Как копировать множества: - Через вырезку
mylist = shoplist[:]