# frontend ------------------------------------------
bucket_3l_list = [" ", " ", " "]
bucket_5l_list = [" ", " ", " ", " ", " "]
clear = "\b" * 10000
front = """

    3l             5l
              _____________
              \{7}{7}{7}{7}{7}{7}{7}{7}{7}{7}{7}/
_________      \{6}{6}{6}{6}{6}{6}{6}{6}{6}/
\{2}{2}{2}{2}{2}{2}{2}/       \{5}{5}{5}{5}{5}{5}{5}/
 \{1}{1}{1}{1}{1}/         \{4}{4}{4}{4}{4}/
  \{0}{0}{0}/           \{3}{3}{3}/
   ¯¯¯             ¯¯¯
"""

# database ------------------------------------------
database = {
    "bucket_3l": 0,
    "bucket_5l": 0,
}

# backend -------------------------------------------
working = True
move_counter = 0
while working:
    bucket_3l_list = (["@"] * database["bucket_3l"] + [" "] * 3)[:3]
    bucket_5l_list = (["@"] * database["bucket_5l"] + [" "] * 5)[:5]
    print(front.format(*(bucket_3l_list[:4] + bucket_5l_list)))
    cmd = input(">> ")

    if cmd == "fill_3l":
        database["bucket_3l"] = 3

    elif cmd == "pour_3l":
        database["bucket_3l"] = 0

    elif cmd == "fill_5l":
        database["bucket_5l"] = 5

    elif cmd == "pour_5l":
        database["bucket_5l"] = 0

    elif cmd == "pour_from_3_to_5":
        if database["bucket_5l"] == 3 and database["bucket_3l"] == 3:
            database["bucket_3l"] = 1
            database["bucket_5l"] = 5
        elif database["bucket_5l"] == 4 and database["bucket_3l"] >= 2:
            database["bucket_3l"] = database["bucket_3l"] - 1
            database["bucket_5l"] = database["bucket_5l"] + 1
        elif database["bucket_5l"] == 5:
            database["bucket_3l"] += 0
            database["bucket_5l"] += 0
        else:
            database["bucket_5l"] += database["bucket_3l"]
            database["bucket_3l"] -= database["bucket_3l"]

    elif cmd == "pour_from_5_to_3":
        if database["bucket_5l"] >= 4 and database["bucket_3l"] == 0:
            database["bucket_3l"] = 3
            database["bucket_5l"] = database["bucket_5l"] - database["bucket_3l"]
        elif database["bucket_5l"] >= 2 and database["bucket_3l"] == 1:
            database["bucket_3l"] = 3
            database["bucket_5l"] = database["bucket_5l"] - 2
        elif database["bucket_5l"] >= 1 and database["bucket_3l"] == 2:
            database["bucket_3l"] = 3
            database["bucket_5l"] = database["bucket_5l"] - 1
        elif database["bucket_3l"] == 3:
            database["bucket_3l"] += 0
            database["bucket_5l"] += 0
        else:
            database["bucket_3l"] = database["bucket_3l"] + database["bucket_5l"]
            database["bucket_5l"] = 0

    elif cmd == "exit":
        break

    if working == True:
        move_counter += 1

    print(clear)
    print(f"Move counter: {move_counter}")

    if database["bucket_5l"] == 4:
        break
