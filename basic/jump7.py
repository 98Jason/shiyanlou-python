num = 0
while num < 100:
    num +=1
    if num % 7 == 0 or num % 10 == 7 or num // 10 == 7:
        continue
    print(num)
