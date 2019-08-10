import pandas as pd
import matplotlib.pyplot as plt


datelst = [i for i in range(1880, 2011)]
dM = {i: {} for i in range(1, 11)}
dF = {i: {} for i in range(1, 11)}
s = 0
e = 12
lstF = []
lstM = []
for key in dM:
    for i in datelst[s:e]:
        df = pd.read_csv(r'C:\Users\Epick\Documents\GitHub\pydata-book\datasets\babynames\yob%s.txt' % i, sep=',',
                         names=["name", "sex", "number"])
        for j in range(len(df)):
            if df['name'][j] in dM[key] and df['sex'][j] == 'M':
                dM[key][df['name'][j]] += int(df['number'][j])
            elif df['name'][j] not in dM[key] and df['sex'][j] == 'M':
                dM[key][df['name'][j]] = int(df['number'][j])
    s += 13
    if e == 116:
        e += 14
    else:
        e += 13
    D = dM[key].values()
    Dsort = sorted(D, reverse=True)
    for Key in dM[key]:
        if dM[key].get(Key) == Dsort[0]:
            lstM.append(Key)
            break

s = 0
e = 12
for key in dF:
    for i in datelst[s:e]:
        df = pd.read_csv(r'C:\Users\Epick\Documents\GitHub\pydata-book\datasets\babynames\yob%s.txt' % i, sep=',',
                         names=["name", "sex", "number"])
        for j in range(len(df)):
            if df['name'][j] in dF[key] and df['sex'][j] == 'F':
                dF[key][df['name'][j]] += int(df['number'][j])
            elif df['name'][j] not in dF[key] and df['sex'][j] == 'F':
                dF[key][df['name'][j]] = int(df['number'][j])
    s += 13
    if e == 116:
        e += 14
    else:
        e += 13
    D = dF[key].values()
    Dsort = sorted(D, reverse=True)
    for Key in dF[key]:
        if dF[key].get(Key) == Dsort[0]:
            lstF.append(Key)
            break
lstall = list(set(lstM)) + list(set(lstF))
for i, e in enumerate(lstall):
    f1 = []
    for k in datelst:
        F = 0
        df = pd.read_csv(r'C:\Users\Epick\Documents\GitHub\pydata-book\datasets\babynames\yob%s.txt' % k, sep=',',
                         names=["name", "sex", "number"])
        for j in range(len(df)):
            if df['name'][j] == e:
                F += int(df['number'][j])
        f1.append(F)

    fig, ax = plt.subplots()
    ax.set_title('Динамика рождаемости')
    ax.plot(datelst, f1, color='black', label=e)
    ax.set_xlabel("Год")
    ax.set_ylabel("Количество")
    ax.legend()
    ax.grid()
    plt.show()
    fig.savefig(e)
