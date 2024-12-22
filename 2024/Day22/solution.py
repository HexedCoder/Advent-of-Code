from collections import Counter
import time

def get_input():
    with open("input", "r") as file:
        file_input = file.read().splitlines()
    
    file_input = list(map(int, file_input))
    return file_input

def generate_secret(secret, secret_series, sequence=None):
    steps = 2000
    initial_val = secret

    curr_series = ""
    curr_results = ""
    if sequence:
        seq_idx = 0
        stored_val = None

    while steps > 0:
        secret = (secret ^ (secret * 64)) % 16777216
        secret = (secret ^ (secret // 32)) % 16777216
        secret = (secret ^ (secret * 2048)) % 16777216
        saved_val = int(str(secret)[-1]) - int(str(initial_val)[-1])
        if sequence:
            if saved_val == sequence[seq_idx]:
                if not stored_val:
                    stored_val = saved_val
                seq_idx += 1
                if seq_idx == len(sequence):
                    return int(str(secret)[-1])
            else:
                seq_idx = 0
                stored_val = None

        curr_series = f"{curr_series} {saved_val}"
        curr_results = f"{curr_results} {int(str(secret)[-1])}"
        initial_val = secret
        steps -= 1

    if not sequence:
        secret_series.append((curr_series[1:], curr_results[1:]))
        return secret
    else:
        return 0

def solve(input_data):
    part_1 = 0
    secret_series = []
    for initial_secret in input_data:
        final_secret = generate_secret(initial_secret, secret_series)
        part_1 += final_secret

    # Analyze price change sequences
    sequence_counts = Counter()
    for series, _ in secret_series:
        numbers = list(map(int, series.split()))
        for i in range(len(numbers) - 3):
            sequence = tuple(numbers[i:i + 4])
            sequence_counts[sequence] += 1

    sequence_counts = {k: v for k, v in sequence_counts.items() if v > 150}

    part_2 = 0
    for sequence in sequence_counts:
        current_value = 0

        for series, results in secret_series:
            changes = list(map(int, series.split()))
            prices = list(map(int, results.split()))

            for i in range(len(changes) - 3):
                if tuple(changes[i:i + 4]) == sequence:
                    current_value += prices[i + 3]
                    break
                
            if current_value > part_2:
                print(f"{current_value = }", end="\r")
                part_2 = current_value

    return part_1, part_2


def main():
    input_data = get_input()

    start_time = time.time()
    part_1, part_2 = solve(input_data)
    end_time = time.time()
    
    print(f"Part One: {part_1}")
    print(f"Part Two: {part_2}")

    completion_time = end_time - start_time
    print(f"Completion Time: {completion_time:.2f} seconds")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
