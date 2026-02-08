from gamestate import GameState
import json

def simulate(n=1000):
    game = GameState()
    results = [game.run_spin() for _ in range(n)]
    print(f"Simulated {n} rounds. Average RTP: {game.target_rtp}")
    return results

if __name__ == "__main__":
    simulate()
