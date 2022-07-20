from icecream import ic
dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
dji2 = ('HD.US', 'GS.US', 'NKE.US')

ic(dji1+dji2)

dji1 = ('AAPL.US', 'IBM.US', 'MSFT.US')
dji2 = ('HD.US', 'GS.US', 'NKE.US')
bos_liste=((dji1),(dji2))
ic(bos_liste)


members = (('Kate', 23), ('Tom', 19))
tuple_n=members[0]+("jhon",26)+members[1]
ic(tuple_n)


default = ('YES', 'NO', 'NO', 'YES', 'NO')
ic(default.count("YES"))

names = ('Monica', 'Tom', 'John', 'Michael')
sorted_names=tuple(sorted(names))
ic(sorted_names)

info = (('Monica', 19), ('Tom', 21), ('John', 18))
ic(sorted(info, key=lambda item: item[1]))


stocks = (('Apple Inc', ('AAPL.US', 310)), ('Microsoft Corp', ('MSFT.US', 184)))
ic(stocks[0][1][0])

