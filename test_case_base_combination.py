import itertools
import pandas as pd
import matplotlib.pyplot as plt
from mage import Mage
from battle import simulate_battle

plt.rcParams.update({"font.size": 18})

# Define statistics with their display names
stats = {
    "control": "Control",
    "focus": "Focus",
    "stream": "Stream",
    "physical_condition": "Physical"
}

# Generate all combinations of two statistics
stat_pairs = list(itertools.combinations(stats.keys(), 2))

# Generate all distributions of 10 points between two statistics
def generate_distributions(stat1, stat2):
    distributions = []
    for points in range(11):
        dist = {stat1: points, stat2: 10 - points}
        # Fill other stats with 0
        for stat in stats.keys():
            if stat not in dist:
                dist[stat] = 0
        distributions.append(dist)
    return distributions

# Simulate battles for all combinations of two stats
def evaluate_combinations():
    results = []
    for stat1, stat2 in stat_pairs:
        mage1_distributions = generate_distributions(stat1, stat2)
        mage2_distributions = generate_distributions(stat1, stat2)
        
        for dist1 in mage1_distributions:
            for dist2 in mage2_distributions:
                mage1 = Mage(**dist1)
                mage2 = Mage(**dist2)
                winner, turns = simulate_battle(mage1, mage2)
                results.append({
                    "Mage1_Stat1": stats[stat1],  # Use display name
                    "Mage1_Stat2": stats[stat2],  # Use display name
                    "Mage1_Distribution": dist1,
                    "Mage2_Distribution": dist2,
                    "Winner": winner,
                    "Turns": turns
                })
    return pd.DataFrame(results)

# Analyze and visualize the results
def analyze_combinations(df):
    # Count wins for each combination of stats
    win_counts = df.groupby(["Mage1_Stat1", "Mage1_Stat2"])["Winner"].apply(lambda x: (x == "Mage1").sum())
    win_counts = win_counts.unstack()

    # Ensure all stats are included in the heatmap, even if some combinations are missing
    win_counts = win_counts.reindex(index=stats.values(), columns=stats.values(), fill_value=0).fillna(0)

    # Plot the results as a heatmap
    plt.figure(figsize=(14, 10))  # Increased figure size for better clarity
    plt.title("Effectiveness of Stat Combinations", fontsize=20)
    plt.xticks(ticks=range(len(stats)), labels=list(stats.values()), rotation=45)
    plt.yticks(ticks=range(len(stats)), labels=list(stats.values()))
    plt.imshow(win_counts, cmap="viridis", origin="upper", aspect="auto")
    plt.colorbar(label="Number of Wins")

    # Add text annotations for each cell
    for i, stat1 in enumerate(stats.values()):
        for j, stat2 in enumerate(stats.values()):
            value = win_counts.loc[stat1, stat2]
            plt.text(j, i, f"{int(value)}", ha="center", va="center", 
                     color="white" if value > 0 else "black")

    plt.show()


# Run the test
df = evaluate_combinations()
analyze_combinations(df)
