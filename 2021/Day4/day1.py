with open("input.txt", "r") as file:
    lines = file.read().split("\n\n")

bingo_cards = []
bingo_nums = []
winning_called_num_column = 0
winning_called_num_row = 0
winning_row = 0
winning_column = 0
winning_index = 9999
winning_num = 5


def main():
    global bingo_cards
    global bingo_nums
    index = 0
    for card in lines:
        card = card.lstrip()
        if index == 0:
            card = card.split(",")
            for num in card:
                bingo_nums.append(int(num))
            index += 1
            continue
        card = card.replace("  ", " ").replace("\n ", "\n").split("\n")
        card_line = []
        for line in card:
            card_num = []
            line = line.split()
            for num in line:
                card_num.append([int(num), 0])
            card_line.append(card_num)
            bingo_cards.append(card_line)

    for called in bingo_nums:
        row_check(called)
        column_check(called)
    print()
    print("Winning Row", winning_row, "Winning Number", winning_called_num_row)
    total_count = 0
    for line in bingo_cards[winning_row]:
        for num in line:
            if num[1] == 0:
                total_count += num[0]
    print(f'Row {total_count = }')
    final_row = total_count * winning_called_num_row

    total_count = 0
    print("Winning Column", winning_column, "Winning Number",
          winning_called_num_column)
    for line in bingo_cards[winning_column]:
        for num in line:
            if num[1] == 0:
                total_count += num[0]
    print(f'Column {total_count = }')
    final_column = total_count * winning_called_num_column
    print(f'{final_row = }')
    print(f'{final_column = }')


def row_check(called):
    global winning_called_num_row
    global winning_num
    global winning_row
    global winning_index
    for card in bingo_cards:
        for line in card:
            if winning_row != 0:
                break
            row_count = 0
            for num in line:
                if winning_row != 0:
                    break
                if num[0] == called:
                    num[1] = 1
                if num[1] == 1:
                    row_count += 1
                if row_count == winning_num:
                    print()
                    print("Winning Row", bingo_cards.index(card),
                          "Winning Number",
                          called)
                    for line in card:
                        print(line)
                    winning_called_num_row = called
                    winning_row = bingo_cards.index(card)
                    break
        # print()


def column_check(called):
    global winning_called_num_column
    global winning_index
    global winning_column
    index_count = [0, 0, 0, 0, 0]
    for card in bingo_cards:
        for line in card:
            if winning_column != 0:
                break
            index_ = 0
            for num in line:
                if winning_column != 0:
                    break
                if num[0] == called:
                    num[1] = 1
                if num[1] == 1:
                    index_count[index_] += 1
                for index in index_count:
                    if winning_column != 0:
                        break
                    if index == winning_num:
                        print()
                        print("Winning Column", bingo_cards.index(card),
                              "Winning Number",
                              called)
                        for line in card:
                            print(line)
                        winning_called_num_column = called
                        winning_column = bingo_cards.index(card)
                        break
                index_ += 1


if __name__ == "__main__":
    main()
