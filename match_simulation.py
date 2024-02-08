import random

class MatchSimulation:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def simulate_match(self):
        # Randomly decide match outcome: 0 for draw, 1 for team1 wins, 2 for team2 wins
        outcome = random.randint(0, 2)
        match_result = {
            "outcome": outcome,
            "team1": self.team1,
            "team2": self.team2,
            "team1_goals": 0,
            "team2_goals": 0
        }

        # Simulate goals for a more realistic outcome
        if outcome == 1:  # Team 1 wins
            match_result["team1_goals"] = random.randint(1, 5)  # Random goals between 1 and 5
            match_result["team2_goals"] = random.randint(0, match_result["team1_goals"] - 1)
        elif outcome == 2:  # Team 2 wins
            match_result["team2_goals"] = random.randint(1, 5)  # Random goals between 1 and 5
            match_result["team1_goals"] = random.randint(0, match_result["team2_goals"] - 1)
        else:  # Draw
            goals = random.randint(0, 4)  # Random goals between 0 and 4 for a draw
            match_result["team1_goals"] = match_result["team2_goals"] = goals

        return match_result

# Example usage:
team1 = "Team A"
team2 = "Team B"
match = MatchSimulation(team1, team2)
result = match.simulate_match()
print(f"Match Result: {result['team1']} {result['team1_goals']} - {result['team2_goals']} {result['team2']}")
print("Outcome:", "Draw" if result["outcome"] == 0 else f"{result['team1']} Wins" if result["outcome"] == 1 else f"{result['team2']} Wins")
