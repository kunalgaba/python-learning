'''
try:
    x = int(input("Whats x? "))
except ValueError:
    print("X is not an integer")
else:        
    print(f"x is {x}")'''

while True:
    try:
        x = int(input("Whats x? "))
    except ValueError:
        #print("X is not an integer")
        pass
    else:     
        break;   
print(f"x is {x}")
