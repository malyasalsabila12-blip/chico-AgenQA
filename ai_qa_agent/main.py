from test_generator import generate_test_cases
from test_executor import execute_test
from defect_analyzer import analyze_results
from config import config

def main():
    print("Chico, the AI QA Automation Engineer started!")

    # Phase 1: Test Case Generation
    target_url = config.BASE_URL
    test_breakdown = {"happy": 8, "negative": 7, "boundary": 3, "edge": 2}
    test_cases = generate_test_cases(target_url, test_breakdown)
    print("\nGenerated Test Cases:")
    for i, test_case in enumerate(test_cases):
        print(f"  {i+1}. {test_case}")

    # Phase 2: Test Execution
    print("\nStarting Test Execution...")
    test_results = []
    for test_case in test_cases:
        result = execute_test(test_case, target_url)
        test_results.append(result)
        print(f"  Test Case: {result['test_case']} - Status: {result['status']} - Message: {result['message']}")

    # Phase 3: Defect Identification
    defects = analyze_results(test_results)
    if defects:
        print("\nSummary of Identified Defects:")
        for i, defect in enumerate(defects):
            print(f"  Defect {i+1}: {defect['test_case']} - {defect['description']} (Severity: {defect['severity']})")
    else:
        print("\nNo defects were identified.")

if __name__ == "__main__":
    main()