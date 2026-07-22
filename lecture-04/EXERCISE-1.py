print('KPH\tMPH')
print('----------------')
for kph in range(60, 199+1, 10):
    mph = kph * 0.621371
    print(f'{kph}\t{mph:.1f}')