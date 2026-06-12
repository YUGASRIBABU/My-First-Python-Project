# 1. We define the machine and tell it to expect two inputs: the number and the limit
def multiplication_table(number, limit):
    
    # 2. We set up our conveyor belt loop using range()
    for i in range(1, limit + 1):
        
        # 3. Every time the belt moves, it calculates and prints the line
        result = number * i
        print(f"{number} x {i} = {result}")

# 4. We turn on the machine at the very bottom with our own choices 

multiplication_table(7, 12)