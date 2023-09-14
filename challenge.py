num = int(input('Donner un nombre : '))
char = input('Ecrire un mot : ')
vowel = 'aeiouy'

if num >= 42 or any(i in char for i in vowel):
    print(num)
else:
    print(char)