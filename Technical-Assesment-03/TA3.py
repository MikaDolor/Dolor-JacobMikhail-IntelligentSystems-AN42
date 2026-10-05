import json

# ------------------------------------------------------------------------------
# 3. DEFINE YOUR CASE BASE
# ------------------------------------------------------------------------------
case_base = [
    {
        "case_id": "CASE_2018_01",
        "problem": {
            "offense_type": "online theft",
            "medium": "phishing website",
            "unauthorized_transfer": True,
            "crypto_involved": False,
            "intent_proven": True
        },
        "solution": {
            "defense_strategy": "Argue lack of direct mens rea regarding electronic bypass.",
            "precedent_clause": "Section 4-A Cybercrime Act (Unauthorized Access)",
            "argument_pattern": "Focus on third-party security vulnerabilities in web browsers."
        }
    },
    {
        "case_id": "CASE_2020_05",
        "problem": {
            "offense_type": "digital fraud",
            "medium": "identity theft",
            "unauthorized_transfer": True,
            "crypto_involved": False,
            "intent_proven": True
        },
        "solution": {
            "defense_strategy": "Challenge IP tracing log reliability and session validity.",
            "precedent_clause": "E-Commerce Act Section 33 (Hacking & Fraud)",
            "argument_pattern": "Highlight shared IP address subnets to establish reasonable doubt."
        }
    },
    {
        "case_id": "CASE_2022_12",
        "problem": {
            "offense_type": "unauthorized bank transfers",
            "medium": "session hijacking",
            "unauthorized_transfer": True,
            "crypto_involved": True,
            "intent_proven": False
        },
        "solution": {
            "defense_strategy": "Demonstrate compromise via malware payload without defendant's consent.",
            "precedent_clause": "Financial Cybercrime Prevention Act Clause 12",
            "argument_pattern": "Establish client was an unwitting victim of a Trojan horse infection."
        }
    },
    {
        "case_id": "CASE_2023_09",
        "problem": {
            "offense_type": "wire fraud",
            "medium": "email spoofing",
            "unauthorized_transfer": False,
            "crypto_involved": False,
            "intent_proven": False
        },
        "solution": {
            "defense_strategy": "Rebut intent based on lack of monetary settlement.",
            "precedent_clause": "Penal Code Sec. 308 (Attempted Fraud)",
            "argument_pattern": "Emphasize non-completion of transaction."
        }
    }
]


# ------------------------------------------------------------------------------
# 4. IMPLEMENT SIMILARITY ASSESSMENT (Weighted Feature Scoring)
# ------------------------------------------------------------------------------
FEATURE_WEIGHTS = {
    "offense_type": 0.30,
    "medium": 0.20,
    "unauthorized_transfer": 0.25,
    "crypto_involved": 0.15,
    "intent_proven": 0.10
}

def calculate_similarity(new_case, historical_case):
    score = 0.0
    for feature, weight in FEATURE_WEIGHTS.items():
        val_new = new_case.get(feature)
        val_hist = historical_case.get(feature)
        
        # String comparison or exact boolean match
        if val_new == val_hist:
            score += weight
        elif isinstance(val_new, str) and isinstance(val_hist, str):
            # Partial match for strings (e.g., matching keywords)
            if val_new in val_hist or val_hist in val_new:
                score += weight * 0.5
                
    return score

def retrieve_best_case(new_case, case_base):
    ranked_cases = []
    for case in case_base:
        similarity = calculate_similarity(new_case, case["problem"])
        ranked_cases.append((case, similarity))
    
    # Sort descending by similarity score
    ranked_cases.sort(key=lambda x: x[1], reverse=True)
    return ranked_cases[0][0], ranked_cases[0][1], ranked_cases


