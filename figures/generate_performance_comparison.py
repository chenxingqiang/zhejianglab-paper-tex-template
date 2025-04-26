#!/usr/bin/env python3
"""
Generate visualization for performance comparison between 
AdaptDifficulty and other training approaches for the Zhejianglab paper.
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

# Data
categories = ['Training Time', 'BeyondAIME', 'Codeforces', 'GPQA', 'Generalization']
adapt_difficulty = [23.1, 18.5, 16.8, 14.2, 19.7]  # Performance improvements in %
static_curriculum = [12.4, 10.3, 9.7, 8.5, 11.2]  # Performance improvements in %
manual_curriculum = [14.7, 12.8, 11.5, 9.8, 13.0]  # Additional data for completeness
difficulty_based = [17.5, 14.0, 13.2, 10.5, 15.3]   # Additional data for completeness

# Set width of bars
barWidth = 0.2
x = np.arange(len(categories))

# Create the figure
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# Set width and positions for bars
x = np.arange(len(categories))
positions = [x - 1.5*barWidth, x - 0.5*barWidth, x + 0.5*barWidth, x + 1.5*barWidth]

# Create bars with hatching patterns similar to the generalization figure
bar1 = ax.bar(positions[0], adapt_difficulty, width=barWidth, edgecolor='black', 
              label='AdaptDifficulty', color='white', hatch='////', linewidth=1)
bar2 = ax.bar(positions[1], static_curriculum, width=barWidth, edgecolor='black',
              label='Static Distribution', color='#ff9999', linewidth=1) 
bar3 = ax.bar(positions[2], manual_curriculum, width=barWidth, edgecolor='black',
              label='Manual Curriculum', color='#bbbbbb', linewidth=1)
bar4 = ax.bar(positions[3], difficulty_based, width=barWidth, edgecolor='black', 
              label='Difficulty-Based', color='#99cc99', linewidth=1)

# Add data labels on top of bars
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

# Add clear black frame around the plot
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1.0)

# Customize axes and labels
ax.set_ylabel('Improvement (%)', fontweight='normal')
ax.set_xticks(x)
ax.set_xticklabels(categories)

# Set axis labels and limits
ax.set_ylim(0, 30)  # Similar to the example

# Configure y-axis ticks and grid
ax.yaxis.set_major_locator(MultipleLocator(10))
ax.yaxis.grid(True, linestyle='-', alpha=0.2)

# Add legend below the chart, similar to example
ax.legend(ncol=4, loc='upper center', bbox_to_anchor=(0.5, -0.08), frameon=False, handlelength=2.5)

# Optional annotation for key insight
ax.annotate('AdaptDifficulty consistently\noutperforms static methods', 
            xy=(1, adapt_difficulty[1]), xytext=(2, 25),
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
            fontsize=9)

# Title below the figure like in the example
fig.text(0.5, 0.01, 'Figure 1: Performance improvements of different training approaches across metrics.', 
         ha='center', va='bottom', fontsize=11)

# Tight layout with space for the title
plt.tight_layout(rect=[0, 0.07, 1, 1])

# Save figure
plt.savefig('output/performance_comparison.png', dpi=300, bbox_inches='tight')
plt.savefig('performance_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

print("Performance comparison visualization generated successfully.")
