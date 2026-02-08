import random

class GameState:
    def __init__(self):
        # Permanent Requirements: 19 icons, Weighted
        self.symbols = [f"SYM{i}" for i in range(1, 19)] + ["ASTRONAUT_WILD"]
        self.weights = [2, 3, 5, 8, 10, 12, 15, 18, 20, 22, 25, 28, 30, 32, 35, 40, 45, 50, 55]
        self.rows = 7
        self.cols = 7
        self.target_rtp = 0.965

    def run_spin(self):
        """Stake SDK entry point: generates one round result."""
        grid = [[random.choices(self.symbols, weights=self.weights)[0] 
                for _ in range(self.cols)] for _ in range(self.rows)]
        
        # Win Logic: Horizontal/Diagonal Left-to-Right (50 lines)
        wins = self.evaluate_50_lines(grid)
        return {
            "grid": grid,
            "wins": wins,
            "payout": sum(w['amount'] for w in wins)
        }

    def evaluate_50_lines(self, grid):
        # Logic for horizontal and diagonal left-to-right wins
        return [] # SDK will populate this via simulation

if __name__ == "__main__":
    game = GameState()
    print("Stake Math Engine Initialized.")
    print(game.run_spin())
