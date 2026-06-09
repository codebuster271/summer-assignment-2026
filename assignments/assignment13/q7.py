import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
from pathlib import Path


semesters = ["Sem 1", "Sem 2", "Sem 3", "Sem 4"]
semester_1 = [72, 76, 79, 83]
semester_2 = [68, 74, 81, 86]

plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(semesters, semester_1, marker="o", linewidth=2.5, label="Semester 1")
ax.plot(semesters, semester_2, marker="s", linewidth=2.5, label="Semester 2")

ax.set_title("Semester Result Comparison")
ax.set_xlabel("Semester")
ax.set_ylabel("Marks")
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend()

plt.tight_layout()
output_path = Path(__file__).with_name("semester_result_comparison.png")
plt.savefig(output_path, dpi=150)
print(f"Chart saved to {output_path}")
