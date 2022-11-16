import random

n = int(input("Please input Hongbao Money: "))
m = int(input("Please input Hongbao Number: "))
#想法：将n 分成m+1 份 ，把最后一份 分成m份 ，再随机加到 m份中
everyMoney = n / (m + 1)
rel = n / (m + 1)
changeRel = n / (m + 1) / m
count = 0
moneyList = []
for i in range(m - 1):
    tmpchange = changeRel * (1 + random.randint(150, 800) / (1000)) * ((-1) ** (random.randint(0, 1000)))
    # 随机
    tmp = everyMoney + tmpchange
    tmp = tmp * 100 // 10 / 10
    rel -= tmp - everyMoney
    if rel < 0:
        tmp = everyMoney + rel
        changeRel = 0
    moneyList.append(tmp)
    count += tmp
count = count * 10
count = int(count) / 10
maxMoney = ((n - count) * 100 // 10 / 10)

#输出

flag = -1
for i in range(m - 1):
    if flag == -1 and random.randint(1, m) % 6 == 0:
        print("the " + str(i + 1) + " is " + str(maxMoney))
        flag = i
        continue
    print("the " + str(i + 1) + " is " + str(moneyList[i]))


if flag == -1:
    print("the " + str(i + 1) + " is " + str(maxMoney))
else:
    print("the " + str(m) + " is " + str(moneyList[flag]))
