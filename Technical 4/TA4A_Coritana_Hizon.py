# Part A: Knowledge Representation + Rule-Based Reasoning (RBR)
# Use case: Laptop troubleshooting assistant

facts = {
    "power": {
        "powers_on": True,
        "battery_level": 12,        # percent
        "is_plugged_in": False,
    },
    "thermal": {
        "temperature_c": 92,        # CPU temperature
        "fan_noise": "loud",        # "normal" or "loud"
    },
    "display": {
        "screen_on": True,
        "screen_flickering": False,
        "storage_free_gb": 3,       # included for the storage rule
    },
}

def rule_no_power(facts):
    if not facts["power"]["powers_on"] and not facts["power"]["is_plugged_in"]:
        return "Plug in the charger and check the power outlet"

def rule_low_battery(facts):
    if facts["power"]["battery_level"] < 20 and not facts["power"]["is_plugged_in"]:
        return "Battery is low - plug in the charger"

def rule_overheating(facts):
    if facts["thermal"]["temperature_c"] > 85:
        return "Close heavy programs and place the laptop on a cooling pad"

def rule_loud_fan(facts):
    if facts["thermal"]["fan_noise"] == "loud":
        return "Clean the fan and air vents from dust"

def rule_flicker(facts):
    if facts["display"]["screen_flickering"]:
        return "Update the graphics/display driver"

def rule_low_storage(facts):
    if facts["display"]["storage_free_gb"] < 10:
        return "Delete unused files or run Disk Cleanup"

# The rule base (the list the inference engine will go through)
rules = [rule_no_power, rule_low_battery, rule_overheating,
         rule_loud_fan, rule_flicker, rule_low_storage]


# Task 2B: Inference engine
def inference_engine(facts, rules):
    # Read the knowledge base, check each rule, return all inferred actions.
    actions = []                       # working memory of conclusions
    for rule in rules:                 # check every rule
        result = rule(facts)           # evaluate the IF part
        if result is not None:         # rule fired -> keep the THEN part
            actions.append(result)
    return actions


# Task 2C: Display output
if __name__ == "__main__":
    print("Knowledge Base (Facts):")
    for category, items in facts.items():
        print(f"  [{category}]")
        for name, value in items.items():
            print(f"    {name}: {value}")

    print("\nRule-Based Reasoning Actions:")
    inferred = inference_engine(facts, rules)
    if inferred:
        for action in inferred:
            print(f"- {action}")
    else:
        print("- No rule matched. No action needed.")
