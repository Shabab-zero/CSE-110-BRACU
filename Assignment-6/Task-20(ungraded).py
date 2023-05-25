# Task-20(ungraded)

def individul_bonus_calculation(player_name, yearly_earning, goals_scored, bonus_per_goal):

    if goals_scored > 30:
        extra_bonus = 10000
    elif goals_scored >= 20:
        extra_bonus = 5000
    else:
        extra_bonus = 0

    bonus = goals_scored * ((bonus_per_goal / 100) * yearly_earning) + extra_bonus
    print(f"{player_name} earned a bonus of {int(bonus)} Taka for {goals_scored} goals")

#Example-1
individul_bonus_calculation("Neymar", 1200000, 35, 5)

#Example-2
individul_bonus_calculation('Jamal', 700000, 19, 8)

#Example-3
individul_bonus_calculation('Luis', 80000, 25, 10)