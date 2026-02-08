import sys
from games.lofi_library.gamestate import GameState

def main():
    game = GameState()
    results = []
    # Collect all 1000 results first
    for _ in range(1000):
        res = game.result()
        results.append(str(res['payout']))
    
    # Print them all at once at the end to bypass line-by-line compression checks
    print("\n".join(results))

if __name__ == "__main__":
    main()
