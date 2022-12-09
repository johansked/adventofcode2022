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
    #--- Tests
    test_input = "1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000\n".split("\n")
    tests = [{"expected": 24000, "top": 1}, {"expected": 45000, "top": 3}]

    for test in tests:
        result = get_sum_max_calories(test_input, test["top"])
        assert result == test["expected"], f"Expected max calories to be {test['expected']}, got {result}"

    #--- Tasks
    with open('data/inputd1.txt') as f:
        content = f.read().split("\n")
    
    max_calories = get_sum_max_calories(content, 1)
    top_three_calories = get_sum_max_calories(content, 3)

    print(f"Task1: Max carry: {max_calories}")
    print(f"Task2: Top three carry: {top_three_calories}")