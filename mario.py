# nested loop
def main():
    print_square(3)


def print_square(size):

    # for each row in square
    for i in range(size):
        print_row(size)

# print brick            
def print_row(width):
    print("#" * width)

main()