from mage import Mage
from battle import simulate_battle

# Test Case 1: Balanced Mage vs Focused Mage
mage1 = Mage(control=2, focus=2, stream=3, physical_condition=3)  # Balanced
mage2 = Mage(control=0, focus=8, stream=1, physical_condition=1)  # Focused on damage

winner, turns = simulate_battle(mage1, mage2)
print(f"Winner: {winner}, Turns: {turns}")
