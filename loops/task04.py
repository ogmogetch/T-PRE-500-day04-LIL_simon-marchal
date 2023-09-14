for i in range(100, -1, -1):
    if (i != 0 and i != 1):
        print(f'{i} bottles of beer on the wall, {i} bottles of beer.\n Take one down and pass it around, {i-1} bottles of beer on the wall')
    elif i == 1:
        print(f'{i} bottles of beer on the wall, {i} bottles of beer.\n Take one down and pass it around, no more bottles of beer on the wall')
    else:
        print('No more bottles of beer on the wall, no more bottles of beer. \n Go to the store and buy some more, 99 bottles of beer on the wall')