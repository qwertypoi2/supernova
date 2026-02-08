import sys
from games.lofi_library.gamestate import GameState

def run_simulation(count=1000):
    game = GameState()
    total_payout = 0
    wins = 0
    
    print(f"Starting simulation of {count} spins...")
    for _ in range(count):
        res = game.result()
        payout = res.get('payout', 0)
        total_payout += payout
        if payout > 0:
            wins += 1
            
    avg_rtp = (total_payout / count) * 100
    hit_rate = (wins / count) * 100
    
    print("-" * 30)
    print(f"Total Spins: {count}")
    print(f"Total Payout: {total_payout:.2f}x")
    print(f"Calculated RTP: {avg_rtp:.2f}%")
    print(f"Hit Rate: {hit_rate:.2f}%")
    print("-" * 30)

if __name__ == "__main__":
    run_simulation(1000)
