def analyze_results(test_results: list[dict]) -> list[dict]:
    """
    Performs Root Cause Analysis (RCA) on test failures.
    Categorizes failures into App Bugs, Environment Issues, or Script Errors.
    """
    defects = []
    print("\n[ANALYZER] Performing Root Cause Analysis...")
    for result in test_results:
        if result["status"] == "FAILED":
            tech_details = result.get("technical_details", "").lower()
            
            # Identify Failure Type
            if "timeout" in tech_details or "waiting for" in tech_details:
                failure_type = "Environment / Latency"
                severity = "Medium"
            elif "assertionerror" in tech_details:
                failure_type = "Functional Bug"
                severity = "High"
            else:
                failure_type = "Uncategorized Failure"
                severity = "Low"

            defect = {
                "test_case": result["test_case"],
                "description": result["message"],
                "type": failure_type,
                "severity": severity
            }
            defects.append(defect)
            print(f"  Detected {failure_type}: {defect['description']} (Severity: {severity})")
    
    if not defects:
        print("  No defects identified after RCA.")

    return defects

if __name__ == "__main__":
    # Example usage
    sample_test_results = [
        {"test_case": "Verify login", "status": "PASSED", "message": ""},
        {"test_case": "Verify invalid login error", "status": "FAILED", "message": "Error message not displayed"},
        {"test_case": "Verify user profile update", "status": "SKIPPED", "message": "Feature not implemented"}
    ]

    found_defects = analyze_results(sample_test_results)
    print("\nIdentified Defects:")
    if found_defects:
        for i, defect in enumerate(found_defects):
            print(f"  Defect {i+1}: {defect["test_case"]} - {defect["description"]} (Severity: {defect["severity"]})")
    else:
        print("  No defects found in sample results.")