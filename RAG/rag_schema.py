import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Remove the axis
ax.axis('off')

# Define box properties
box_style = dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="lightblue")

# Define the positions of the boxes
positions = {
    "User Query": (0.5, 0.9),
    "Retriever": (0.5, 0.75),
    "Retriever Embeds Query": (0.5, 0.6),
    "Search Documents/Chunks": (0.5, 0.45),
    "Retrieve Top-K Relevant Chunks": (0.5, 0.3),
    "Pass Chunks to Generator": (0.5, 0.15),
    "Generate Final Response": (0.5, 0.05)
}

# Create the boxes
for text, pos in positions.items():
    ax.text(pos[0], pos[1], text, ha="center", va="center", bbox=box_style, fontsize=12)

# Create the arrows
arrow_props = dict(facecolor='black', shrink=0.05)
for i in range(len(positions) - 1):
    start_pos = list(positions.values())[i]
    end_pos = list(positions.values())[i + 1]
    ax.annotate('', xy=end_pos, xytext=start_pos, arrowprops=dict(arrowstyle="->", lw=1.5))

# Display the flowchart
plt.title("Flowchart for RAG Model", fontsize=14)
plt.show()
