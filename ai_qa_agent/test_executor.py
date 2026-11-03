import subprocess
import os
import json
from config import config

def execute_test(test_case: str, target_url: str) -> dict:
    """
    Executes a specific test case using the professional pytest framework.
    Captures full output and identifies technical root causes.
    """
    print(f"  [RUNNER] Executing Scenario: {test_case}")
    
    # Path to our test file
    test_file = os.path.join("ai_qa_agent", "test_saucedemo.py")
    
    # Professional Command Construction:
    # -k filters for the specific test case
    # --alluredir saves results for the Trend Analysis
    cmd = [
        "pytest", 
        test_file, 
        "-k", test_case, 
        f"--alluredir={config.ALLURE_RESULTS_DIR}",
        "--clean-alluredir",
        "--reruns", "2",
        "-v"
    ]

    try:
        # Run the actual test suite
        process = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        
        # Determine Status
        if process.returncode == 0:
            status = "PASSED"
            message = "Requirement verified successfully."
        elif process.returncode == 5: # No tests collected
            status = "SKIPPED"
            message = "Test implementation pending."
        else:
            status = "FAILED"
            # Extract technical error from the end of the pytest output
            message = "Assertion failed or UI element mismatch."
            
            # Senior QA: Extracting traceback snippet
            lines = process.stdout.splitlines()
            for i, line in enumerate(lines):
                if "E   AssertionError" in line or "E   playwright._impl._api_types.Error" in line:
                    message = " ".join(lines[i:i+3]) # Get context around error
                    break

        return {
            "test_case": test_case,
            "status": status,
            "message": message,
            "technical_details": process.stdout[-500:] if status == "FAILED" else ""
        }

    except subprocess.TimeoutExpired:
        return {"test_case": test_case, "status": "BLOCKED", "message": "Test timed out after 60s."}
    except Exception as e:
        return {"test_case": test_case, "status": "ERROR", "message": f"Runner Error: {str(e)}"}

if __name__ == "__main__":
    # Smoke test the runner
    res = execute_test("Verify standard_user can log in", "https://www.saucedemo.com/")
    print(json.dumps(res, indent=2))
