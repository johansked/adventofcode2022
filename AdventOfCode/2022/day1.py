def get_sum_max_calories(day_input, top):
    current_sum = 0
    elves = []

    for line in day_input:
        if line == "":
            elves.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(line)

    return sum(sorted(elves, reverse=True)[0:top])

if __name__ == '__main__':
    with open('data/inputd1.txt') as f:
        content = f.read().split("\n")
    
    max_calories = get_sum_max_calories(content, 1)
    top_three_calories = get_sum_max_calories(content, 3)

    print(f"Task1: Max carry: {max_calories}")
    print(f"Task2: Top three carry: {top_three_calories}")