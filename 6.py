import pandas as pd
import matplotlib.pyplot as plt


d = {'Charlie': "M", 'Martin': "M", 'Mike': "M", 'Jennifer': "F", 'Marilyn': "F"}  # словарь известных людей
datelst = [i for i in range(1940, 2011)]   # список лет
datelstaverage = [i for i in range(1940, 2011, 10)]  # список 10летий
for key in d:
    s = 0
    e = 9
    num = []
    numaverage = []
    for i in datelst:    # чтение файла
        df = pd.read_csv(r'C:\Users\Epick\Documents\GitHub\pydata-book\datasets\babynames\yob%s.txt' % i, sep=',',
                         names=["name", "sex", "number"])
        for j in range(len(df)):  # цикл для формирования списка значений по ключу в словаре
            if df['name'][j] == key and df['sex'][j] == d.get(key):
                num.append(int(df['number'][j]))
    for q in range(len(num)//10):   # цикл формирования спсика средних значений за 10 лет
        numaverage.append(sum(num[s:e]))
        s += 10
        e += 10
    numaverage.append(num[-1])
    fig, ax = plt.subplots()
    ax.set_title("Влияние на динамику")
    ax.plot(datelstaverage, numaverage, color='red', label=key)
    ax.set_xlabel("Год")
    ax.set_ylabel("Рождаемость")
    ax.legend()
    plt.show()
    fig.savefig(key)
