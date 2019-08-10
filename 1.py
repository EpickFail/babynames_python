import pandas as pd
import matplotlib.pyplot as plt

datelst = [i for i in range(1880, 2011, 1)]
f = []
m = []
for i in datelst:
    F = 0
    M = 0
    df = pd.read_csv(r'C:\Users\Epick\Documents\GitHub\pydata-book\datasets\babynames\yob%s.txt' % i, sep=',',
                     names=["name", "sex", "number"])
    for j in range(len(df)):
        if df['sex'][j] == 'F':
            F += int(df['number'][j])
        elif df['sex'][j] == 'M':
            M += int(df['number'][j])
    f.append(F)
    m.append(M)
fig, ax = plt.subplots()
ax.set_title('Динамика рождаемости')
ax.plot(datelst, f, color='red', label='Female')
ax.plot(datelst, m, color='blue', label='Male')
ax.set_xlabel("Год")
ax.set_ylabel("Количество")
ax.legend()
ax.grid()
plt.show()


