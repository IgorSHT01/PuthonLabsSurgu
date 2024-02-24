# laba 1
## 00_distance
### задание:
Есть словарь координат городов

sites = {

    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),

}

Составить словарь словарей расстояний между ними расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

### решение:

<img width="701" alt="distances_00" src="https://github.com/IgorSHT01/PythonLabsSurgu/assets/145825325/9ca311e8-e5ca-4768-b110-a86b1bcfd78a">

1.создаем пустой словарь distances2

2.высчитываем расстояние с помощью функии def a()

3.создаем цикл for, который будет добавлять значения из словаря sites в словарь distances2 

4.выводим результат

<img width="1357" alt="00_distances" src="https://github.com/IgorSHT01/PythonLabsSurgu/assets/145825325/49d74e55-fbde-4a37-aea0-025249e1d3c2">


## 01_circle
### задание:
Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой

radius = 42, pi = 3.1415926

### решение:

S=round(pi * radius**2, 4)
print(S)

<img width="921" alt="01_circle1" src="https://github.com/IgorSHT01/PythonLabsSurgu/assets/145825325/29b803bd-f608-491d-8926-8fd34c1160c8">

<img width="731" alt="01_circle2" src="https://github.com/IgorSHT01/PythonLabsSurgu/assets/145825325/5dfc6e8b-a716-45d6-a12d-3f5ec2d9890d">

<img width="933" alt="01_circle3" src="https://github.com/IgorSHT01/PythonLabsSurgu/assets/145825325/8cbd27e3-e087-43da-8d13-70d0871b5728">

## 02_operations
### задания:
Расставьте знаки операций "плюс", "минус", "умножение" и скобки между числами "1 2 3 4 5" так, что бы получилось число "25".

### решение:
formula = (1 * 2) + (3 + (4*5))
print(formula)



