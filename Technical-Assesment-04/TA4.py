# ==============================================================================
# PART 1 — Knowledge Representation (KR) Setup
# ==============================================================================

knowledge_base = {
    "temperature": 34,
    "is_raining": True,
    "power_connected": True,
    "humidity": 88,
    "ambient_light": 150
}


# ==============================================================================
# PART 2 — Implement Rule-Based Reasoning (RBR)
# ==============================================================================

def rule_heat_warning(facts):
    if facts["temperature"] > 30:
        return "Turn on the air conditioner"
    return None

def rule_rain_advisory(facts):
    if facts["is_raining"]:
        return "Bring an umbrella before going outside"
    return None

def rule_dehumidifier(facts):
    if facts["humidity"] > 80 and facts["power_connected"]:
        return "Activate the dehumidifier"
    return None


def run_inference_engine(facts, rules):
    inferred_actions = []
    
    for rule in rules:
        action = rule(facts)
        if action:
            inferred_actions.append(action)
            
    return inferred_actions


# ==============================================================================
# PART 3 — Implement Case-Based Reasoning (CBR)
# ==============================================================================

case_base = [
    {
        "id": "Case 1",
        "problem": {"temperature_high": True, "humidity_high": False, "is_raining": False},
        "solution": "Set AC mode to Cool."
    },
    {
        "id": "Case 2",
        "problem": {"temperature_high": True, "humidity_high": True, "is_raining": True},
        "solution": "Set AC mode to Dry and close all windows."
    },
    {
        "id": "Case 3",
        "problem": {"temperature_high": False, "humidity_high": True, "is_raining": True},
        "solution": "Turn on ventilation fan and keep windows shut."
    }
]

def calculate_similarity(new_case_features, existing_case_features):
    matches = 0
    total_features = len(new_case_features)
    
    for feature, value in new_case_features.items():
        if feature in existing_case_features and existing_case_features[feature] == value:
            matches += 1
            
    return matches / total_features if total_features > 0 else 0

def retrieve_best_case(new_problem, cases):
    best_case = None
    highest_similarity = -1.0
    
    for case in cases:
        sim_score = calculate_similarity(new_problem, case["problem"])
        if sim_score > highest_similarity:
            highest_similarity = sim_score
            best_case = case
            
    return best_case, highest_similarity

def reuse_solution(best_case):
    return best_case["solution"]

def revise_solution(suggested_solution):
    print(f"\n[CBR - Revise Step] Retried Solution: '{suggested_solution}'")
    user_input = input("Would you like to modify this solution? (yes/no): ").strip().lower()
    
    if user_input == 'yes':
        new_solution = input("Enter the revised solution: ").strip()
        return new_solution
    else:
        print("Solution accepted unchanged.")
        return suggested_solution

def retain_case(cases, problem_features, final_solution):
    new_case_id = f"Case {len(cases) + 1}"
    new_entry = {
        "id": new_case_id,
        "problem": problem_features,
        "solution": final_solution
    }
    cases.append(new_entry)
    print(f"[CBR - Retain Step] New case saved as '{new_case_id}' in Case Base.")


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("         PART 2: RULE-BASED REASONING (RBR) EXECUTION")
    print("=" * 60)
    
    rules_list = [rule_heat_warning, rule_rain_advisory, rule_dehumidifier]
    
    inferred_actions = run_inference_engine(knowledge_base, rules_list)
    
    print("Rule-Based Reasoning Actions:")
    for action in inferred_actions:
        print(f" - {action}")
        
    print("\n" + "=" * 60)
    print("         PART 3: CASE-BASED REASONING (CBR) EXECUTION")
    print("=" * 60)
    
    new_problem = {
        "temperature_high": True,
        "humidity_high": True,
        "is_raining": False
    }
    
    print(f"Target Problem Features: {new_problem}\n")
    
    best_case, sim_score = retrieve_best_case(new_problem, case_base)
    print(f"[CBR - Retrieve Step] Matched {best_case['id']} with {sim_score * 100:.1f}% similarity.")
    
    suggested_solution = reuse_solution(best_case)
    print(f"[CBR - Reuse Step] Suggested Solution: {suggested_solution}")
    
    final_solution = revise_solution(suggested_solution)
    print(f"\nFinal Confirmed Solution: {final_solution}")
    
    retain_case(case_base, new_problem, final_solution)
    
    print("\nUpdated Case Base Size:", len(case_base))