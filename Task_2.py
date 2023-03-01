# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное
# число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random
a = [random.randint(1,11) for i in range(random.randint(5, 15))]
print(a)

# the first way


sums = []
for i in range(len(a)):
    if (i + 1) >= len(a):
        sum  = a[i] + a[0] + a[1]
    elif (i + 2) >=len(a):
        sum  = a[i] + a[i + 1] + a[0]
    elif i < len(a) - 2:
        sum  = a[i] + a[i+1] + a[i+2]
    sums.append(sum)
    sum = 0
print(max(sums))

# the second way

maxSum, sum = 0, 0
i = 0
while i < len(a) - 2:
    sum = a[i] + a[i+1] + a[i+2]
    if sum > maxSum:
        maxSum = sum
    i += 1
if (a[-2] + a[-1] + a[0]) > maxSum:
    maxSum = a[-2] + a[-1] + a[0]
if (a[-1] + a[0] + a[1]) > maxSum:
    maxSum = a[-1] + a[0] + a[1]
print(maxSum)

# the third way

sum_ = 0
for i in range(0, 3):
    sum_ +=a[i]
temp_sum = 0
i = 1
while i < len(a) - 2:
    temp_sum = temp_sum - a[i-1] + a[i+2]
    if temp_sum > maxSum:
        maxSum = temp_sum
    i += 1
if (a[-2] + a[-1] + a[0]) > sum_:
    sum_ = a[-2] + a[-1] + a[0]
if (a[-1] + a[0] + a[1]) > sum_:
    sum_ = a[-1] + a[0] + a[1]
print(maxSum)

# the forth way

j = 0
while j < 2:
    a.append(a[j])
    j+=1
print(a)

sum_ = 0
for i in range(0, 3):
    sum_ +=a[i]
temp_sum = 0
i = 1
while i < len(a) - 2:
    temp_sum = sum_ - a[i-1] + a[i+2]
    if temp_sum > maxSum:
        maxSum = temp_sum
    sum_ = temp_sum
    i += 1
print(maxSum)