import random


# 1. Symbols, dummy/only one time used
def boa():
    global winner1, winner2
    name = {
        "num1": "!",
        "num2": "@",
        "num3": "#",
        "num4": "$",
        "num5": "%",
        "num6": "^",
        "num7": "&",
        "num8": "*",
        "num9": "?"
    }
    board = [
        [f"{name.get('num1')}", f"{name.get('num2')}", f"{name.get('num3')}"],
        [f"{name.get('num4')}", f"{name.get('num5')}", f"{name.get('num6')}"],
        [f"{name.get('num7')}", f"{name.get('num8')}", f"{name.get('num9')}"]
    ]
    print_boa(board)


# 2. Good Board/ main
def print_boa(bo, fro_d=False):
    import time
    global winner1
    global winner2
    global counter
    if value:
        for i in range(len(bo)):
            if i % 1 == 0 and i != 0:
                print("--+---+---")

            for j in range(len(bo[0])):
                if j % 1 == 0 and j != 0:
                    print(" | ", end="")

                if j == 2:
                    print(bo[i][j])

                else:
                    print(str(bo[i][j]) + "", end="")

                if i == 2 and j == 2:
                    print("""
--------------
                    """)

    if winner1:
        winner1 = True
        winner2 = False
        print("You won the match!!")

    elif winner2:
        winner2 = True
        winner1 = False
        print("You lost the match! Ha! Ha!")
    elif counter >= 9:
        print("Match Drawn!")
    elif not winner1 and not winner2:
        if not fro_d:
            user(bo)

        elif fro_d:
            print("Computer.......")
            time.sleep(3)
            comp(bo)


# 3. input and changing symbol/ main
def user(bo):
    val = ""
    global co_value
    global value
    global counter
    if value:
        val = input("Which position: ")

        for item in range(len(bo)):
            for i in range(len(bo[0])):
                if val == bo[item][i]:
                    counter += 1
                    bo[item][i] = use

        co_value = False
    decider(bo, counter, fro=True)


# Computer solver
def comp(bo):
    global value
    global co_value
    global counter
    count = 0
    counter += 1
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == use:
                # Right first stage
                if j < len(bo[0]) - 1 and bo[i][j + 1] == use and count == 0:

                    if bo[i][0] != use and bo[i][0] != com:
                        count += 2
                        bo[i][0] = com

                    elif bo[i][2] != use and bo[i][2] != com:
                        count += 2
                        bo[i][2] = com

                # Right second stage/ Middle
                elif j == 0 and bo[i][j + 2] == use and count == 0:

                    if bo[i][j + 1] != use and bo[i][j + 1] != com:
                        count += 2
                        bo[i][j + 1] = com

                # Down first stage
                elif i < len(bo) - 1 and bo[i + 1][j] == use and count == 0:

                    if bo[0][j] != use and bo[0][j] != com:
                        count = 2
                        bo[0][j] = com

                    elif bo[2][j] != use and bo[2][j] != com:
                        count = 2
                        bo[2][j] = com

                # Down second stage/ Middle
                elif i == 0 and bo[i + 2][j] == use and count == 0:

                    if bo[i + 1][j] != com and bo[i + 1][j] != use:
                        count = 2
                        bo[i + 1][j] = com

                # Diagonal/ Right
                elif i < len(bo) - 1 and j < len(bo[0]) - 1 and bo[i + 1][j + 1] == use and count == 0:

                    if bo[0][0] != use and bo[0][0] != com:
                        count = 2
                        bo[0][0] = com

                    elif bo[2][2] != use and bo[2][2] != com:
                        count = 2
                        bo[2][2] = com

                # Diagonal/ Right second stage/ Middle
                elif i == 0 and j == 0 and bo[i][j] == use and count == 0:

                    if bo[i + 1][j + 1] != use and bo[i + 1][j + 1] != com:
                        count = 2
                        bo[i + 1][j + 1] = com

                # Diagonal/ Left
                elif i < len(bo) - 1 and j >= 1 and bo[i + 1][j - 1] == use and count == 0:

                    if i == 0 and j == 2 and bo[i + 2][j - 2] != com and bo[i + 2][j - 2] != use:
                        count = 2
                        bo[i + 2][j - 2] = com

                    elif i == 1 and j == 1 and bo[i - 1][j + 1] != com and bo[i - 1][j + 1] != use:
                        count = 2
                        bo[0][2] = com

                # Diagonal/ Left Middle
                elif i == 0 and j == 2 and bo[i + 2][j - 2] == use and count == 0:

                    if bo[i + 1][j - 1] != com and bo[i + 1][j - 1] != use:
                        count = 2
                        bo[i + 1][j - 1] = com

                nume = 0
                while count == 0 and nume <= 11:
                    nume += 1
                    rand = int(random.randint(0, 2))
                    rand2 = int(random.randint(0, 2))

                    if bo[rand][rand2] != use and bo[rand][rand2] != com:
                        count += 2
                        bo[rand][rand2] = com

    if co_value:
        rand = int(random.randint(0, 2))
        rand2 = int(random.randint(0, 2))
        bo[rand][rand2] = com
        value = True
        co_value = False

    decider(bo, counter, fro=False)


