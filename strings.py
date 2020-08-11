prefixes = 'JKLMNOPQ'
suffix = 'ack'
add3 = prefixes.replace('O', 'Ou')
add = 'u' + suffix
for letter in prefixes:
    letter1 = letter.replace('O', 'Ou')
    print(letter1.replace('Q','Qu') + suffix)



word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
    print(count)


def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


day = 'Sunday'
months = 'July'
def my_splice(day, months):
    for letters in day:
        if len(day) == 6:
            return day +' 20th of ' + months
        else:
            return 'Today is ' + day.replace('Sun', 'Tues') + ' 28th of ' + months.upper() + ' my younger brother birthday'

day = 'WEDNESDAY'
for i in day:
    today = day[7:]
    monday = day.replace('EA', 'EAS')
    print(i + today)


def my_splice2(a, b):
    sum = len(a) + len(b)
    sum2 = a+ ' ' +b
    print(sum)
    print(a[:2]+ b[1:2])
    print(sum2.split())
    
    
    
