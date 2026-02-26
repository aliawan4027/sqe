# main.py
"""
Entry point to run the full experimental pipeline.
"""
from tools import tools
from agent import SimpleAgent
from safety import safety_check
from semantic import semantic_similarity
from testcases import generate_test_cases
import pandas as pd
from analysis import analyze_results
import time

def run_experiment():
    # Generate test cases
    test_cases = generate_test_cases(100)

    # Initialize agent
    agent = SimpleAgent(tools, failure_rate=0.1)

    results = []

    # Run all test cases
    for case in test_cases:
        task = case["task"]
        start = time.time()
        predicted_safe = safety_check(task)

        if not predicted_safe:
            results.append({
                "task": task,
                "true_safe": case["label_safe"],
                "pred_safe": False,
                "behavior_valid": False,
                "semantic_score": 0,
                "execution_time": 0
            })
            continue

        plan = agent.plan(task)
        behavior_valid = plan == case["expected_plan"]
        output = agent.execute(plan, task.replace("calculate", ""))
        similarity = semantic_similarity(output, case["expected_output"])
        end = time.time()

        results.append({
            "task": task,
            "true_safe": case["label_safe"],
            "pred_safe": predicted_safe,
            "behavior_valid": behavior_valid,
            "semantic_score": similarity,
            "execution_time": end-start
        })

    df = pd.DataFrame(results)
    df.to_csv("publishable_experiment_results.csv", index=False)
    print("Experiment saved as publishable_experiment_results.csv")

    # Analyze results
    analyze_results(df)

if __name__ == "__main__":
    run_experiment()