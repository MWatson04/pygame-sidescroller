import json

# Pull high score from file
# Exception to keep game from crashing if file doesn't exist/is corrupted
def get_high_score(hs_file = "highscore.json"):
    try:
        with open(hs_file, "r") as file:
            high_score = json.load(file)
        return high_score
    except (FileNotFoundError, json.JSONDecodeError):
        return 0
    
def store_high_score(score, hs_file = "highscore.json"):
    current_high_score = get_high_score(hs_file)

    if score > current_high_score:
        with open(hs_file, "w") as file:
            json.dump(score, file)