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
    "X": "rock",
    "Y": "paper",
    "Z": "scissor"
}

rules = {
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

with open("data/inputd2.txt") as f:
    content = f.read().split("\n")

total_score = 0
for game in content:
    if game == "":
        continue
    opponent, self = game.split(" ")

    opponent = opponent_mapping[opponent]
    self = self_mapping[self]

    selection_score = scores[self]
    game_score = rules[self][opponent]

    total_score += selection_score + game_score

print(f"Task1: Total score: {total_score}")
    