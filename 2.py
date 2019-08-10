import pandas as pd

datelst = [i for i in range(1880, 2011, 1)]
d = {}
for i in datelst:
    df = pd.read_csv(r'C:\Users\Epick\Documents\GitHub\pydata-book\datasets\babynames\yob%s.txt' % i, sep=',',
                     names=["name", "sex", "number"])
    for j in range(len(df)):
        if df['name'][j] in d:
            d[df['name'][j]] += int(df['number'][j])
        else:
            d[df['name'][j]] = int(df['number'][j])
D = d.values()
Dsort = sorted(D, reverse=True)
dsort = []
for key in d:
    for i in range(10):
        if d.get(key) == Dsort[i]:
            dsort.append(Dsort[i])
rev = {}
for key in d:
    rev[d.get(key)] = key
for i, e in enumerate(sorted(dsort, reverse=True)):
    print(rev.get(e), e)
# TOP 10 имен за всю историю
# James 5072771
# John 5061897
# Robert 4788050
# Michael 4265373
# Mary 4119074
# William 4002392
# David 3538748
# Richard 2552269
# Joseph 2529809
# Charles 2347703
