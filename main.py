
def encode(thing):
    encoded = ''
    for i in range(0, len(thing)):
        digit = int(thing[1]) +3
        if digit > 9:
            digit = digit % 10
        encoded += str(digit)
    return thing


def decode(password):
    decoded = ''
    for i in range(0, len(password)):
        digit = int(password[i]) - 3
        if digit < 0:
            digit = digit + 10
        decoded += str(digit)
    return decoded


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