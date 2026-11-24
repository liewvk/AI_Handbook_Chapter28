risks = [
    ("Private data disclosure", 3, 5),
    ("Wrong invoice total", 2, 4),
    ("Minor formatting error", 3, 1),
]
ranked = sorted(
    ((name, likelihood * impact) for name, likelihood, impact in risks),
    key=lambda item: item[1], reverse=True)
for name, score in ranked:
    print(f"{name}: {score}")

