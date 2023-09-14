def crypt(a, x):
    c_result = ''
    for i in a:
        if i.isalpha():
            b = ord('A' if i.isupper() else 'a')
            c_result += chr((ord(i) - b + x) %26 + b)
        else:
            c_result += i
    print(c_result)

crypt('hello', 4)

crypt('lipps', -4)