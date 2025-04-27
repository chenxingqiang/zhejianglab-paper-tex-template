#!/usr/bin/env python3
"""
Generate visualization for generalization capabilities
of AdaptDifficulty across different reasoning tasks for the Zhejianglab paper.
"""

import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib.ticker import MultipleLocator

# Create directory if it doesn't exist
os.makedirs('output', exist_ok=True)

# Set style for academic paper - clean, professional style with black outlines
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 12,
    'xtick.labelsize': 11,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.figsize': (8, 6),
    'lines.linewidth': 1.5,
    'patch.linewidth': 1,
    'legend.frameon': True,
    'legend.framealpha': 1.0,
})

# Data for bar chart - using a more typical academic chart style instead of radar
# Format: [AdaptDifficulty, Static Distribution, Manual Curriculum, Difficulty-Based]
categories = ['Step Accuracy', 'Conceptual Correctness', 'Path Optimality', 'Error Recovery']

# Data matching the example figure
adapt_difficulty = [78.3, 82.4, 67.8, 52.1]  # Pattern filled in example
static_distribution = [68.5, 73.2, 54.3, 31.8]  # Red in example
manual_curriculum = [71.4, 75.8, 58.9, 35.2]  # Black in example 
difficulty_based = [74.7, 78.3, 62.5, 41.3]  # Green in example

# Create the figure
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# Set width and positions for bars
bar_width = 0.2
x = np.arange(len(categories))
positions = [x - 1.5*bar_width, x - 0.5*bar_width, x + 0.5*bar_width, x + 1.5*bar_width]

# Create bars with hatching patterns similar to example figure
bar1 = ax.bar(positions[0], adapt_difficulty, width=bar_width, edgecolor='black', 
              label='AdaptDifficulty', color='white', hatch='////', linewidth=1)
bar2 = ax.bar(positions[1], static_distribution, width=bar_width, edgecolor='black',
              label='Static Distribution', color='#ff9999', linewidth=1) 
bar3 = ax.bar(positions[2], manual_curriculum, width=bar_width, edgecolor='black',
              label='Manual Curriculum', color='#bbbbbb', linewidth=1)
bar4 = ax.bar(positions[3], difficulty_based, width=bar_width, edgecolor='black', 
              label='Difficulty-Based', color='#99cc99', linewidth=1)

# Add data labels on top of each bar
def add_labels(bars):
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 2),  # Small vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8)

add_labels(bar1)
add_labels(bar2)
add_labels(bar3)
add_labels(bar4)

# Set axis labels and limits
ax.set_ylabel('Score (%)')
ax.set_ylim(0, 90)  # Similar to the example
ax.set_xticks(x)
ax.set_xticklabels(categories)

# Add black frame around the plot
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1.0)

# Configure y-axis ticks and grid
ax.yaxis.set_major_locator(MultipleLocator(20))
ax.yaxis.grid(True, linestyle='-', alpha=0.2)

# Add legend below the chart, similar to example
ax.legend(ncol=4, loc='upper center', bbox_to_anchor=(0.5, -0.08), frameon=False, handlelength=2.5)

# Title below the figure like in the example
# fig.text(0.5, 0.01, 'Figure 4: Analysis of reasoning quality across different training approaches.', 
#          ha='center', va='bottom', fontsize=11)

# Tight layout with space for the title
plt.tight_layout(rect=[0, 0.07, 1, 1])

# Save figure
plt.savefig('output/generalization_capabilities.png', dpi=300, bbox_inches='tight')
plt.savefig('generalization_capabilities.png', dpi=300, bbox_inches='tight')
plt.close()

print("Generalization capabilities visualization generated successfully.")
