checks = {
    "Defined intended use": True,
    "Approved data sources": True,
    "Subgroup evaluation": False,
    "Validated outputs": True,
    "Human approval for sensitive actions": False,
    "Documented incident response": True,
}
for label, passed in checks.items():
    print(("PASS" if passed else "REVIEW") + ": " + label)
print("Ready for release:", all(checks.values()))

