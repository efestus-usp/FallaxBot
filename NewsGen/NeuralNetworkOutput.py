import re, datetime, random

def getText():
    text = "\n"

    now = datetime.datetime.now()

    with open('output.txt', 'r') as fin:
        data = fin.read().splitlines(True)
        text = data[0]
    with open('output.txt', 'w') as fout:
        fout.writelines(data[1:])

    array = text.split()

    newText = "\n"

    for index, string in enumerate(array):
        number = [int(s) for s in re.findall(r'\b\d+\b', string)]
        if(number != None and len(number) > 0):
            if(number[0] > 2000 and number[0] < now.year):
                array[index] = random.randint(now.year, 2030)

        newText += str(array[index]) + ' '

    print(newText)

    return newText