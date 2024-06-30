while True:
    name = input("Enter your name (or 'q' to quit): ")
    if name.lower() == 'q':
        break

    print(f"Hello, {name}!")
    with open('guest_book.txt', 'a') as file:
        file.write(f"{name}\n")
