scores = {
    "rock": 1,
    "paper": 2,
    "scissor": 3,
    "lost": 0,
    "draw": 3,
    "win": 6
}

opponent_mapping = {
    "A": "rock",
    "B": "paper",
    "C": "scissor"
}

self_mapping_task_1 = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissor"
}

rules_task1 = {
    "rock":{
        "scissor": scores["win"],
        "paper": scores["lost"],
        "rock": scores["draw"]
    },
    "paper":{
        "scissor": scores["lost"],
        "paper": scores["draw"],
        "rock": scores["win"]
    },
    "scissor":{
        "scissor": scores["draw"],
        "paper": scores["win"],
        "rock": scores["lost"]
    },
}

self_mapping_task_2 = {
    "X": "lost",
    "Y": "draw",
    "Z": "win"
}

rules_task_2 = [
    "rock",
    "paper",
    "scissor"
]

def task1(day_input):
    total_score = 0
    for game in day_input:
        if game == "":
            continue
        opponent, self = game.split(" ")

        opponent = opponent_mapping[opponent]
        self = self_mapping_task_1[self]

        selection_score = scores[self]
        game_score = rules_task1[self][opponent]

        total_score += selection_score + game_score

    return total_score


def task2(day_input):
    total_score = 0
    for game in day_input:
        if game == "":
            continue
        opponent_option, self = game.split(" ")

        opponent_option = opponent_mapping[opponent_option]
        self_strategy = self_mapping_task_2[self]

        opponent_option_ind = [i for i,val in enumerate(rules_task_2) if val == opponent_option][0]

        if self_strategy == "draw":
            self_options_ind = opponent_option_ind
            game_score = scores["draw"]
        elif self_strategy == "win":
            self_options_ind = opponent_option_ind + 1 if opponent_option_ind < len(rules_task_2) - 1 else 0
            game_score = scores["win"]
        else:
            self_options_ind = opponent_option_ind - 1 if opponent_option_ind > 0 else len(rules_task_2) - 1
            game_score = scores["lost"]

        self_option = rules_task_2[self_options_ind]

        selection_score = scores[self_option]

        total_score += selection_score + game_score

    return total_score
    

if __name__ == "__main__":
    with open("data/inputd2.txt") as f:
        content = f.read().split("\n")

    task1_total_score = task1(content)
    task2_total_score = task2(content)

    print(f"Task1: Total score: {task1_total_score}")
    print(f"Task2: Total score: {task2_total_score}")
        