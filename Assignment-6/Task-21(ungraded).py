# Task-21(ungraded)

def individul_bonus_calculation(player_name, yearly_earning, goals_scored, bonus_per_goal):

    if goals_scored > 30:
        extra_bonus = 10000
    elif goals_scored >= 20:
        extra_bonus = 5000
    else:
        extra_bonus = 0

    bonus = goals_scored * ((bonus_per_goal / 100) * yearly_earning) + extra_bonus
    print(f"{player_name} earned a bonus of {int(bonus)} Taka for {goals_scored} goals")


def earning_bonus(*args):
    for i in range(0, len(args), 4):
        individul_bonus_calculation(args[i], args[i + 1], args[i + 2], args[i + 3])
        #OR:
        #individul_bonus_calculation(*args[i: i + 4])

earning_bonus("Neymar", 1200000, 35, 5, 'Jamal', 700000, 19, 8, 'Luis', 80000, 25, 10)