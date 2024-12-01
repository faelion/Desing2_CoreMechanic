import pandas as pd
import matplotlib.pyplot as plt
from mage import Mage
from battle import simulate_battle

# Set global font size
plt.rcParams.update({"font.size": 18})

# Create specialized mages with 10 points in each characteristic
def create_specialized_mages():
    return {
        "Control": Mage(control=10, focus=0, stream=0, physical_condition=0),
        "Focus": Mage(control=0, focus=10, stream=0, physical_condition=0),
        "Stream": Mage(control=0, focus=0, stream=10, physical_condition=0),
        "Physical": Mage(control=0, focus=0, stream=0, physical_condition=10)
    }

# Simulate battles between mages and track metrics
def evaluate_characteristics():
    specialized_mages = create_specialized_mages()
    stats = ["Control", "Focus", "Stream", "Physical"]
    
    metrics = []
    
    for stat1, mage1 in specialized_mages.items():
        for stat2, mage2 in specialized_mages.items():
            if stat1 != stat2:
                winner, turns = simulate_battle(mage1, mage2)
                
                # Record key metrics
                metrics.append({
                    "Mage1_Stat": stat1,
                    "Mage2_Stat": stat2,
                    "Winner": winner,
                    "Turns": turns,
                    "Mage1_Health_Remaining": mage1.health,
                    "Mage2_Health_Remaining": mage2.health,
                    "Mage1_Damage_Inflicted": mage2.health - 50,  # Starting health is 50
                    "Mage2_Damage_Inflicted": mage1.health - 50  # Starting health is 50
                })
    
    return pd.DataFrame(metrics)

# Analyze and visualize the results
def analyze_characteristics(df):
    # Calculate average metrics for each characteristic
    summary = df.groupby("Mage1_Stat").agg({
        "Turns": "mean",
        "Mage1_Health_Remaining": "mean",
        "Mage1_Damage_Inflicted": "mean"
    }).rename(columns={
        "Turns": "Avg_Turns",
        "Mage1_Health_Remaining": "Avg_Health_Remaining",
        "Mage1_Damage_Inflicted": "Avg_Damage_Inflicted"
    })
    
    # Plot metrics
    fig, axes = plt.subplots(3, 1, figsize=(16, 24))  # Larger size for better clarity
    plt.tight_layout()  # Automatically adjust spacing
    
    # Titles and labels
    axes[0].set_title("Average Turns per Characteristic")
    axes[0].set_ylabel("Turns")
    summary["Avg_Turns"].plot(kind="bar", ax=axes[0], color="skyblue")
    axes[0].tick_params(axis='x', rotation=45)  # Rotate x-axis labels

    axes[1].set_title("Average Health Remaining")
    axes[1].set_ylabel("Health")
    summary["Avg_Health_Remaining"].plot(kind="bar", ax=axes[1], color="lightgreen")
    axes[1].tick_params(axis='x', rotation=45)

    axes[2].set_title("Average Damage Inflicted")
    axes[2].set_ylabel("Damage")
    summary["Avg_Damage_Inflicted"].plot(kind="bar", ax=axes[2], color="salmon")
    axes[2].tick_params(axis='x', rotation=45)

    # Adjust spacing manually if tight_layout isn't enough
    fig.subplots_adjust(hspace=0.6, top=0.95)  # Ensure enough space between plots
    plt.show()

# Run the test
df = evaluate_characteristics()
analyze_characteristics(df)
