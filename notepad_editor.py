import os

def create_file():
    filename = input("Enter file name (example: notes.txt): ")
    content = []

    print("\nStart typing your text. Type 'SAVE' on a new line to save the file.\n")

    while True:
        line = input()
        if line.upper() == "SAVE":
            break
        content.append(line)

    with open(filename, "w") as file:
        file.write("\n".join(content))

    print(f"\nFile '{filename}' saved successfully!\n")


def open_file():
    filename = input("Enter file name to open: ")

    if not os.path.exists(filename):
        print("File not found!")
        return

    print("\n===== File Content =====\n")
    with open(filename, "r") as file:
        print(file.read())
    print("========================\n")


def edit_file():
    filename = input("Enter file name to edit: ")

    if not os.path.exists(filename):
        print("File not found!")
        return

    print("\nCurrent content:\n")
    with open(filename, "r") as file:
        print(file.read())

    print("\nStart editing. Type 'SAVE' on a new line to save changes.\n")

    content = []
    while True:
        line = input()
        if line.upper() == "SAVE":
            break
        content.append(line)

    with open(filename, "w") as file:
        file.write("\n".join(content))

    print(f"\nFile '{filename}' updated and saved!\n")


def main():
    while True:
        print("===== NOTEPAD / TEXT EDITOR =====")
        print("1. Create New File")
        print("2. Open File")
        print("3. Edit Existing File")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            open_file()
        elif choice == "3":
            edit_file()
        elif choice == "4":
            print("Exiting Notepad... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
