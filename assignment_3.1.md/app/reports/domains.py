from app.core.utils import extract_domain

def show_domain_report(users):
    print("\n=== EMAIL DOMAIN REPORT ===")

    if len(users) == 0:
        print("No users registered")
        return

    domain_counts = {}

    for user in users:
        domain = extract_domain(user["email"])
        if domain is None:
            continue
        domain_counts[domain] = domain_counts.get(domain, 0) + 1

    for domain in domain_counts:
        print(domain + ":", domain_counts[domain])
