# 거스름돈
money = int(input())

coins = [500, 100, 50, 10]

answer = 0
for coin in coins :
    answer += money // coin
    money %= coin

print(answer)