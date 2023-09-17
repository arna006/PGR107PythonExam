
def main(string_is_palindromic):

    string = string_is_palindromic.lower()

    for i in range(len(string) // 2):
        if string[i] != string[i - 1]:
            return False
        else:
            return True

    input_string = input("Enter a word you think is palindromic: ")

    while True:
        for char in input_string:
            if not char.isalpha():
                print("You can only type in letters")
                break
            else:
                if main(input_string):
                    print(f"The word {input_string} is a palindromic word.")
                else:
                    print(f"The word {input_string} is not a palindromic word.")
                break
        break

main("")
