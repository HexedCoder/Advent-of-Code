# 261213978 high
def get_input():
    with open("input") as file_input:
        puzzle_input = file_input.read().split("\n")
        lines_input = []

    for line in puzzle_input:
        if line:
            lines_input.append(line.split())
    return lines_input


def hand_sort_p1(hand):
    card_map = '23456789TJQKA'

    return [card_map.index(card) for card in hand[0]]


def hand_sort_p2(hand):
    card_map = 'J23456789TQKA'

    return [card_map.index(card) for card in hand[0]]


def part_one(file_input):
    hand_lists = {"high": [], "pair": [], "2 pair": [], "3 kind": [], "full house": [], "4 kind": [], "5 kind": []}
    total_score = 0

    for hand, bid in file_input:
        bid = int(bid)
        if len(set(hand)) == 1:
            hand_lists["5 kind"].append([hand, bid])
        if len(set(hand)) == 2:
            count = hand.count(hand[0])
            if count == 1 or count == 4:
                hand_lists["4 kind"].append([hand, bid])
            else:
                hand_lists["full house"].append([hand, bid])
        # 3, kind, 2 pair
        if len(set(hand)) == 3:
            three = False
            for card in hand:
                if hand.count(card) == 3:
                    three = True
                    break
            if three:
                hand_lists["3 kind"].append([hand, bid])
            else:
                hand_lists["2 pair"].append([hand, bid])
        # pair
        if len(set(hand)) == 4:
            hand_lists["pair"].append([hand, bid])
        # high card
        if len(set(hand)) == 5:
            hand_lists["high"].append([hand, bid])

    idx = 1
    for key, hand_list in hand_lists.items():
        print(key)
        print("Before", hand_list)
        hand_list.sort(key=hand_sort_p1)
        print("After", hand_list)
        for hand in hand_list:
            total_score += hand[1] * idx
            idx += 1
        print()
    return total_score


def part_two(file_input):
    hand_lists = {"high": [], "pair": [], "2 pair": [], "3 kind": [], "full house": [], "4 kind": [], "5 kind": []}
    total_score = 0

    for hand, bid in file_input:
        joker_count = hand.count("J")
        bid = int(bid)
        # 5 kind
        if len(set(hand)) == 1:
            hand_lists["5 kind"].append([hand, bid])
        # 4 kind, full house
        elif len(set(hand)) == 2:
            if joker_count:
                hand_lists["5 kind"].append([hand, bid])
            else:
                count = hand.count(hand[0])
                if count == 1 or count == 4:
                    hand_lists["4 kind"].append([hand, bid])
                else:
                    hand_lists["full house"].append([hand, bid])
        # 3 kind, 2 pair
        elif len(set(hand)) == 3:
            three = False
            for card in hand:
                if hand.count(card) == 3:
                    three = True
                    break
            # 3 kind
            if three:
                if joker_count:
                    hand_lists["4 kind"].append([hand, bid])
                else:
                    hand_lists["3 kind"].append([hand, bid])
            # 2 pair
            else:
                if joker_count == 1:
                    hand_lists["full house"].append([hand, bid])
                elif joker_count == 2:
                    hand_lists["4 kind"].append([hand, bid])
                else:
                    hand_lists["2 pair"].append([hand, bid])
        # pair
        elif len(set(hand)) == 4:
            if joker_count:
                hand_lists["3 kind"].append([hand, bid])
            else:
                hand_lists["pair"].append([hand, bid])
        # high card
        elif len(set(hand)) == 5:
            if joker_count:
                hand_lists["pair"].append([hand, bid])
            else:
                hand_lists["high"].append([hand, bid])

    # print(hand_lists)
    idx = 1
    for key, hand_list in hand_lists.items():
        hand_list.sort(key=hand_sort_p2)
        for hand in hand_list:
            total_score += hand[1] * idx
            idx += 1
    return total_score


def main():
    puzzle_input = get_input()

    part_1 = part_one(puzzle_input)
    part_2 = part_two(puzzle_input)

    print(f"Part One:", part_1)
    print(f"Part Two:", part_2)


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt, GeneratorExit, Exception) as err:
        from traceback import print_exc
        print_exc()
