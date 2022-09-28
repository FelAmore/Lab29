bill = int(input('Enter amount of bill: '))
people = int(input('Enter number of people: '))
tips = int(input('Enter amount of tips (%): '))
tips_total = bill*(tips/100)
total = (bill + tips_total) / people
print(f'Tips amount per person is ${tips_total/people:.2f}')
print(f'Total amount per person is ${total:.2f}')

given = int(input('Enter the number of seconds: '))
if given > 3600:
    hour = given//3600
    minute = (given%3600)//60
    sec = (given%3600)%60
elif given < 3600 and given > 60:
    hour = 0
    minute = given//60
    sec = given%60
else:
    hour = 0
    minute = 0
    sec = given
print(f'{hour}:{minute}:{sec}')
