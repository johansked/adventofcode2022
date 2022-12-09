# Communication system
# To be able to communicate with the Elves, the device needs to lock on to their signal
# Signal is a series of seemingly-random characters received one at the time
# Add a subrutine to the device that detects a start-of-package marker
#   Indicated by a sequence of 4 chars that are all different
#   => Identify the first posiiton where the four most recent char wer all different
#       Report the number of chars from begining of buffer to end of the first 4-char marker
# Example mjqjpqmgbljsphdztnvjfqwrcgsmlb The first time a marker appears is after the seventh character arrives
#   I.e. jpqm, m being the seventh char
#   => rutine reports 7 as result

def check_buffer_for_start(buffer, sequence_size):
    current_sequence = []
    for i,char in enumerate(buffer):
        current_sequence.append(char)

        if len(current_sequence) > sequence_size:
            _ = current_sequence.pop(0)

        is_sequence = len(list(set(current_sequence))) == sequence_size

        if is_sequence:
            break

    return i + 1

if __name__ == '__main__':
    with open("data/inputd6.txt") as f:
        content = f.read().strip()

    print(f"Task1: First sequence starts at {check_buffer_for_start(content, 4)}")
    print(f"Task2: First sequence starts at {check_buffer_for_start(content, 14)}")