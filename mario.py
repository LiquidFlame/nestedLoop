def main():
    print_column(3)
    print("---------")
    print_row(4)
    print("---------")
    print_square(3)
    print("---------")
    print_square2(3)
    print("---------")
    print_square3(3)
    
def print_column(height):
    print("#\n" * height, end="")
    
def print_row(width):
    print("?" * width)
    
def print_square(size):
    # For each row in square
    for i in range(size):
        # For each brick in row
        for j in range(size):
            # Print brick
            print("#", end="")
        print()
        
def print_square2(size):
    for _ in range(size):
        print("#" * size)
        
def print_square3(size):
    for _ in range(size):
        print_row2(size)
    
def print_row2(width):
    print("#" * width)
        
main()