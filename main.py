import random


def check_winning_position(row_list):
    if row_list[0] == row_list[1] == row_list[2] != " ":
        if row_list[0] == "X":
            print("Player One is the Winner")
        else:
            print("Player Two is the Winner")
        return True
    elif row_list[3] == row_list[4] == row_list[5] != " ":
        if row_list[3] == "X":
            print("Player One is the Winner")
        else:
            print("Player Two is the Winner")
        return True
    elif row_list[6] == row_list[7] == row_list[8] != " ":
        if row_list[6] == "X":
            print("Player One is the Winner")
        else:
            print("Player Two is the Winner")
        return True
    elif row_list[0] == row_list[3] == row_list[6] != " ":
        if row_list[0] == "X":
            print("Player One is the Winner")
        else:
            print("Player Two is the Winner")
        return True
    elif row_list[1] == row_list[4] == row_list[7] != " ":
        if row_list[1] == "X":
            print("Player One is the Winner")
        else:
            print("Player Two is the Winner")
        return True
    elif row_list[2] == row_list[5] == row_list[8] != " ":
        if row_list[2] == "X":
            print("Player One is the Winner")
        else:
            print("Player Two is the Winner")
        return True
    elif row_list[2] == row_list[4] == row_list[6] != " ":
        if row_list[2] == "X":
            print("Player One is the Winner")
        else:
            print("Player Two is the Winner")
        return True
    elif row_list[0] == row_list[4] == row_list[8] != " ":
        if row_list[0] == "X":
            print("Player One is the Winner")
        else:
            print("Player Two is the Winner")
        return True
    else:
        return False


def print_chart(row_list):
    row1 = [row_list[0], " | ", row_list[1], " | ", row_list[2]]
    row2 = [row_list[3], " | ", row_list[4], " | ", row_list[5]]
    row3 = [row_list[6], " | ", row_list[7], " | ", row_list[8]]
    combined_list = row1 + new_line + row2 + new_line + row3
    chart = ''
    for n in range(0, len(combined_list)):
        chart += combined_list[n]

    print(chart)


rows = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

new_line = ["\n", "----------", "\n"]
possible_positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
error_check_array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
is_game_on = True

while is_game_on:
    if " " in rows:
        print(f"Available Positions: {possible_positions}")
        player1_input = int(input('\nPlayer 1--> Pick a position: '))
        while player1_input not in possible_positions or player1_input == " ":
            print("Invalid selection. Please Try Again.")
            player1_input = int(input('Player 1-- Pick a position: '))

        possible_positions.remove(player1_input)
        rows[player1_input] = "X"
        if check_winning_position(rows):
            is_game_on = False
            print_chart(rows)
            break

        # if len(possible_positions) == 0:
        #     is_game_on = False
        #     print(rows)
        #     print("Game has ended")

        else:
            print(f"Available Positions: {possible_positions}")
            player2_input = int(input('\nPlayer 2--> Pick a position: '))
            while player2_input == player1_input or player2_input not in possible_positions:
                if player2_input not in error_check_array:
                    print("Invalid Position. Please Try Again")
                else:
                    print("Position has already been Picked. Please Try Again")
                player2_input = int(input('Player 2-- Pick a position: '))

            possible_positions.remove(player2_input)

            rows[player2_input] = "0"
            if check_winning_position(rows):
                is_game_on = False
                print_chart(rows)
                break

            print_chart(rows)

    else:
        if check_winning_position(rows):
            is_game_on = False
            print("Game Ended")
        else:
            is_game_on = False
            print("Draw")
