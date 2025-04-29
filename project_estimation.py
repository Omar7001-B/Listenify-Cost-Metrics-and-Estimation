import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
import os

# Create assets directory if it doesn't exist
if not os.path.exists('assets'):
    os.makedirs('assets')

print("# React/JavaScript Project Estimation Report")
print("\n## Executive Summary")
print("\nThis report presents a detailed estimation for a React/JavaScript project requiring real-time transcription, multi-language support, and API integrations, developed by a 2-person team.\n")
print("**Key Metrics:**")
print("- **Function Points:** 304 FP")
print("- **Total LOC:** 12,160 (React/JS)")
print("- **Total Effort:** 30 person-months")
print("- **Timeline:** 15 months with 2 developers")

print("\n## 1. Function Point Analysis")
print("\n### Functional Units & Weights\n")
print("| Component | Example | Count | Weight | Total |")
print("|-----------|---------|-------|--------|-------|")
print("| External Inputs (EI) | Language selection, API keys | 18 | 4 | 72 |")
print("| External Outputs (EO) | Transcripts, AI responses | 12 | 5 | 60 |")
print("| External Inquiries (EQ) | Word definitions, translations | 10 | 4 | 40 |")
print("| Internal Files (ILF) | Saved prompts, chat history | 6 | 10 | 60 |")
print("| External Interfaces (EIF) | Gemini/GPT API calls | 5 | 7 | 35 |")
print("| **Total UFP** | | | | **267** |")

print("\n### Function Point Calculation\n")
print("The equation for Unadjusted Function Points (UFP):")
print("\nUFP = (18 × 4) + (12 × 5) + (10 × 4) + (6 × 10) + (5 × 7) = 267")

# Function Point Components Visualization
components = ['External Inputs', 'External Outputs', 'External Inquiries', 'Internal Files', 'External Interfaces']
values = [72, 60, 40, 60, 35]

plt.figure(figsize=(10, 6))
bars = plt.bar(components, values, color=sns.color_palette("muted"))
plt.xlabel('Component Type')
plt.ylabel('Function Points')
plt.title('Function Point Analysis Breakdown')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1,
            f'{height:.0f}',
            ha='center', va='bottom', fontweight='bold')

plt.savefig('assets/function_point_breakdown.png')
plt.close()

print("\n![Function Point Analysis](assets/function_point_breakdown.png)")

print("\n## 2. Complexity Adjustment\n")
print("| Factor | Rating (0–5) |")
print("|--------|-------------|")
print("| Real-time transcription | 5 |")
print("| Multi-language support | 4 |")
print("| API integrations | 5 |")
print("| User customization | 4 |")
print("| Other factors (avg) | 3 |")
print("| **Total (Sum Fi)** | **49** |")

print("\n### Adjusted Function Point Calculation\n")
print("CAF = 0.65 + (0.01 × 49) = 1.14")
print("FP = 267 × 1.14 = 304 FP")

# Complexity factors visualization
factors = ['Real-time transcription', 'Multi-language support', 'API integrations', 
           'User customization', 'Other factors (avg)']
ratings = [5, 4, 5, 4, 3]

# Create radar chart
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Calculate angle for each factor
angles = np.linspace(0, 2*np.pi, len(factors), endpoint=False).tolist()
ratings_plot = ratings.copy()
ratings_plot.append(ratings_plot[0])
angles.append(angles[0])
factors_plot = factors.copy()
factors_plot.append(factors_plot[0])

# Plot data
ax.plot(angles, ratings_plot, 'o-', linewidth=2)
ax.fill(angles, ratings_plot, alpha=0.25)
ax.set_thetagrids(np.degrees(angles[:-1]), factors_plot[:-1])
ax.set_ylim(0, 5)
ax.set_yticks([1, 2, 3, 4, 5])
ax.set_title('Complexity Factors (0-5 scale)', size=15)
ax.grid(True)

plt.tight_layout()
plt.savefig('assets/complexity_factors.png')
plt.close()

print("\n![Complexity Factors](assets/complexity_factors.png)")

print("\n## 3. LOC Estimation (React/JavaScript)\n")
print("| Language | LOC/FP | Total LOC |")
print("|----------|--------|----------|")
print("| JavaScript (React) | 40 | 12,160 |")
print("\nLOC = 304 × 40 = 12,160")

print("\n## 4. Effort & Timeline (2-Person Team)\n")
print("Assumed productivity: 400 LOC/person-month (React/JS with AI integration complexity).\n")
print("### Total effort:")
print("Effort = 12,160 / 400 = 30 person-months")
print("\n### Duration:")
print("Duration = 30 / 2 = 15 months")

# Create project timeline (Gantt chart)
phases = ['Requirements & Planning', 'Architecture Design', 'Core Framework Setup', 
          'API Integration', 'UI Development', 'Real-time Features', 
          'Multi-language Support', 'Testing & QA', 'Documentation & Deployment']

