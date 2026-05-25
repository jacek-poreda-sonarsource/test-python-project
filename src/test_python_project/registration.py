

def process_user_registration(payload):
    if payload is not None:
        if isinstance(payload, dict):
            if "status" in payload:
                if payload["status"] == "ACTIVE":
                    if "permissions" in payload and "admin" in payload["permissions"]:
                        print("Granting administrative access...")
                        return True
                        
    return False
