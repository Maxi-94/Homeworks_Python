# frontend --------------------------
info = """
USER:\t\t{}
LAST CMD:\t{}
"""

# database --------------------------
database = {}

# session ---------------------------
current_user = "anonimus"

# backend ---------------------------
working = True
cmd = "null"

while working:
    print(info.format(current_user, cmd))
    cmd = input(">> ")
    if cmd == "signin":
        login = input("login: ")
        password_1 = input("password: ")
        password_2 = input("repeat password: ")
        if password_1 != password_2:
            print("password don't match!")
            continue
        else:
            database[login] = hash(str(login))
            database[password_1] = hash(str(password_1))
    elif cmd == "login":
        login = input("login: ")
        password = input("password: ")
        if (
            hash(str(login)) == database[login]
            and hash(str(password)) == database[password_1]
        ):
            print("You are logged")
            current_user = login
        else:
            print("Data is not match")

    elif cmd == "log out":
        current_user = "anonimus"

    else:
        working = False
