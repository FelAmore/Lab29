bill = int(input('Enter amount of bill: '))
people = int(input('Enter number of people: '))
tips = int(input('Enter amount of tips (%): '))
tips_total = bill*(tips/100)
total = (bill + tips_total) / people
print(f'Tips amount per person is ${tips_total/people:.2f}')
print(f'Total amount per person is ${total:.2f}')
