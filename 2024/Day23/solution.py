def get_input():
    with open("input", "r") as file:
        file_input = file.read().split('\n')

    links = [tuple(line.split('-')) for line in file_input]
    return links


def create_link_dict(links):
    link_dict = {}
    for a, b in links:
        if a not in link_dict:
            link_dict[a] = []
        if b not in link_dict:
            link_dict[b] = []
            
        if b not in link_dict[a]:
            link_dict[a].append(b)
        if a not in link_dict[b]:
            link_dict[b].append(a)
    
    return link_dict


def get_connected_sets(link_dict):
    lan_sets = set()
    for node in link_dict:
        if node[0] == 't':
            neighbors = link_dict[node]
            for i in range(len(neighbors)):
                for j in range(i + 1, len(neighbors)):
                    if neighbors[j] in link_dict[neighbors[i]]:
                        lan_sets.add(tuple(sorted((node, neighbors[i], neighbors[j]))))

    return len(lan_sets)


def get_largest(link_dict):
    largest = []
    for node in link_dict:
        neighbors = link_dict[node]
        lan = [node]
        for neighbor in neighbors:
            if all(neighbor in link_dict[other] for other in lan):
                lan.append(neighbor)
        if len(lan) > len(largest):
            largest = lan

    return sorted(largest)


def solve(links):
    link_dict = create_link_dict(links)
    connected_sets = get_connected_sets(link_dict)

    largest_list = get_largest(link_dict)
    part_2 = ','.join(largest_list)
    
    return connected_sets, part_2


def main():
    links = get_input()

    part_1, part_2 = solve(links)
    
    print(f"Part One: {part_1}")
    print(f"Part Two: {part_2}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
