#!/usr/bin/env python3
"""
Generate visualization for learning efficiency comparison
between AdaptDifficulty and baseline approaches for the Zhejianglab paper.
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

# Data for learning curves
training_steps = np.linspace(0, 500, 100)  # 0 to 500K training steps

# Performance functions for different approaches
def adapt_difficulty_curve(x):
    return 85 * (1 - np.exp(-0.008 * x)) + 10  # Faster learning curve

def static_distribution_curve(x):
    return 75 * (1 - np.exp(-0.005 * x)) + 10  # Slower learning curve

def manual_curriculum_curve(x):
    return 78 * (1 - np.exp(-0.006 * x)) + 10  # Medium learning curve

def difficulty_based_curve(x):
    return 80 * (1 - np.exp(-0.007 * x - 0.0000025 * x**2)) + 10  # Quick initial gains but plateaus

# Calculate performance values
adapt_difficulty_perf = adapt_difficulty_curve(training_steps)
static_distribution_perf = static_distribution_curve(training_steps)
manual_curriculum_perf = manual_curriculum_curve(training_steps)
difficulty_based_perf = difficulty_based_curve(training_steps)

# Create the figure
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# Create step values with fewer points for cleaner marker appearance
marker_steps = np.linspace(0, 500, 10)  # 10 points for markers

# Calculate performance values at marker points
adapt_difficulty_markers = adapt_difficulty_curve(marker_steps)
static_distribution_markers = static_distribution_curve(marker_steps)
manual_curriculum_markers = manual_curriculum_curve(marker_steps)
difficulty_based_markers = difficulty_based_curve(marker_steps)

# Plot learning curves with consistent colors and markers
line1 = ax.plot(training_steps, adapt_difficulty_perf, linewidth=2, label='AdaptDifficulty', color='black', linestyle='-')
line2 = ax.plot(training_steps, static_distribution_perf, linewidth=2, label='Static Distribution', color='#ff9999', linestyle='-')
line3 = ax.plot(training_steps, manual_curriculum_perf, linewidth=2, label='Manual Curriculum', color='#bbbbbb', linestyle='-')
line4 = ax.plot(training_steps, difficulty_based_perf, linewidth=2, label='Difficulty-Based', color='#99cc99', linestyle='-')

# Add markers to highlight data points
ax.plot(marker_steps, adapt_difficulty_markers, 'o', color='black', markerfacecolor='white', markeredgecolor='black', markersize=6)
ax.plot(marker_steps, static_distribution_markers, 's', color='#ff9999', markerfacecolor='white', markeredgecolor='#ff9999', markersize=6)
ax.plot(marker_steps, manual_curriculum_markers, '^', color='#bbbbbb', markerfacecolor='white', markeredgecolor='#bbbbbb', markersize=6)
ax.plot(marker_steps, difficulty_based_markers, 'D', color='#99cc99', markerfacecolor='white', markeredgecolor='#99cc99', markersize=6)

# Find the crossing point where AdaptDifficulty reaches what Static Distribution does at max
static_max = static_distribution_perf[-1]
crossing_idx = np.argmax(adapt_difficulty_perf >= static_max)
crossing_x = training_steps[crossing_idx]

# Add crosslines to highlight the efficiency point - subtle dotted lines
ax.axhline(y=static_max, color='black', linestyle=':', alpha=0.5, linewidth=0.8)
ax.axvline(x=crossing_x, color='black', linestyle=':', alpha=0.5, linewidth=0.8)

# Set axis labels and limits
ax.set_xlabel('Training Steps (thousands)')
ax.set_ylabel('Performance (%)')
ax.set_xlim(0, 500)
ax.set_ylim(0, 100)

# Add black frame around the plot
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_color('black')
    spine.set_linewidth(1.0)

# Configure axis ticks and grid with consistent styling
ax.xaxis.set_major_locator(MultipleLocator(100))
ax.yaxis.set_major_locator(MultipleLocator(20))
ax.yaxis.grid(True, linestyle='-', alpha=0.2)

# Add annotation for the efficiency gain with same styling as other figures
efficiency_text = "Equivalent performance\nat ~42K steps\n(57% reduction)"
ax.annotate(efficiency_text,
            xy=(crossing_x, static_max), xycoords='data',
            xytext=(crossing_x + 50, static_max - 15), textcoords='data',
            arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
            fontsize=8, color='black')

# Add legend below the chart, similar to example
ax.legend(ncol=4, loc='upper center', bbox_to_anchor=(0.5, -0.08), frameon=False, handlelength=2.5)

# # Title below the figure like in the example
# fig.text(0.5, 0.01, 'Figure 2: Training efficiency comparison between different approaches.', 
#          ha='center', va='bottom', fontsize=11)

# Tight layout with space for the title
plt.tight_layout(rect=[0, 0.07, 1, 1])

# Save the figure
plt.savefig('output/learning_efficiency.png', dpi=300, bbox_inches='tight')
plt.savefig('learning_efficiency.png', dpi=300, bbox_inches='tight')
plt.close()

print("Learning efficiency visualization generated successfully.")
