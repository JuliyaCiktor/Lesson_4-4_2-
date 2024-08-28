numbers = [5,6,9,7,1,6,6]
if len(numbers) == 0:
    result = 0
    print("the list is empty")
else:
    summ = 0
    num = 0
    while num < len(numbers):
        if num % 2 == 0:
            summ = summ + numbers[num]
        num = num + 1
    last_num = numbers[len(numbers) - 1]
    result = summ * last_num
print(result)