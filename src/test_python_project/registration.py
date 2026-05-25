

def process_user_registration(payload):
    if (payload is not None and isinstance(payload, dict)
            and "status" in payload and payload["status"] == "ACTIVE"
            and "permissions" in payload and "admin" in payload["permissions"]):
        print("Granting administrative access...")
        return True

    return False
