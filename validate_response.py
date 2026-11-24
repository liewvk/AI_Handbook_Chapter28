def validate(result):
    if not isinstance(result, dict):
        return False
    categories = {"billing", "technical", "general"}
    category = result.get("category")
    confidence = result.get("confidence")
    return (category in categories and
            type(confidence) in (int, float) and
            0 <= confidence <= 1)

samples = [
    {"category": "technical", "confidence": 0.91},
    {"category": "other", "confidence": 1.20},
]
for item in samples:
    print(validate(item))

