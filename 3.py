'''Задана натуральная степень k. Сформировать случайным образом список 
коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен 
степени k.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0'''
import random

def add_text(result, coefficient, parameter=""):
    if coefficient!=0:
        if result!="": result+="+"
        result+=str(coefficient)
    if parameter!="": result += "*" + parameter
    return result

result = ''
k=int(input('Введите k '))
coefficients = [random.randint(0,100) for n in range(0,k+1)]
parameters = ["x" if n==-1 else "x^" + str(-n) for n in range(-k,0)]
for i in range(0,len(parameters)):
    result = add_text(result,coefficients[i],parameters[i])
result = add_text(result,coefficients[i+1])
result += "=0"
print(result)