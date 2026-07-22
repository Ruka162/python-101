column = int(input('How many columns? '))
for i in range(1, 101):
    print(i, end='\t')
    if i % column == 0:
        print()