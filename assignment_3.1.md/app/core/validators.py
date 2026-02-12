def validate_age(age):
    return age >= 18

def validate_password(password):
    return len(password) >= 8

def validate_terms(terms_input):
    normalized = terms_input.strip().lower()
    return normalized.startswith("y")
