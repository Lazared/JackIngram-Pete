
import tkinter as tk
from tkinter import ttk
import math
import random
import match_simulation as ms

class LeagueTable:
    def __init__(self, root):
        self.root = root
        self.root.title("Football League Simulator")
        # Ensuring the window has a minimum size for consistent display
        self.root.minsize(600, 400)

        # Create a frame for the league table with a scrollbar
        self.table_frame = ttk.Frame(root)
        self.table_frame.pack(side=tk.RIGHT, padx=10, pady=10)
        self.scrollbar = ttk.Scrollbar(self.table_frame, orient="vertical")
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a label for the league table
        self.table_label = ttk.Label(self.table_frame, text="League Table")
        self.table_label.pack()

        # Placeholder for the table widget (e.g., Treeview) - to be implemented
        self.table = ttk.Treeview(self.table_frame, yscrollcommand=self.scrollbar.set, columns=("Rank", "Team", "Points", "Games Played", "Wins", "Draws", "Losses"), show="headings")
        self.table.heading("#1", text="Rank")
        self.table.heading("#2", text="Team")
        self.table.heading("#3", text="Points")
        self.table.heading("#4", text="Games Played")
        self.table.heading("#5", text="Wins")
        self.table.heading("#6", text="Draws")
        self.table.heading("#7", text="Losses")

        # Set column widths and anchor text to center
        self.table.column("#1", width=50, anchor=tk.CENTER)
        self.table.column("#2", width=100, anchor=tk.CENTER)
        self.table.column("#3", width=75, anchor=tk.CENTER)
        self.table.column("#4", width=100, anchor=tk.CENTER)
        self.table.column("#5", width=75, anchor=tk.CENTER)
        self.table.column("#6", width=75, anchor=tk.CENTER)
        self.table.column("#7", width=75, anchor=tk.CENTER)
        
        self.table.pack()
        self.scrollbar.config(command=self.table.yview)

       # Define the number of teams
        num_teams = 10

        # Create a list of team names
        self.team_names = [f"Team {chr(65 + i)}" for i in range(num_teams)]

        # Insert teams into the table with initial points (0)
        for team in self.team_names:
            self.table.insert("", "end", iid=team, values=(0, team, 0, 0, 0, 0, 0))


        # Initialization of GUI elements for simulation control - placeholders for future implementation
        self.init_simulation_controls()

    def init_simulation_controls(self):
        """Initialize GUI elements for simulation control like start, pause, and reset buttons."""
        control_frame = ttk.Frame(self.root)
        control_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Start button
        start_button = ttk.Button(control_frame, text="Start Simulation", command=self.start_simulation)
        start_button.pack(pady=5)

        # Pause button - functionality to be implemented
        pause_button = ttk.Button(control_frame, text="Pause Simulation", command=self.pause_simulation)
        pause_button.pack(pady=5)

        # Reset button - functionality to be implemented
        reset_button = ttk.Button(control_frame, text="Reset Simulation", command=self.reset_simulation)
        reset_button.pack(pady=5)

    def start_simulation(self):
        """Start or resume the football league simulation - functionality to be implemented."""
        # def simulate_match(self):
        # Edd self.root.withdraw()  # Hide the league table window
        # Create the football pitch window
        football_pitch_window = tk.Toplevel(self.root)
        football_pitch = FootballPitch(football_pitch_window, self.team_names, self.table)

        pass

    def pause_simulation(self):
        """Pause the ongoing football league simulation - functionality to be implemented."""
        pass

    def reset_simulation(self):
        """Reset the simulation to its initial state - functionality to be implemented."""
        pass

    def quit_application(self):
        """Cleanly quit the application."""
        self.root.destroy()  # This closes the Tkinter window

