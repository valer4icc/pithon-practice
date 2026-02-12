def show_statistics(users):
    print("\n=== USER STATISTICS ===")

    if len(users) == 0:
        print("No users registered")
        return

    ages = [user["age"] for user in users]

    youngest = min(ages)
    oldest = max(ages)
    average = sum(ages) / len(ages)

    print("Successful registrations:", len(users))
    print("Youngest age:", youngest)
    print("Oldest age:", oldest)
    print("Average age:", round(average, 1))
