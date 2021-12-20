#Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
#Найдите сумму всех простых чисел меньше двух миллионов.

n=2*10**6
num = list(range(2,n+1))
for i in num:
    if i != 0:
        for k in range(2*i,n+1,i): # с шагом i убираем все числа
            num[k-2] =0 
print('Сумма равна',sum(list(filter(lambda x: x !=0,num))))

#аверное, уже неакутально, но все же отвечу на ваш вопрос. 
#рограмма, начиная с числа i*2 включительно заменяет все числа на 0, 
#с шагом i. Так, как число, с которого мы берем перебор, равносильно нашему шагу, 
#то мы простыми движениями убираем все числа, кратные i. Простые числа не кратны ничему, 
#кроме 1, поэтому они не заменятся на 0. (Например, начинаем с 2, удаляем 4 6 8 и тд. 
#    Начинаем с 3 и удаляем 6 9 12, начинаем с 5 и удаляем 10 15 20...). Сам сначала запутался, 
#умая, что i - это индекс числа в списке, но нет, i - это и есть число в списке, где 
#мы начнем с 2.