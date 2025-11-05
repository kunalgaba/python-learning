def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print(" " * (n-i), end="")
        print("#" * i," " *(n-i))
        

if __name__ == "__main__":
    main()