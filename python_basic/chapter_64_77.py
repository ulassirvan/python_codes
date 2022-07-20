dic={"USA":"w","Türkiye":"Ankara","italya":"Roma"}
print(dic)

capitals = {
    'USA': 'Washington',
    'Germany': 'Berlin',
    'Austria': 'Vienna'
}

print(capitals.keys())
print(capitals.values())


print(capitals.items())


print(capitals.get("Austria"))



stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}



print(stocks.get("AAPL.US"))

stocks['MSFT.US']['Microsoft Corp'] = 190
print(stocks.get("MSFT.US"))


stocks['V.US'] = {'Visa Inc': 185}
print(stocks.values())


tickers = [
    'AAPL.US', 'AXP.US', 'BA.US', 'CAT.US',
    'CSCO.US', 'CVX.US', 'DIS.US', 'DOW.US',
    'GS.US', 'HD.US', 'IBM.US', 'INTC.US'
]
print(list(enumerate(tickers)))


project_ids = {
    '01': 'open',
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}
result = list(set(project_ids.values()))
result.sort()
print(result)


stats = {'site': 'e-smartdata.org', 'traffic': 100, 'type': 'organic'}
stats.pop("traffic")
print(stats)