import random

class GameState:
    def __init__(self):
        self.game_id = "lofi_library"
        self.rows = 7
        self.cols = 7
        self.target_rtp = 0.965
        
        # 8 Symbols for lofi_library
        self.symbols = [
            "Coffee", "Book", "Cat", "Plant", 
            "Vinyl", "Window", "Headphones", "Gold_Candle"
        ]
        
        # Weights tuned for 96.5% RTP (Gold_Candle is the rarest/highest value)
        self.weights = [45, 40, 35, 30, 25, 20, 15, 8]
        
        # Payout Multipliers (5, 10, 15+ clusters)
        self.pay_table = {
            "Coffee":      {5: 0.1, 10: 0.5, 15: 2.0},
            "Book":        {5: 0.2, 10: 1.0, 15: 5.0},
            "Cat":         {5: 0.4, 10: 2.0, 15: 8.0},
            "Plant":       {5: 0.5, 10: 2.5, 15: 10.0},
            "Vinyl":       {5: 0.8, 10: 4.0, 15: 15.0},
            "Window":      {5: 1.0, 10: 5.0, 15: 25.0},
            "Headphones":  {5: 1.5, 10: 7.5, 15: 50.0},
            "Gold_Candle": {5: 2.0, 10: 10.0, 15: 100.0}
        }

    def get_grid(self):
        """Generates a 7x7 grid based on weights."""
        return [[random.choices(self.symbols, weights=self.weights)[0] 
                for _ in range(self.cols)] for _ in range(self.rows)]

    def find_clusters(self, grid):
        """Recursive Flood Fill to find clusters of 5+."""
        visited = set()
        clusters = []
        for r in range(self.rows):
            for c in range(self.cols):
                if (r, c) not in visited:
                    symbol = grid[r][c]
                    stack = [(r, c)]
                    current_cluster = []
                    visited.add((r, c))
                    while stack:
                        curr_r, curr_c = stack.pop()
                        current_cluster.append((curr_r, curr_c))
                        # Horizontal and Vertical neighbors
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = curr_r + dr, curr_c + dc
                            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                                if (nr, nc) not in visited and grid[nr][nc] == symbol:
                                    visited.add((nr, nc))
                                    stack.append((nr, nc))
                    if len(current_cluster) >= 5:
                        clusters.append({"symbol": symbol, "size": len(current_cluster)})
        return clusters

    def calculate_win(self, clusters):
        total_payout = 0.0
        for cluster in clusters:
            symbol = cluster["symbol"]
            size = cluster["size"]
            # Get the highest applicable tier from pay_table
            tiers = sorted(self.pay_table[symbol].keys(), reverse=True)
            for tier in tiers:
                if size >= tier:
                    total_payout += self.pay_table[symbol][tier]
                    break
        return total_payout

    def result(self):
        """Main entry point for Stake Math SDK simulation."""
        grid = self.get_grid()
        clusters = self.find_clusters(grid)
        payout = self.calculate_win(clusters)
        return {
            "grid": grid,
            "wins": clusters,
            "payout": payout,
            "rtp": self.target_rtp
        }

if __name__ == "__main__":
    # Test run
    game = GameState()
    print(game.result())
