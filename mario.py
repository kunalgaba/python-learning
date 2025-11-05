
def main():
    print_column(3)
    print_column2(3)
    print_row(4)
    print_grid(10)

def print_column(height):
    for _ in range(height):
        print("#")

def print_column2(height):
    print("#\n" *3, end="")

def print_row(width):
    print("?" * width)

def print_grid(size):
    for i in range(size):
        for y in range(size):
            print("#", end="")
        print()

main()

