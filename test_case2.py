import itertools
import pandas as pd
import matplotlib.pyplot as plt
from mage import Mage
from battle import simulate_battle

# Generate all possible distributions of 10 points among 4 characteristics
distributions = [comb for comb in itertools.product(range(11), repeat=4) if sum(comb) == 10]

# Simulate all battles and collect results
results = []
for dist1 in distributions:
    for dist2 in distributions:
        mage1 = Mage(*dist1)
        mage2 = Mage(*dist2)
        winner, turns = simulate_battle(mage1, mage2)
        results.append({
            "Mage1_Control": dist1[0],
            "Mage1_Focus": dist1[1],
            "Mage1_Stream": dist1[2],
            "Mage1_Physical": dist1[3],
            "Mage2_Control": dist2[0],
            "Mage2_Focus": dist2[1],
            "Mage2_Stream": dist2[2],
            "Mage2_Physical": dist2[3],
            "Winner": winner,
            "Turns": turns
        })

# Convert results to a DataFrame
df = pd.DataFrame(results)

# Function to create victory heatmaps for Mage1 based on two characteristics
def plot_victory_heatmaps(df, characteristic_pairs):
    for char1, char2 in characteristic_pairs:
        summary = df.groupby([f"Mage1_{char1}", f"Mage2_{char2}"])["Winner"].apply(lambda x: (x == "Mage1").sum()).unstack()
        
        plt.figure(figsize=(10, 8))
        plt.xlabel(f"Mage2 {char2}", fontsize=18)
        plt.ylabel(f"Mage1 {char1}", fontsize=18)
        plt.imshow(summary, cmap="viridis", origin="lower", aspect="auto", extent=[0, 10, 0, 10])
        plt.colorbar(label="Number of Wins (Mage1)")
        plt.show()

# Define characteristic pairs to analyze
characteristic_pairs = [
    ("Control", "Control"),
    ("Focus", "Focus"),
    ("Stream", "Stream"),
    ("Physical", "Physical"),
    ("Control", "Focus"),
    ("Focus", "Stream"),
    ("Stream", "Physical"),
    ("Physical", "Control")
]

# Plot victory heatmaps for Mage1 based on characteristic pairs
plot_victory_heatmaps(df, characteristic_pairs)
