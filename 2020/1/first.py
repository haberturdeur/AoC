numbers = []
with open("data.txt") as f:
    for line in f:
        numbers.append(int(line))
        
    for i, a in enumerate(numbers):
        for j, b in enumerate(numbers[i+1:]):
            if a + b == 2020:
                print(a, b, a*b)