"""Assignment 13 - Question 7."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt


def main():
	semesters = ["Sem 1", "Sem 2", "Sem 3", "Sem 4"]
	semester_1 = [72, 76, 79, 83]
	semester_2 = [68, 74, 81, 86]

	plt.style.use("seaborn-v0_8")
	fig, ax = plt.subplots(figsize=(8.5, 5.5))

	ax.plot(semesters, semester_1, marker="o", linewidth=2.4, label="Semester 1")
	ax.plot(semesters, semester_2, marker="s", linewidth=2.4, label="Semester 2")

	ax.set_title("Semester Result Comparison", fontsize=14, fontweight="bold")
	ax.set_xlabel("Semester")
	ax.set_ylabel("Marks")
	ax.set_ylim(60, 90)
	ax.grid(True, linestyle="--", alpha=0.35)
	ax.legend(frameon=False)

	plt.tight_layout()
	output_path = Path(__file__).with_name("semester_result_comparison.png")
	plt.savefig(output_path, dpi=150)
	plt.close(fig)
	print(f"Chart saved to {output_path}")


if __name__ == "__main__":
	main()
