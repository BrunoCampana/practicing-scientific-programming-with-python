numerals = {'one':'I', 'two':'II', 'three':'III', 'four':'IV', 'five':'V',
            'six':'VI', 'seven':'VII', 'eight':'VIII', 1: 'I', 2: 'II',
            3: 'III', 4:'IV', 5: 'V', 6:'VI', 7:'VII', 8:'VIII'}

for i in ['three', 'four', 'five', 'six']:
    print(numerals[i], end=' ')

for i in range(8, 0, -1):
    print(numerals[i], end=' ')
