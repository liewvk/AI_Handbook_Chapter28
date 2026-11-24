record = {
    "customer_name": "Sample Person",
    "email": "sample@example.invalid",
    "order_id": "DEMO-1001",
    "quantity": 3,
    "delivery_days": 2,
}
allowed = ("order_id", "quantity", "delivery_days")
clean = {key: record[key] for key in allowed}
print(clean)
print("Email retained:", "email" in clean)

