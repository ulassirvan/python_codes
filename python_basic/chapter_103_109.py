print("ulas")
counter = 0
number = 2
prime = []

while counter < 10:
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        prime.append(str(number))
        counter += 1
    number += 1

print(','.join(prime))

def dobule_accont_calculator(start,interest_rate):
    futer_value=start
    year=1
    while True:
        print(year)
        futer_value+=(interest_rate*(futer_value/100))
        year +=1
        if futer_value >= (2 * start):
            return futer_value, year


print(dobule_accont_calculator(1000,4))

max_iters = 10000
iters = 0
w_0 = -1
previous_step_size = 1
learning_rate = 0.01
precision = 0.000001
derivative = lambda w: 2 * w - 4

while previous_step_size > precision and iters < max_iters:
    w_prev = w_0
    w_0 = w_prev - learning_rate * derivative(w_prev)
    previous_step_size = abs(w_0 - w_prev)
    iters += 1

print(f'A local minimum in point: {w_0:.2f}')

numbers = [1, 2, 3, 4, 5, 6,7, 8, 9]
target = 7
start = 0
end = len(numbers) - 1
flag = None

while start <= end:
    mid = int((start + end) / 2)
    if numbers[mid] == target:
        flag = True
        break
    else:
        if numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

if flag:
    print('Found')
else:
    print('Not found')



sum = 3000
counter = 0


try:
    result=sum/counter

except ZeroDivisionError:
    print('Division by zero.')



try:
    with open("file.txt","r")as file:
        content=file.read()
except FileNotFoundError:
    print("oyle bir dosya yok")



users = {'001': 'Mark', '002': 'Monica', '003': 'Jacob'}
user_id = '004'

try:
    print(users[user_id])
except KeyError:
    users[user_id]=None
    print(users)