class FootballPitch:
    def __init__(self, root, team_names, table):
        self.root = root
        self.root.title("Football Pitch with Players and Football")

        # Create a canvas to draw the football pitch
        self.canvas = tk.Canvas(self.root, width=810, height=600)
        self.canvas.pack()

        self.timer_frame = ttk.Frame(self.root)
        self.timer_frame.pack(side=tk.TOP, fill=tk.X)

        self.timer = Timer(self.timer_frame)
        # score display 
        self.scoreboard = Score(self.timer_frame)

        # Draw the football pitch with player positions
        self.draw_football_pitch()

        # Update the league table after match simulation
        self.team_names = team_names
        self.table = table

        self.football = Football(self.canvas, 397.5, 300, color="black", radius=5)

        # Create players for the blue and red teams
        self.players = [
            Player(self.canvas, 100, 150, "blue", "defender"),
            Player(self.canvas, 100, 250, "blue", "defender"),
            Player(self.canvas, 100, 350, "blue", "defender"),
            Player(self.canvas, 100, 450, "blue", "defender"),
            Player(self.canvas, 200, 150, "blue", "midfield"),
            Player(self.canvas, 200, 250, "blue", "midfield"),
            Player(self.canvas, 200, 350, "blue", "midfield"),
            Player(self.canvas, 200, 450, "blue", "midfield"),
            Player(self.canvas, 300, 250, "blue", "attacker"),
            Player(self.canvas, 300, 350, "blue", "attacker"),
            Player(self.canvas, 25, 300, "blue", "goalkeeper"),
            Player(self.canvas, 710, 150, "red", "defender"),
            Player(self.canvas, 710, 250, "red", "defender"),
            Player(self.canvas, 710, 350, "red", "defender"),
            Player(self.canvas, 710, 450, "red", "defender"),
            Player(self.canvas, 610, 150, "red", "midfield"),
            Player(self.canvas, 610, 250, "red", "midfield"),
            Player(self.canvas, 610, 350, "red", "midfield"),
            Player(self.canvas, 610, 450, "red", "midfield"),
            Player(self.canvas, 510, 250, "red", "attacker"),
            Player(self.canvas, 510, 350, "red", "attacker"),
            Player(self.canvas, 785, 300, "red", "goalkeeper"),
        ]

        self.canvas.bind("<Motion>", self.check_goal_collision)

    def check_goal_collision(self, event):
        # Get the current position of the football
        coords = self.canvas.coords(self.football.football_id)
        if coords:  # Check if coords is not empty
            # Unpack the coordinates
            x1, y1, x2, y2 = coords

        # Check if the football is within the goal box
        if x1 < 5 and y1 < 300 < y2:
            # Increase the red team score by 1
            self.scoreboard.red_score += 1
            self.scoreboard.update_score(self.scoreboard.blue_score, self.scoreboard.red_score)

            # Reset the football position to the center
            self.canvas.coords(self.football.football_id, 397.5 - self.football.radius, 300 - self.football.radius,
                                397.5 + self.football.radius, 300 + self.football.radius)
        elif x2 > 800 and y1 < 300 < y2:
            # Increase the blue team score by 1
            self.scoreboard.blue_score += 1
            self.scoreboard.update_score(self.scoreboard.blue_score, self.scoreboard.red_score)

            # Reset the football position to the center
            self.canvas.coords(self.football.football_id, 397.5 - self.football.radius, 300 - self.football.radius,
                                397.5 + self.football.radius, 300 + self.football.radius)
    def draw_football_pitch(self):
        # Draw grass and other elements
        self.canvas.create_rectangle(0, 0, 805, 601, fill="green", outline="green")
        self.canvas.create_rectangle(5, 5, 800, 600, outline="white", width=2)  # Outer boundary
        self.canvas.create_line(397.5, 5, 397.5, 600, fill="white", width=2)  # Halfway line
        self.canvas.create_rectangle(5, 230, 70, 370, outline="white", width=2)  # Left penalty area
        self.canvas.create_rectangle(740, 230, 800, 370, outline="white", width=2)  # Right penalty area
        self.canvas.create_oval(347.5, 250, 447.5, 350, outline="white", width=2)  # halfway circle
        self.canvas.create_oval(50, 295, 60, 305, outline="white", fill="blue", width=2)  # blue penalty spot
        self.canvas.create_oval(750, 295, 760, 305, outline="white", fill="red", width=2)  # red penalty spot
        self.canvas.create_arc(50, 330, 90, 270, start=270, extent=180, outline="white", fill="green", width=2)  # blue Penalty semi circle
        self.canvas.create_arc(720, 330, 760, 270, start=90, extent=180, outline="white", fill="green", width=2)  # red Penalty semi circle
        self.canvas.create_rectangle(5, 260, 30, 340, outline="white", width=2)  # red 6 yard box
        self.canvas.create_rectangle(780, 260, 800, 340, outline="white", width=2)  # blue 6 yard box
        self.canvas.create_rectangle(0, 330, 5, 270, outline="blue", fill="blue", width=2) # blue goal box
        self.canvas.create_rectangle(800, 330, 805, 270, outline="red", fill="red", width=2) # red goal box


    
