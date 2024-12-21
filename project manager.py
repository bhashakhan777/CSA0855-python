from itertools import combinations

def find_team_combinations(team_members, team_size):
    
    return list(combinations(team_members, team_size))


team_members = ['Alice', 'Bob', 'Charlie', 'David']
team_size = 2
possible_combinations = find_team_combinations(team_members, team_size)


print(possible_combinations)
