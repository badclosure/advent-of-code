def find_start_packet(input_str):
    for i in range(len(input_str) - 3):
        substr = input_str[i : i + 4]
        if len(set(list(substr))) == 4:
            print(i + 4)
            break


def find_start_message(input_str):
    for i in range(len(input_str) - 13):
        substr = input_str[i : i + 14]
        if len(set(list(substr))) == 14:
            print(i + 14)
            break


with open("../input/day06.txt", "r") as handle:
    lines = handle.readlines()


EXAMPLE_1 = "bvwbjplbgvbhsrlpgdmjqwftvncz"

if __name__ == "__main__":
    find_start_packet(lines[0])
    find_start_message(lines[0])
    find_start_message(EXAMPLE_1)
    # process_code(EXAMPLE_1)
