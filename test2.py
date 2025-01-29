import array
myArray = array.array("i",[75000, 85000,92000])
myArray.append(78000)
bonusPercent = 1.08
totalPayList = [i * bonusPercent for i in myArray]
totalPay = sum(totalPayList)
# for salary in myArray:
#     totalPayList.append(salary * bonusPercent)
#     totalPay = totalPay + (salary * bonusPercent)

print(f'Total pay: {totalPay}')