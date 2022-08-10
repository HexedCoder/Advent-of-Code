with open("input.txt", "r") as file:
    lines = file.read().split("\n\n")

bingo_cards = []
bingo_nums = []
winning_cards = []


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
                card_num.append(int(num))
            card_line.append(card_num)
        bingo_cards.append(card_line)

    nums_called = []
    for current_num in bingo_nums:
        for card in bingo_cards:
            nums_called.append(current_num)

            if row_check(nums_called, card) or column_check(nums_called, card):
                card_sum = check_sum(nums_called, card)
                winning_cards.append(card_sum * current_num)

    print(winning_cards[0])


def row_check(called_list, card):
    for row in card:
        count = 0

        for num in row:
            if num in called_list:
                count += 1
        if count == 5:

            return True
    return False


def column_check(called_list, card):
    for row in range(0, 5):
        count = 0
        for column in range(0, 5):
            if card[column][row] in called_list:
                count += 1
        if count == 5:
            return True
    return False


def check_sum(called_list, winning_card):
    card_sum = 0
    for row in winning_card:
        for num in row:
            if num not in called_list:
                card_sum += num
    return card_sum


if __name__ == "__main__":
    main()
