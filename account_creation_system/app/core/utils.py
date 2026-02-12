def extract_domain(email):
    if email.count("@") != 1:
        return None

    parts = email.split("@")
    domain = parts[1]
    return domain
