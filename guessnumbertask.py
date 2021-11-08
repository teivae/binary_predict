"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np
from numpy.random.mtrand import randint

def random_predict(number: int = 1) -> int:
    count = 1
    min =1
    max=101
    predict_number=(min+max)//2
    predict_number = np.random.randint(1, 101)  # предполагаемое число
    while number !=predict_number:
        count += 1
        if number > predict_number:
            min=predict_number+1
        elif number<predict_number:
            max=predict_number-1
        predict_number=(min+max)//2
    return count
num=randint(1,101)
print(num)
print(random_predict(num))

def score_game(random_predict) -> int:
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
