from examples.mvp_dump_into_json import mvp_dump_into_json
from examples.mvp_with_print import mvp_with_print


def main():
    while True:
        print("===============")
        print("Menu:")
        print("1. Start MVP with print in stdout")
        print("2. Start MVP with JSON dump")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            mvp_with_print()
        elif choice == "2":
            mvp_dump_into_json()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
        print("\n\n")

if __name__ == "__main__":
    main()
