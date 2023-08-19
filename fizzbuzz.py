n = int(input("Enter the value of n: "))

for x in range(n):
    fizz = x % 3
    buzz = x % 5
    if fizz == 0 and buzz == 0:
        print("FizzBuzz")

    elif fizz != 0 and buzz == 0:
        print("Buzz")

    elif fizz == 0 and buzz != 0:
        print("Fizz")
    
    else:
        print(int(x))