# Start and duration in months
start_times = [0, 1, 2, 3, 3, 6, 8, 11, 13]
durations = [2, 2, 2, 4, 8, 6, 4, 4, 2]

# Create DataFrame for the Gantt chart
df = pd.DataFrame({
    'Phase': phases,
    'Start': start_times,
    'Duration': durations
})

# Sort by start time
df = df.sort_values('Start')

# Plot
fig, ax = plt.subplots(figsize=(12, 7))

# Plot each phase
for i, row in df.iterrows():
    ax.barh(row['Phase'], row['Duration'], left=row['Start'], 
            color=plt.cm.tab10(i % 10), alpha=0.8, edgecolor='black')
    # Add text label in the middle of each bar
    ax.text(row['Start'] + row['Duration']/2, row['Phase'], f"{row['Duration']} months",
            ha='center', va='center', color='black', fontweight='bold')

# Customize the plot
ax.set_xlabel('Timeline (Months)')
ax.set_title('Project Development Timeline (15 Months)')
ax.set_xlim(0, 15)
ax.grid(axis='x', alpha=0.3)

plt.tight_layout()
plt.savefig('assets/project_timeline.png')
plt.close()

print("\n![Project Timeline](assets/project_timeline.png)")

print("\n## 5. Risk Mitigation Strategies\n")
print("| Risk | Mitigation Strategy |")
print("|------|---------------------|")
print("| API integration delays | Mock APIs for early development |")
print("| Real-time performance | Optimize WebSocket/SSE usage |")
print("| Scope creep | Freeze features post-MVP |")

# Risk matrix visualization
risks = ['API integration delays', 'Real-time performance', 'Scope creep', 
         'Technical debt', 'Resource availability', 'Third-party API changes']
impact = [4, 5, 3, 2, 3, 4]  # 1-5 scale
likelihood = [3, 4, 5, 3, 2, 3]  # 1-5 scale

# Create risk matrix
fig, ax = plt.subplots(figsize=(10, 8))

# Background colors for different risk zones
x = np.linspace(0.5, 5.5, 6)
y = np.linspace(0.5, 5.5, 6)
X, Y = np.meshgrid(x, y)
Z = X * Y  # Risk score = impact * likelihood

# Define risk levels
cmap = LinearSegmentedColormap.from_list('risk_cmap', ['green', 'yellow', 'orange', 'red'])

# Plot heatmap
c = ax.pcolormesh(X, Y, Z, cmap=cmap, vmin=1, vmax=25)
plt.colorbar(c, ax=ax, label='Risk Score')

# Plot risk points
scatter = ax.scatter(likelihood, impact, s=200, c='blue', edgecolor='black', zorder=5)

# Add risk labels
for i, risk in enumerate(risks):
    ax.annotate(risk, (likelihood[i], impact[i]), xytext=(7, 0), 
                textcoords='offset points', ha='left', va='center')

# Customize the plot
ax.set_xlim(0.5, 5.5)
ax.set_ylim(0.5, 5.5)
ax.set_xticks(range(1, 6))
ax.set_yticks(range(1, 6))
ax.set_xlabel('Likelihood')
ax.set_ylabel('Impact')
ax.set_title('Risk Assessment Matrix')
ax.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig('assets/risk_matrix.png')
plt.close()

print("\n![Risk Matrix](assets/risk_matrix.png)")

print("\n## 6. Summary Table\n")
print("| Metric | Value |")
print("|--------|-------|")
print("| Function Points | 304 FP |")
print("| Total LOC | 12,160 (React/JS) |")
print("| Effort | 30 person-months |")
print("| Timeline (2 devs) | 15 months |")

# Summary metrics visualization
metrics = ['Function Points', 'LOC (hundreds)', 'Effort (person-months)', 'Timeline (months)']
values = [304, 121.6, 30, 15]  # LOC in hundreds for better visualization

fig, ax = plt.subplots(figsize=(10, 6))
colors = ['#3498db', '#2ecc71', '#e74c3c', '#f39c12']
bars = ax.bar(metrics, values, color=colors)

# Add value labels
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
            f'{height:.1f}' if height != int(height) else f'{int(height)}',
            ha='center', va='bottom', fontweight='bold')

ax.set_title('Project Estimation Summary')
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('assets/summary_metrics.png')
plt.close()

print("\n![Summary Metrics](assets/summary_metrics.png)")

print("\n## 7. Optimization Possibilities\n")
print("- **UI Libraries:** Using Material-UI or other component libraries could reduce LOC by ~20%")
print("- **Team Scaling:** Adding a third developer would reduce timeline to approximately 10 months")
print("- **Phased Delivery:** Implementing core features first could allow for earlier partial deployment")

print("\n## 8. Conclusion\n")
print("This estimation provides a comprehensive analysis of the project requirements, complexity, and timeline. The 15-month development timeline reflects the comprehensive nature of the application with its real-time transcription, multi-language support, and complex API integrations.")
print("\nRegular reassessment of the project metrics is recommended as development progresses to account for any changes in requirements or technological approach.") 