class Timer:
    def __init__(self, parent):
        self.parent = parent 
        self.seconds = 0
        self.timer_label = ttk.Label(parent, text="00:00", font=("Helvetica", 24), foreground="orange", background="black")
        self.timer_label.pack(side=tk.TOP, padx=10, pady=10)
        self.update_timer()

    def update_timer(self):
        minutes = self.seconds // 60
        seconds = self.seconds % 60
        time_string = f"{minutes:02d}:{seconds:02d}"
        self.timer_label.config(text=time_string)
        self.seconds += 1
        self.parent.after(1000, self.update_timer)
        
        if self.seconds == 10:
            self.timer_label.config(text="Match Finished")
            self.parent.after(2000, self.return_to_league_table)

    def open_gui(self):
        root = tk.Tk()
        root.mainloop()

    def return_to_league_table(self):
        self.parent.master.destroy()
        # //Edd self.open_gui()

    
   
class Football:
    def __init__(self, canvas, x, y, color="black", radius=10):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.draw()

    def draw(self):
        self.football_id = self.canvas.create_oval(self.x - self.radius, self.y - self.radius,
                                                    self.x + self.radius, self.y + self.radius,
                                                    fill=self.color)

    def move(self, dx, dy):
        self.canvas.move(self.football_id, dx, dy)

class Score:
    def __init__(self, parent):
        self.parent = parent
        self.blue_score = 0
        self.red_score = 0

        # Create blue score label
        self.blue_score_label = ttk.Label(parent, text=str(self.blue_score), font=("Helvetica", 18), foreground="blue")
        self.blue_score_label.pack(side=tk.LEFT, padx=10, pady=10)

        # Create red score label
        self.red_score_label = ttk.Label(parent, text=str(self.red_score), font=("Helvetica", 18), foreground="red")
        self.red_score_label.pack(side=tk.RIGHT, padx=10, pady=10)
    
    # Example usage:
    def simulate_game(self):
        team1 = "Team A"
        team2 = "Team B"
        match = ms.MatchSimulation(team1, team2)
        result =match.simulate_match()
        print(f"Match Result: {result['team1']} {result['team1_goals']} - {result['team2_goals']} {result['team2']}")
        print("Outcome:", "Draw" if result["outcome"] == 0 else f"{result['team1']} Wins" if result["outcome"] == 1 else f"{result['team2']} Wins")

    def update_score(self, blue_score, red_score):
        self.blue_score = blue_score
        self.red_score = red_score

        # Update the text of the labels
        self.blue_score_label.config(text=str(self.blue_score))
        self.red_score_label.config(text=str(self.red_score))


class Player:
    def __init__(self, canvas, x, y, color, position):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.color = color
        self.position = position
        self.draw()

    def draw(self):
        # Draw the player as a circle
        self.player_id = self.canvas.create_oval(self.x - 10, self.y - 10, self.x + 10, self.y + 10, fill=self.color, outline="white")


# Function to run the application
def run_app():
    root = tk.Tk()
    app = LeagueTable(root)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("Application interrupted. Exiting...")
        app.quit_application()  # Ensure resources are cleaned up properly

if __name__ == "__main__":
    run_app()
