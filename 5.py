import pandas as pd
import matplotlib.pyplot as plt
from string import ascii_uppercase
import numpy as np


index = np.arange(len(ascii_uppercase))
a = ord('A')
b = ord('a')
az = [chr(i) for i in range(a, a+26)]  # генерация списка заглавных букв алфавита
za = [chr(i) for i in range(b, b+26)]  # генерация списка строчных букв алфавита
AZ = {az[i]: 0 for i in range(len(az))}  # генерация словаря счетчиков букв заглавных букв алфавита
ZA = {za[i]: 0 for i in range(len(za))}  # генерация словаря счетчиков букв строчных букв алфавита
datelst = ['1900', '1945', '1990', '2005']  # список выбранных лет
for i in datelst:  # чтение файла
    df = pd.read_csv(r'C:\Users\Epick\Documents\GitHub\pydata-book\datasets\babynames\yob%s.txt' % i, sep=',',
                     names=["name", "sex", "number"])
    for j in range(len(df)):   # цикл подсчета первых букв
        if df['name'][j][0] in AZ:
            AZ[df['name'][j][0]] += 1
    for j in range(len(df)):  # цикл подсчета последних букв
        if df['name'][j][-1] in ZA:
            ZA[df['name'][j][-1]] += 1
    fig, ax = plt.subplots()
    ax.set_title(i+' год')
    ax.bar(index - 0.2, AZ.values(), color='blue', label="первая буква", width=0.4)
    ax.bar(index + 0.2, ZA.values(), color='yellow', label='последняя буква', width=0.4)
    ax.set_xlabel("Буква")
    ax.set_ylabel("Количество имен")
    ax.set_xticks(index)
    ax.set_xticklabels(ascii_uppercase)
    ax.legend()
    plt.show()
    fig.savefig(i)
    
