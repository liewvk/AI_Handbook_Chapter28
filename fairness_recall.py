groups = {
    "Group A": {"tp": 18, "fn": 2},
    "Group B": {"tp": 12, "fn": 8},
}
recalls = {}
for name, counts in groups.items():
    tp, fn = counts["tp"], counts["fn"]
    recalls[name] = tp / (tp + fn)
    print(f"{name} recall: {recalls[name]:.2f}")
gap = abs(recalls["Group A"] - recalls["Group B"])
print(f"Absolute recall gap: {gap:.2f}")

