import random

def set_the_value():   # Функція для задання і перевірки значень
    while True:
        try:
            value = input()
            if value == 'exit':
                print('Програма завершила роботу')
                exit()
            else:
                return int(value)
            break
        except ValueError:
            print("НЕ вірні дані! Спробуй ще разочок")

def set_the_number():   # Функція для задання розміру
    print("Введіть кількість елементів у масиві:")
    numbers = set_the_value()
    if numbers <= 0:
        while numbers <= 0:
            print("Масив не може бути меншим або дорівнювати нулю!!! Спробуй ще:")
            numbers = set_the_value()
    return numbers

def create_an_array():   # Функція для створення масиву
    numbers = set_the_number()
    arr = []
    for i in range(numbers):
        print("Введіь елемент масиву " + str(i + 1) + ":")
        element = set_the_value()
        arr.append(element)
    return arr

def create_an_random_array():   # Функція для створення рандомного масиву
    numbers = set_the_number()
    arr = []
    print("Введіь елемент a:")
    a = set_the_value()
    print("Введіь елемент b:")
    b = set_the_value()
    for i in range(numbers):
        if a < b:
            arr.append(random.randint(a, b))
        elif a > b:
            arr.append(random.randint(b, a))
        elif a == b:
            while a == b:
                print("Діапазон не може бути рівний!")
                print("Введіь елемент a:")
                a = set_the_value()
                print("Введіь елемент b:")
                b = set_the_value()
    return arr

def merge_two_elements(a, b):   # Функція для злиття двох елементів
    global count
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
            count += 1
        else:
            result.append(b[j])
            j += 1
            count += 1
    if i < len(a):
        result += a[i:]
        count += 1
    if j < len(b):
        result += b[j:]
        count += 1
    return result

def merge_sort(arr):     # Функція для сортування масиву
    global count
    if len(arr) == 1:
        count += 1
        return arr
    middle = len(arr)//2
    left = merge_sort(arr[:middle])
    rigth = merge_sort(arr[middle:])
    count += 1
    return merge_two_elements(left, rigth)

def method_selection():    #Функція для вибору методу створення масиву
    print("Доброго дня, шановний користувач!\n"
          "Якщо ви бажаєте ввести масив довжини N з клавіатури, то введіть 'a'\n"
          "Якщо ви бажаєте згенерувати довільний масив довжини N зі значень, які знаходяться в діапазоні [a, b], де a,b вводяться з клавіатури, то введіть 'b'\n"
          "Якщо ви бажаєте завершити роботу програми введіть 'exit'")
    while True:
            sposib = input("Ви вибираєте: ")
            if sposib == 'exit':
                print('Програма завершила роботу')
                exit()
            elif sposib == 'a':
                return merge_sort(create_an_array())
            elif sposib == 'b':
                return merge_sort(create_an_random_array())
            else:
                print("Упс, помилка! Такого варіанту у нас нема. Спробуй ще раз.")

while True:
    count = 0
    print("Відсортований масив: " + str(method_selection()))
    print("Кількість операцій, виконаних при цьому: " + str(count))