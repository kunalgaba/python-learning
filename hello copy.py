def main():
    #function with a return value
    # name = input("Whats your name? ").strip().title()
    hello()
    name = input("What's your name?")
    hello(name)
    # print the name

def hello(to="world"):
    print ("hello,", to)

main()