# ------------------------------------------------------------------------------
# 5. ADAPT THE SOLUTION
# ------------------------------------------------------------------------------
def adapt_solution(retrieved_case, new_case):
    base_solution = retrieved_case["solution"].copy()
    new_prob = new_case
    
    adaptations = []
    
    # Adaptation Rule 1: Technical context adaptation for Cryptocurrency
    if new_prob.get("crypto_involved") and not retrieved_case["problem"].get("crypto_involved"):
        base_solution["argument_pattern"] += " [ADAPTED]: Incorporate blockchain forensic analysis logs and immutable ledger timing verification."
        adaptations.append("Added cryptocurrency/blockchain forensic argument module.")
        
    # Adaptation Rule 2: Technical context adaptation for specific electronic medium
    if new_prob.get("medium") != retrieved_case["problem"].get("medium"):
        base_solution["defense_strategy"] += f" [ADAPTED]: Adjust focus to digital evidence specific to '{new_prob.get('medium')}' vectors."
        adaptations.append(f"Shifted technical defense target from '{retrieved_case['problem'].get('medium')}' to '{new_prob.get('medium')}'.")
        
    # Adaptation Rule 3: Intent mitigation adaptation
    if not new_prob.get("intent_proven") and retrieved_case["problem"].get("intent_proven"):
        base_solution["precedent_clause"] += " + Sec 10-B (Lack of Criminal Intent in Automated Scripts)"
        adaptations.append("Appended statutory defense for unproven intent in automated execution.")
        
    return base_solution, adaptations


# ------------------------------------------------------------------------------
# 6. DEMONSTRATE LEARNING (RETAIN STAGE)
# ------------------------------------------------------------------------------
def retain_new_case(case_base, new_problem, final_solution, outcome="Verdict: Acquitted / Charges Reduced"):
    new_id = f"CASE_2026_{len(case_base) + 1:02d}"
    new_entry = {
        "case_id": new_id,
        "problem": new_problem,
        "solution": final_solution,
        "case_outcome": outcome
    }
    case_base.append(new_entry)
    return new_id


# ------------------------------------------------------------------------------
# 7. MAIN EXECUTION & OUTPUT DISPLAY
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 70)
    print("      AI-BASED LEGAL DECISION SUPPORT SYSTEM (CBR ENGINE)")
    print("=" * 70)
    
    # New Target Problem Scenario
    new_client_case = {
        "offense_type": "theft involving electronic transfer",
        "medium": "unauthorized API key extraction",
        "unauthorized_transfer": True,
        "crypto_involved": True,
        "intent_proven": False
    }
    
    print("\n[1] NEW CLIENT PROBLEM SCENARIO:")
    print(json.dumps(new_client_case, indent=4))
    
    # Retrieve
    best_case, top_score, all_rankings = retrieve_best_case(new_client_case, case_base)
    
    print("\n" + "-" * 70)
    print("[2] SIMILARITY ASSESSMENT & RETRIEVAL:")
    print(f"✔ Top Ranked Precedent Case: {best_case['case_id']}")
    print(f"✔ Similarity Score:          {top_score * 100:.1f}%")
    print("\nFull Case Rankings:")
    for case_item, score in all_rankings:
        print(f"  • {case_item['case_id']}: {score * 100:.1f}% similarity")
        
    print("\nRetrieved Case Solution:")
    print(json.dumps(best_case["solution"], indent=4))
    
    # Adapt
    adapted_solution, applied_adaptations = adapt_solution(best_case, new_client_case)
    
    print("\n" + "-" * 70)
    print("[3] SOLUTION ADAPTATION (REASONING ENGINE):")
    print("Applied Technical Adaptations:")
    for adapt_note in applied_adaptations:
        print(f"  ✔ {adapt_note}")
        
    print("\nFinal Adapted Legal Strategy:")
    print(json.dumps(adapted_solution, indent=4))
    
    # Retain
    new_case_id = retain_new_case(case_base, new_client_case, adapted_solution)
    
    print("\n" + "-" * 70)
    print("[4] RETAIN STAGE (LEARNING CONFIRMATION):")
    print(f"✔ New case successfully stored as '{new_case_id}' in Knowledge Base.")
    print(f"✔ Total cases in system memory: {len(case_base)}")
    
    print("\nUpdated Case Base Summary List:")
    for c in case_base:
        print(f"  - [{c['case_id']}] {c['problem']['offense_type']} via {c['problem']['medium']}")
    print("=" * 70)