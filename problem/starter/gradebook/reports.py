"""gradebook.reports — build a printable report from grade records."""

# TODO: use a RELATIVE import to pull from the sibling stats module.
# from .stats import average_per_student, subjects_offered, top_scorer, passing_students

from typing import List
from .stats import average_per_student, subjects_offered, top_scorer, passing_students

def format_report(records: List[dict]) -> str:
    """
    Build a human-readable, multi-line report using the functions in stats.py.
    """
    total_records = len(records)
    subjects = sorted(subjects_offered(records))
    averages = average_per_student(records)
    top_name, top_avg = top_scorer(records)
    passing = passing_students(records)

    lines = []
    lines.append("=== Gradebook Report ===")
    lines.append(f"Total records: {total_records}")
    lines.append(f"Subjects offered: {', '.join(subjects)}\n")

    lines.append("Averages:")
    for name in sorted(averages.keys()):
        lines.append(f"  {name:<7}: {averages[name]}")

    lines.append(f"\nTop scorer: {top_name} ({top_avg})")
    lines.append(f"Passing students (>= 60.0): {', '.join(passing)}")

    return "\n".join(lines)


