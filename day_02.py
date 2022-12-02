"""
A  - rock
B  - paper
C  - scissors
"""

scores = {
    ("A", "B"): 6,
    ("A", "A"): 3,
    ("A", "C"): 0,
    ("B", "A"): 0,
    ("B", "B"): 3,
    ("B", "C"): 6,
    ("C", "A"): 6,
    ("C", "B"): 0,
    ("C", "C"): 3,
}

shape_scores = {"A": 1, "B": 2, "C": 3}


def get_score(file_lines):
    strat_guide = {"X": "A", "Y": "B", "Z": "C"}
    total_score = 0
    for game in file_lines:
        game = game.strip()
        roles = game.split(" ")
        strat_role = strat_guide[roles[1]]
        remaped_roles = (roles[0], strat_role)
        score = scores[remaped_roles] + shape_scores[strat_role]
        total_score += score
    return total_score


print(
    get_score(
        """A Y
B X
C Z""".splitlines()
    )
)

# part 1
print(get_score(open("day_02.txt").readlines()))


def get_score_2(file_lines):
    code_to_score = {"X": 0, "Y": 3, "Z": 6}
    score_role_play = {(score, play[0]): play[1] for play, score in scores.items()}

    total_score = 0
    for game in file_lines:
        game = game.strip()
        roles = game.split(" ")
        desired_score = code_to_score[roles[1]]
        my_role = score_role_play[(desired_score, roles[0])]
        my_role_score = shape_scores[my_role]
        total_score += desired_score + my_role_score
    return total_score


print(
    get_score_2(
        """A Y
B X
C Z""".splitlines()
    )
)

# part 2
print(get_score_2(open("day_02.txt").readlines()))
