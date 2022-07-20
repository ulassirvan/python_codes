x = -1.5
expression = 'x**2 + x'
expression.replace("x","-1.5")
print(eval(expression))


var1 = 'Python'
var2 = ('Python')
var3 = ('Python',)
var4 = ['Python']
var5 = {'Python'}

print(isinstance(var1,tuple),isinstance(var2,tuple),isinstance(var3,tuple),isinstance(var4,tuple),isinstance(var5,tuple))


characters = ['k', 'b', 'c', 'j', 'z', 'w']
print(min(characters))
print((max(characters)))


ticker = ('TEN', 'PLW', 'CDR')
full_name = ('Ten Square Games', 'Playway', 'CD Projekt')


print(list(zip(ticker,full_name)))


items = (' ', '0', 0.1, True)
print(all(items))


print(list(bin(234)).count("1"))



def max(nums):
    if nums[0]>nums[1] and nums[0]>nums[2]:
        print(f"{nums[0]}")
    elif nums[1]>nums[0] and nums[1]>nums[2]:
        print(f"{nums[1]}")
    elif nums[2]>nums[0] and nums[2]>nums[1]:
        print(f"{nums[2]}")

max([250,4145,2])


def multi(nums):
    carpım=1
    for i in nums:
        carpım *=i
    return carpım

print(multi([5,5,2]))


def longest_str(strings):
    max_later=0
    for i in strings:
        if max_later<len(i):
            max_later=len(i)

    return max_later


print(longest_str(["ulas","sirvan"]))


def filiters_ge_6 (strings):
    later_s=[]
    max_later=6
    for i in strings:
        if max_later<=len(i):
            later_s.append(i)

    return later_s


print(filiters_ge_6(["ulas","sirvan","asd","asdgasd","123dsad"]))


def faktorel(sayı):
    aws=1
    for i in range(1,sayı+1):
        aws*=i

    return aws

print(faktorel(1548))



def istring(vars):
    str_cunter = 0
    for i in vars:
        if isinstance(i,str):
            str_cunter+=1
    return str_cunter


print(istring(["123213","123213",41,True]))


def istring2(vars):
    str_cunter = 0
    for i in vars:
        if isinstance(i,str):
            if len(i)>=3:
                str_cunter+=1
    return str_cunter


print(istring2(["12","123213",41,True]))



def remove_duplicates(items):
    return list(set(items))
print(remove_duplicates([1,5,5,2,3,5,4,1,2,5,41,1]))




def is_uniqe(items):
    if list(set(items))==items:
        return True
    else:
        return False

print(is_uniqe([2,4,5]))




def function(idx, l=[]):
    for i in range(idx):
        l.append(i ** 3)
    print(l)


print(function(3))
print(function(5,["a","b","c"]))
print(function(6))


def function2(*args, **kwargs):
    print(args, kwargs)

function2(3,4)
function2(x=3,y=4)
function2(1,2,x=3,y=4)


def is_palindrome(metin:str):
    if metin==metin[::-1]:
        return True
    else:
        return False

print(is_palindrome("aba"))



stocks = ['playway', 'boombit', 'cd projekt']


stocks = ['playway', 'boombit', 'cd projekt']
length = list(map(lambda stock: len(stock), stocks))
print(length)


def sort_list(items):
    return sorted(items, key=lambda item: item[1])


func_2 = lambda x,y: x + y + 2


print(func_2(1,3))

items = [(3, 4), (2, 5), (1, 4), (6, 1)]
items.sort(key=lambda item: item[0]**2 + item[1]**2)
print(items)


stocks = [
    {'index': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'index': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'index': 'sWIG80', 'name': 'BBT', 'price': 22}
]



for i in stocks:
    if i["index"]=="mWIG40":
        print(True)
    else:
        print(False)


items = ['P-1', 'R-2', 'D-4', 'F-6']

for i in items:
    print(i.replace("-",""))


num1 = [4, 2, 6, 2, 11]
num2 = [5, 2, 3, 3, 9]


for a in zip(num1,num2):
    print(a[0]%a[1])








