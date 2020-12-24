#FIZZBUZZ GAME 
state =0
for i in range(1,101):
    if i%3==0:
        if i%5==0:
            state = "FizzBuzz"
        else:
            state = "Fizz"
    elif i%5==0:
        state = "Buzz"
    else:
        state = i
    print(state)
