ALLOWED_TOOLS = {"lookup_order", "calculate_total"}

def authorize(tool_name, approved=False):
    if tool_name not in ALLOWED_TOOLS:
        return "BLOCKED: unknown or restricted tool"
    if tool_name == "calculate_total" and not approved:
        return "APPROVAL REQUIRED"
    return "ALLOWED"

print(authorize("lookup_order"))
print(authorize("delete_customer_data"))
print(authorize("calculate_total", approved=True))

