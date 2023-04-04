''' На столе лежат n монеток.
Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
5 -> 1 0 1 1 0
2 '''
num_of_coins = int(input('Введите количество монет на столе: '))
positions = list(map(int, input('Перечислите положение монет через пробел (0 - решка, 1 - герб): ').split()))
count_tails = count_eagle = 0
for position in positions:
    if position == 0:
        count_tails += 1
    else: 
        count_eagle += 1     
count = min(count_eagle, count_tails)
print(f'Количество монет, которое нужно перевернуть - {count}!')