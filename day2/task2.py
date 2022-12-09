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

self_mapping = {
    "X": "lost",
    "Y": "draw",
    "Z": "win"
}

options = [
    "rock",
    "paper",
    "scissor"
]
with open("data/inputd2.txt") as f:
    content = f.read().split("\n")

total_score = 0
for game in content:
    if game == "":
        continue
    opponent_option, self = game.split(" ")

    opponent_option = opponent_mapping[opponent_option]
    self_strategy = self_mapping[self]

    opponent_option_ind = [i for i,val in enumerate(options) if val == opponent_option][0]

    if self_strategy == "draw":
        self_options_ind = opponent_option_ind
        game_score = scores["draw"]
    elif self_strategy == "win":
        self_options_ind = opponent_option_ind + 1 if opponent_option_ind < len(options) - 1 else 0
        game_score = scores["win"]
    else:
        self_options_ind = opponent_option_ind - 1 if opponent_option_ind > 0 else len(options) - 1
        game_score = scores["lost"]

    self_option = options[self_options_ind]

    selection_score = scores[self_option]

    total_score += selection_score + game_score

print(f"Task2: Total score: {total_score}")
    