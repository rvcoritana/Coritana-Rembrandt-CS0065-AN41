# Part B: Case-Based Reasoning (CBR)
# Use case: Laptop troubleshooting assistant (same domain as the RBR program)

case_base = [
    {"problem": {
        "wont_turn_on": True,
        "overheating": False,
        "loud_fan": False,
        "slow": False,
        "screen_flicker": False
        },
     "solution": "Check the power cable and charger."
     },
    {"problem": {
        "wont_turn_on": False,
        "overheating": True,
        "loud_fan": True,
        "slow": True,
        "screen_flicker": False
        },
     "solution": "Clean the fan and vents, then use a cooling pad."
     },
    {"problem": {
        "wont_turn_on": False,
        "overheating": False,
        "loud_fan": False,
        "slow": True,
        "screen_flicker": False
        },
     "solution": "Free up disk space and remove startup programs."
     },
    {"problem": {
        "wont_turn_on": False,
        "overheating": False,
        "loud_fan": False,
        "slow": False,
        "screen_flicker": True
        },
     "solution": "Update the display driver."
     },
]

FEATURES = [
    "wont_turn_on",
    "overheating",
    "loud_fan",
    "slow",
    "screen_flicker"
    ]


# Retrieve - similarity matching
def similarity(new_problem, old_problem):
    # Fraction of features that have the same value (0.0 to 1.0).
    matches = sum(1 for f in FEATURES if new_problem[f] == old_problem[f])
    return matches / len(FEATURES)

def retrieve(new_problem, case_base):
    # Return the most similar case and its score.
    best_case, best_score = None, -1
    for case in case_base:
        score = similarity(new_problem, case["problem"])
        if score > best_score:
            best_case, best_score = case, score
    return best_case, best_score


# Reuse - use the solution of the most similar case
def reuse(best_case):
    return best_case["solution"]


# Revise - let the student adjust the solution or keep it
def revise(solution):
    print(f"\nSuggested solution: {solution}")
    answer = input("Edit the solution? (type new solution or press Enter to keep): ").strip()
    return answer if answer else solution


# Retain - store the new case in the case base
def retain(new_problem, final_solution, case_base):
    case_base.append({"problem": new_problem, "solution": final_solution})
    print(f"Case retained. Case base now has {len(case_base)} cases.")


def get_yes_no(prompt):
    # Keep asking until the user enters a valid yes/no answer
    while True:
        answer = input(prompt).strip().lower()
        if answer in ["y", "yes"]:
            return True
        elif answer in ["n", "no"]:
            return False
        else:
            print("Invalid input! Please enter 'y' or 'n'.")


def ask_problem():
    # Input: ask the user yes/no questions to build the new problem.
    print("Describe your laptop problem (y/n):")
    problem = {}
    for f in FEATURES:
        problem[f] = get_yes_no(f"  {f.replace('_', ' ')}? ")
    return problem

def main():
    print("=== Case-Based Reasoning: Laptop Troubleshooter ===\n")
    new_problem = ask_problem()

    best_case, score = retrieve(new_problem, case_base)
    print(f"\nMost similar case found (similarity: {score:.0%}):")
    print(f"  Problem : {best_case['problem']}")

    solution = reuse(best_case)
    final_solution = revise(solution)
    retain(new_problem, final_solution, case_base)

    print(f"\nFinal solution: {final_solution}")

if __name__ == "__main__":
    main()
