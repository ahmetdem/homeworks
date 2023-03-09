from random import randint

def main(number):
        
    data = {}

    #to get the output count
    for i in range(number):

        r1 = randint(1, 6)
        r2 = randint(1, 6)

        temp = r1+r2

        if temp not in data.keys():
            data[temp] = 1
        else:
            data[temp] += 1

    _min = min(data.values())
    _max = max(data.values())

    #to get normalized value
    for key, val in data.items():
        nv = 1 + ((val - _min) * (12)) / (_max - _min)
        data[key] = int(nv)

    #to print the output
    for key in sorted(data.keys()):
        hey = str(key).ljust(2)
        print(hey, data[key]*'*')

for i in range(2, 5):
    print(f"for {10**i} times: ")
    main(10**i)
    print()