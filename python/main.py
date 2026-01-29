# TODO: add constant REACTION_TIME = 1.2
REACTION_TIME = 1.2
KG_PER_TON = 1000

def power_to_weight(power_kw, mass_kg):
    return power_kw / (mass_kg / KG_PER_TON)

def classify_performance(p2w_rounded):
    if p2w_rounded < 60:
        return "Weak"
    elif p2w_rounded < 100:
        return "Average"
    else:
        return "Strong"

def evaluate_overtaking(own_speed, target_speed, distance_available):
    cond_a = own_speed > target_speed
    cond_b = (own_speed - target_speed) >= 20
    cond_c = distance_available >= 100
    overtaking_safe = (cond_a and cond_b) and cond_c
    return cond_a, cond_b, cond_c, overtaking_safe

def kmh_to_ms(speed_kmh):
    return (speed_kmh * 1000) / 3600

def kmh_to_ms(speed_kmh):
    return speed_kmh / 3.6

def braking_distance(speed_kmh, friction):
    v = kmh_to_ms(speed_kmh)
    g = 9.81
    distance = (v ** 2) / (2 * friction * g)
    return distance
# TODO: create function reaction_distance(speed_kmh, reaction_time)
def reaction_distance(speed_kmh, reaction_time):
    v = kmh_to_ms(speed_kmh)
    distance = v * reaction_time
    return distance
# TODO: create function total_stopping_distance(speed_kmh, friction, reaction_time)
def total_stopping_distance(speed_kmh, friction, reaction_time):
    react_dist = reaction_distance(speed_kmh, reaction_time)
    brake_dist = braking_distance(speed_kmh, friction)
    total = react_dist + brake_dist
    return react_dist, brake_dist, total

def performance_class(p2w):
    if p2w > 100:
        return "Strong"
    elif p2w > 60:
        return "Medium"
    else:
        return "Weak"

def print_report(power_kw, mass_kg, p2w_rounded, performance,
                 cond_a, cond_b, cond_c, overtaking,
                 dry_dist, wet_dist, snow_dist,
                 reaction_dist, braking_dist_dry, total_stop, is_safe):

    print("\n=== PERFORMANCE REPORT ===")
    print(f"{'Parameter':<25}{'Value'}")
    print("-" * 40)
    print(f"{'Engine Power (kW):':<25}{power_kw}")
    print(f"{'Vehicle Mass (kg):':<25}{mass_kg}")
    print(f"{'Power-to-weight:':<25}{p2w_rounded}")
    print(f"{'Performance class:':<25}{performance}")

    print("\n=== OVERTAKING CHECK ===")
    print(f"{'Condition A (faster)':<25}{cond_a}")
    print(f"{'Condition B (>= 20 km/h)':<25}{cond_b}")
    print(f"{'Condition C (>= 100 m)':<25}{cond_c}")
    print(f"{'Overtaking safe':<25}{overtaking}")

    print("\n=== BRAKING DISTANCE ===")
    print(f"{'Surface':<25}{'Distance (m)'}")
    print("-" * 40)
    print(f"{'Dry asphalt (μ=0.90)':<25}{dry_dist}")
    print(f"{'Wet asphalt (μ=0.45)':<25}{wet_dist}")
    print(f"{'Snow/Ice (μ=0.20)':<25}{snow_dist}")
# TODO: extend print_report() to print REACTION & TOTAL STOPPING section
    print("\n=== REACTION & TOTAL STOPPING ===")
    print(f"{'Reaction time (s)':<30} {REACTION_TIME:>10.1f}")
    print(f"{'Reaction distance (m)':<30} {reaction_dist:>10.1f}")
    print(f"{'Braking distance (dry)':<30} {braking_dist_dry:>10.1f}")
    print(f"{'Total stopping (dry)':<30} {total_stop:>10.1f}")
    print(f"{'Stops within 70 m?':<30} {str(is_safe):>10}")


def main():
    power_kw = float(input("power (kW): "))
    mass_kg = float(input("mass (kg): "))
    own_speed = float(input("Own (km/h): "))
    target_speed = float(input("target (km/h): "))
    available_distance = float(input("distance (m): "))
    speed_for_braking = float(input("braking test speed (km/h): "))

    p2w = power_kw / (mass_kg / 1000)
    p2w_rounded = round(p2w, 1)
    performance = performance_class(p2w_rounded)

    cond_a = own_speed > target_speed
    cond_b = (own_speed - target_speed) >= 20
    cond_c = available_distance >= 100
    overtaking = cond_a and cond_b and cond_c

    dry_dist = round(braking_distance(speed_for_braking, 0.9), 1)
    wet_dist = round(braking_distance(speed_for_braking, 0.45), 1)
    snow_dist = round(braking_distance(speed_for_braking, 0.2), 1)

    reaction_dist, braking_dist_dry, total_stop = total_stopping_distance(
        speed_for_braking, 0.9, REACTION_TIME
    )

    reaction_dist = round(reaction_dist, 1)
    braking_dist_dry = round(braking_dist_dry, 1)
    total_stop = round(total_stop, 1)
# TODO: create boolean check: is_safe = total_stop < 70
    is_safe = total_stop < 70

    print_report(power_kw, mass_kg, p2w_rounded, performance,
                 cond_a, cond_b, cond_c, overtaking,
                 dry_dist, wet_dist, snow_dist,
                 reaction_dist, braking_dist_dry, total_stop, is_safe)

if __name__ == "__main__":
    main()