def decider(bo, coun, fro):
    global winner1
    global winner2

    if fro:
        for verti in range(len(bo)):

            co1 = 0
            winner1 = False
            winner2 = False
            for ho in range(len(bo[0])):
                # User
                if bo[verti][ho] == use:
                    co1 += 1

                    if co1 == 3:
                        winner1 = True
                        winner2 = False
                        print_boa(bo)
                        break

                    cou = 1
                    vert2 = verti
                    while vert2 < len(bo) - 1 and bo[vert2 + 1][ho] == use:
                        cou += 1
                        vert2 += 1
                    if cou == 3:
                        winner1 = True
                        winner2 = False
                        print_boa(bo)
                        break

                    cou = 1
                    vert3 = verti
                    ho2 = ho
                    while vert3 < len(bo) - 1 and ho2 < len(bo[0]) - 1 and bo[vert3 + 1][ho2 + 1] == use:
                        cou += 1
                        vert3 += 1
                        ho2 += 1

                    if cou == 3:
                        winner1 = True
                        winner2 = False
                        print_boa(bo)
                        break

                    cou = 1
                    vert4 = verti
                    ho3 = ho
                    while len(bo) - 1 > vert4 >= 0 and ho3 >= 1 and bo[vert4 + 1][ho3 - 1] == use:
                        cou += 1
                        vert4 += 1
                        ho3 -= 1

                    if cou == 3:
                        winner1 = True
                        winner2 = False
                        print_boa(bo)
                        break

                if winner1:
                    break

            if winner1:
                break

        if coun >= 9 and not winner1 and not winner2:
            print_boa(bo)

        elif fro and not winner2 and not winner1:
            winner1 = False
            winner2 = False
            return print_boa(bo, fro_d=True)

    elif not fro:
        winner1 = False
        winner2 = False
        for i in bo:
            verti = bo.index(i)
            winner1 = False
            winner2 = False
            co2 = 0
            for j in i:
                ho = bo[verti].index(j)
                if bo[verti][ho] == com:
                    co2 += 1

                    if co2 == 3:
                        winner2 = True
                        winner1 = False
                        print_boa(bo)
                        break

                    cou2 = 1

                    vert5 = verti
                    while vert5 < len(bo) - 1 and bo[vert5 + 1][ho] == com:
                        cou2 += 1
                        vert5 += 1

                    if cou2 > 2:
                        winner2 = True
                        winner1 = False
                        print_boa(bo)
                        break

                    cou2 = 1
                    vert6 = verti
                    ho3 = ho
                    while vert6 < len(bo) - 1 and ho3 < len(bo[0]) - 1 and bo[vert6 + 1][ho3 + 1] == com:
                        cou2 += 1
                        vert6 += 1
                        ho3 += 1

                    if cou2 == 3:
                        winner2 = True
                        winner1 = False
                        print_boa(bo)
                        break

                    cou2 = 1
                    vert7 = verti
                    ho4 = ho
                    while len(bo) - 1 > vert7 >= 0 and ho4 >= 1 and bo[vert7 + 1][ho4 - 1] == com:
                        cou2 += 1
                        vert7 += 1
                        ho4 -= 1

                    if cou2 == 3:
                        winner2 = True
                        winner1 = False
                        print_boa(bo)
                        break

                if winner2:
                    break

            if winner2:
                break

        if coun >= 9 and not winner1 and not winner2:
            print_boa(bo)

        elif not fro and not winner1 and not winner2:
            winner1 = False
            winner2 = False
            return print_boa(bo)


start = input("Play Tic Tac Toe (y or n): ")
re = ""
while start == "y" or re == "y":
    use = input("Do you choose(X or O): ").upper()

    counter = 0

    if use == 'X':
        com = 'O'
        value = True
        co_value = False

    elif use == "O":
        com = 'X'
        co_value = True
        value = False

    winner1 = ""
    winner2 = ""
    boa()
    start = "n"
    re = input("Do you want to play again(y or n): ")

