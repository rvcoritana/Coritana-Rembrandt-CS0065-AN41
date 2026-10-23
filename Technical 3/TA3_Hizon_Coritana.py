import math

case_base = [
    {
        "name": "Typhoon Ursula (2019)",
        "problem": {
            "type": "typhoon",
            "area": "urban",
            "population": 120000
            },
        "solution": {
            "strategy": "Evacuate low-lying barangays to schools and gyms",
            "evacuee_percent": 0.30, 
            "shelter_capacity": 400
            },
    },
    {
        "name": "Typhoon Odette (2021)",
        "problem": {
            "type": "typhoon", 
            "area": "coastal", 
            "population": 250000
            },
        "solution": {
            "strategy": "Move coastal residents to inland shelters",
            "evacuee_percent": 0.45, 
            "shelter_capacity": 350
            },
    },
    {
        "name": "Metro Flood (2012)",
        "problem": {
            "type": "flood", 
            "area": "urban", 
            "population": 300000
            },
        "solution": {
            "strategy": "Evacuate riverside communities and use boats",
            "evacuee_percent": 0.25, 
            "shelter_capacity": 450
            },
    },
    {
        "name": "Bohol Earthquake (2013)",
        "problem": {
            "type": "earthquake", 
            "area": "rural", 
            "population": 80000
            },
        "solution": {
            "strategy": "Move residents to open ground and set up tents",
            "evacuee_percent": 0.40, 
            "shelter_capacity": 250
            },
    },
]

# ---------------------------------------------------------------
def similarity(new, old):
    score = 0.0
    # Same disaster type is the most important (weight 0.5)
    if new["type"] == old["type"]:
        score += 0.5

    # Same area type (weight 0.3)
    if new["area"] == old["area"]:
        score += 0.3

    score += 0.2 * min(new["population"], old["population"]) / max(new["population"], old["population"])
    return score

def adapt(new, old_case):
    old = old_case["solution"]
    evacuees = round(new["population"] * old["evacuee_percent"])
    shelters = math.ceil(evacuees / old["shelter_capacity"])
    strategy = old["strategy"]

    # Urban flooding needs extra measures
    if new["area"] == "urban":
        strategy += "; add vertical evacuation and rescue boats"
    return {"strategy": strategy, "evacuee_percent": old["evacuee_percent"],
            "shelter_capacity": old["shelter_capacity"],
            "evacuees": evacuees, "shelters_needed": shelters}

# ---------------------------------------------------------------
def main():
    new_problem = {
        "type": "typhoon", 
        "area": "urban", 
        "population": 200000
        }

    print("=== CBR DISASTER RESPONSE SYSTEM ===")
    print("\nNEW PROBLEM: Typhoon with expected flooding in an urban area")
    print(f"  Type: {new_problem['type']}, Area: {new_problem['area']}, "
          f"Population: {new_problem['population']:,}")

    # RETRIEVE
    print("\nSIMILARITY SCORES:")
    ranked = sorted(case_base, key=lambda c: similarity(new_problem, c["problem"]), reverse=True)
    for i, c in enumerate(ranked, 1):
        print(f"  {i}. {c['name']:<26} {similarity(new_problem, c['problem']):.2f}")
    best = ranked[0]
    print(f"\nMOST SIMILAR CASE: {best['name']}")
    print(f"  Old strategy: {best['solution']['strategy']}")

    # REUSE
    final = adapt(new_problem, best)
    print("\nADAPTED FINAL SOLUTION:")
    print(f"  Strategy : {final['strategy']}")
    print(f"  Evacuees : {final['evacuees']:,} ({final['evacuee_percent']:.0%} of population)")
    print(f"  Shelters : {final['shelters_needed']} (capacity {final['shelter_capacity']} each)")

    # RETAIN
    case_base.append({"name": "Typhoon New Event (2025)",
                      "problem": new_problem, "solution": final})
    print("\nNew case saved!")
    print("\nUPDATED CASE BASE:")
    for i, c in enumerate(case_base, 1):
        print(f"  {i}. {c['name']}")

if __name__ == "__main__":
    main()
