import random
from enum import Enum
from typing import Final

class Outcome(Enum):
    """Enum class for match outcomes"""
    DRAW = 0
    TEAM1_WINS = 1
    TEAM2_WINS = 2

class MatchSimulation:
    """Class for simulating a match between two teams"""
    def __init__(self, team1: str, team2: str):
        self.team1: Final = team1
        self.team2: Final = team2

    def simulate_match(self) -> dict:
        """Simulate a match and return the result as a dictionary"""
        outcome: Final = random.choices(
            [Outcome.DRAW, Outcome.TEAM1_WINS, Outcome.TEAM2_WINS],
            weights=[1, 2, 2]
        )[0]

        match_result: dict = {
            "outcome": outcome,
            "team1": self.team1,
            "team2": self.team2,
            "team1_goals": 0,
            "team2_goals": 0
        }

        if outcome == Outcome.TEAM1_WINS:
            match_result["team1_goals"] = random.randint(1, 5)
            match_result["team2_goals"] = random.randint(0, match_result["team1_goals"])
        elif outcome == Outcome.TEAM2_WINS:
            match_result["team2_goals"] = random.randint(1, 5)
            match_result["team1_goals"] = random.randint(0, match_result["team2_goals"])

        return match_result

    def get_winner(self) -> str:
        """Return the winning team or 'draw' if the match ended in a draw"""
        match_result: dict = self.simulate_match()

        if match_result["outcome"] == Outcome.DRAW:
            return "Draw"
        elif match_result["outcome"] == Outcome.TEAM1_WINS:
            return match_result["team1"] + " Wins"
        else:
            return match_result["team2"] + " Wins"
        
match_simulation = MatchSimulation("Team A", "Team B")
match_result = match_simulation.simulate_match()
print(f"Match Result:\n"
      f"Team 1: {match_result['team1']} - Goals: {match_result['team1_goals']}\n"
      f"Team 2: {match_result['team2']} - Goals: {match_result['team2_goals']}\n"
      f"Outcome: {match_simulation.get_winner()}")