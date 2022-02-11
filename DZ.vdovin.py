def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" Формат ввода: введите число от 1 до 9")

inputed = list(range(1, 10))


def draw_board(inputed):
    print()
    print("       Поле игры")
    print("-" * 25)
    for i in range(3):
        print("       ", inputed[0 + i * 3], "", inputed[1 + i * 3], "", inputed[2 + i * 3], "")


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Ход: " + player_token + " - ")
        try:
            player_answer = int(player_answer)
        except:
            print("Неверный числовой диапазон")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(inputed[player_answer - 1]) not in "XO"):
                inputed[player_answer - 1] = player_token
                valid = True
            else:
                print("Это поле занято")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(inputed):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8))
    for each in win_coord:
        if inputed[each[0]] == inputed[each[1]] == inputed[each[2]]:
            return inputed[each[0]]
    return False


def main(inputed):
    greet()
    counter = 0
    win = False
    while not win:
        draw_board(inputed)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(inputed)
            if tmp:
                print(tmp, "Победа")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(inputed)


main(inputed)


