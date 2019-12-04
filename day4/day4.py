import sys

# Input: 138241-674034
min = int(sys.argv[1])
max = int(sys.argv[2])

def generate_passwords(min, max):
    for i in range(min, max + 1):
        yield [int(number) for number in str(i)]

def match_criteria(password):
    adjacenty_match = False
    for i in range(1, len(password)):
        prev_number = password[i - 1]
        next_number = password[i]
        if next_number < prev_number:
            return False
        if not adjacenty_match:
            adjacenty_match = next_number == prev_number

    return adjacenty_match

matching_passwords = [password for password in generate_passwords(min,max) if match_criteria(password)]
solution = print(len(matching_passwords))
