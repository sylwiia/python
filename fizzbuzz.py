
number = input('Podaj liczbę')

numbers = []

for char in number:
    if char == '0':
        numbers.append('zero')
    elif char == '1':
        numbers.append('jeden')
    elif char == '2':
        numbers.append('dwa')
    elif char == '3':
        numbers.append('trzy')
    elif char == '4':
        numbers.append('cztery')
    elif char == '5':
        numbers.append('pięć')
    elif char == '6':
        numbers.append('sześć')
    elif char == '7':
        numbers.append('siedem')
    elif char == '8':
        numbers.append('osiem')
    elif char == '9':
        numbers.append('dziewięć')

print([' '.join(numbers)])