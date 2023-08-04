def prompt():
    choice, name, email, file_name = "", "", "", ""
    print("-" * 40)
    while choice != "q":
        choice = input("Please enter your name: ")
        if choice != "q":
            name = choice

        choice = input("Please enter your email: ")
        if choice != "q":
            email = choice

        choice = input("Please enter CSV filename (fullpath): ")
        if choice != "q":
            file_name = choice
            break
    print("-" * 40)
    return name, email, file_name
