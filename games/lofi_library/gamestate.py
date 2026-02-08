import random

class GameState:
    def __init__(self):
        self.rows, self.cols = 7, 7
        self.symbols = ["Coffee", "Book", "Cat", "Plant", "Vinyl", "Window", "Headphones", "Gold_Candle"]
        self.weights = [60, 50, 40, 30, 20, 15, 10, 5]
        
        self.pay_table = {
            "Coffee":      {5: 0.5, 10: 5.5,  15: 20.0},  # 10-tier increased from 5.0
            "Book":        {5: 1.1, 10: 11.0, 15: 55.0},  # Base increased from 1.0 to 1.1
            "Cat":         {5: 2.0, 10: 20.0, 15: 80.0},
            "Plant":       {5: 3.0, 10: 30.0, 15: 150.0},
            "Vinyl":       {5: 5.0, 10: 50.0, 15: 300.0},
            "Window":      {5: 10.0, 10: 100.0, 15: 500.0},
            "Headphones":  {5: 20.0, 10: 200.0, 15: 1000.0},
            "Gold_Candle": {5: 50.0, 10: 500.0, 15: 5000.0}
        }

    def result(self):
        grid = [[random.choices(self.symbols, weights=self.weights)[0] for _ in range(7)] for _ in range(7)]
        visited, total_payout = set(), 0.0
        for r in range(7):
            for c in range(7):
                if (r, c) not in visited:
                    sym, stack, cluster = grid[r][c], [(r, c)], []
                    visited.add((r, c))
                    while stack:
                        curr_r, curr_c = stack.pop(); cluster.append((curr_r, curr_c))
                        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                            nr, nc = curr_r+dr, curr_c+dc
                            if 0<=nr<7 and 0<=nc<7 and (nr,nc) not in visited and grid[nr][nc]==sym:
                                visited.add((nr,nc)); stack.append((nr,nc))
                    if len(cluster) >= 5:
                        payouts = sorted(self.pay_table[sym].keys(), reverse=True)
                        for tier in payouts:
                            if len(cluster) >= tier:
                                total_payout += self.pay_table[sym][tier]; break
        return {"payout": total_payout}
