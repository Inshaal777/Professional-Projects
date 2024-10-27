import random
from typing import List, Tuple

class DiceGame:
    def __init__(self, rolls: int = 3):
        self.rolls = rolls
        self.results: List[Tuple[int, int]] = []

    def roll_dice(self) -> Tuple[int, int]:
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        return die1, die2

    def play(self):
        for roll_number in range(1, self.rolls + 1):
            result = self.roll_dice()
            self.results.append(result)
            print(f"Roll {roll_number}: Die 1: {result[0]}, Die 2: {result[1]}")

    def display_results(self):
        print("\nAll rolls:")
        for index, (die1, die2) in enumerate(self.results, start=1):
            print(f"Roll {index}: Die 1: {die1}, Die 2: {die2}")

if __name__ == "__main__":
    game = DiceGame(rolls=3)
    game.play()
    game.display_results()