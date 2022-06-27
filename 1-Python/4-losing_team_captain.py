def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    last_team = teams[-1]
    return last_team[1]


### Answer: return teams[-1][1]
