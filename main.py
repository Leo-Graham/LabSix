
def encode(thing):
    thing_string = int(thing)
    for i in thing_string:
        i += 3
    return thing_string



def main():
    encoded = True

    while True:
        print("Menu\n------------\n1. Encode\n2. Decode\n3. Quit\n")
        menu_choice = int(input("Please enter an option: "))
        if menu_choice == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)

        elif menu_choice == 2:
            decoded = decode(encoded)
            print(f"The encoded password is {encoded} and the original password is {decoded}.")

        elif menu_choice == 3:
            break

if __name__ == "__main__":
    main()