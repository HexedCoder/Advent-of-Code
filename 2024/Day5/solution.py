def get_input():
    with open("input") as _input:
        prereqs_list, updates_list = _input.read().split("\n\n")
    
    prereqs_list = prereqs_list.split("\n")
    prereqs = {}
    for prereq in prereqs_list:
        key, value = map(int, prereq.split("|"))
        if value not in prereqs:
            prereqs[value] = []
        prereqs[value].append(key)

    updates = [list(map(int, update.split(","))) for update in updates_list.split("\n")]
    return [prereqs, updates]

def part_1(input_data):
    prereqs, updates = input_data
    valid_updates = []
    invalid_updates = []
    
    for update in updates:
        completed_pages = set()
        valid_update = True
        
        for page in update:
            if page in prereqs:
                if any(prereq not in completed_pages for prereq in prereqs[page] if prereq in update):
                    valid_update = False
                    break
            completed_pages.add(page)
        
        if valid_update:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)
    
    return sum([update[int(len(update)/2)] for update in valid_updates]), invalid_updates
    
def sort_update(prereqs, update):
    sorted_pages = []
    remaining_pages = update

    while remaining_pages:
        for page in remaining_pages:
            if all(prereq in sorted_pages or prereq not in update for prereq in prereqs.get(page, [])):
                sorted_pages.append(page)
                remaining_pages.remove(page)

    return sorted_pages

def part_2(prereqs, invalid_reports):

    sorted_invalid_reports = [sort_update(prereqs, update) for update in invalid_reports]

    return sum(update[len(update) // 2] for update in sorted_invalid_reports)


def main():
    input_data = get_input()
    sum, invalid_reports = part_1(input_data)
    print("Part 1:", sum)
    print("Part 2:", part_2(input_data[0], invalid_reports))


if __name__ == "__main__":
    main()
    