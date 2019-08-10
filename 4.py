
import pandas as pd
import matplotlib.pyplot as plt


datelst = [i for i in range(1880, 2011, 1)]
name50 = []
for e, i in enumerate(datelst):
    all = 0
    k = 0
    q = 0
    F = 0
    df = pd.read_csv(r'C:\Users\Epick\Documents\GitHub\pydata-book\datasets\babynames\yob%s.txt' % i, sep=',',
                     names=["name", "sex", "number"])
    for j in range(len(df)):
        all += int(df['number'][j])
        if df['sex'][j] == 'F':
            F += 1
    for j in range(len(df)):
        if k < all/4 and df['sex'][j] == 'F':
            k += int(df['number'][j])
        elif k >= all/4:
            q += j + 1
            break
    for j in range(len(df)):
        if k < all/2 and df['sex'][j] == 'M':
            k += int(df['number'][j])
        elif k >= all/2:
            q += j + 1 - F
            name50.append(q)
            break
fig, ax = plt.subplots()
ax.set_title('Динамика рождаемости')
ax.plot(datelst, name50, color='red')
ax.set_xlabel("Год")
ax.set_ylabel("Разнообразие имен")
ax.legend()
ax.grid()
plt.show()






