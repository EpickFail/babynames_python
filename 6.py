import pandas as pd
import matplotlib.pyplot as plt


d = {'Frank': "M", 'Martin': "M", 'Mike': "M", 'Jennifer': "F", 'Marilyn': "F"}
datelst = [i for i in range(1940, 2011)]
for key in d:
    num = []
    for i in datelst:
        df = pd.read_csv(r'C:\Users\Epick\Documents\GitHub\pydata-book\datasets\babynames\yob%s.txt' % i, sep=',',
                         names=["name", "sex", "number"])
        for j in range(len(df)):
            if df['name'][j] == key and df['sex'][j] == d.get(key):
                num.append(int(df['number'][j]))
                print(num)
    fig, ax = plt.subplots()
    ax.set_title("Влияние на динамику")
    ax.plot(datelst, num, color='red', label=key)
    ax.set_xlabel("Год")
    ax.set_ylabel("Количество")
    ax.legend()
    plt.show()
    fig.savefig(key)
