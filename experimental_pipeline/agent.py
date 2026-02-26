# agent.py
"""
This module defines the SimpleAgent class, which plans and executes tasks.
"""
import random

class SimpleAgent:
    def __init__(self, tools, failure_rate=0.0):
        self.tools = tools
        self.failure_rate = failure_rate

    def plan(self, task):
        """
        Decide which tools to use based on the task.
        Introduces failure with self.failure_rate.
        """
        if random.random() < self.failure_rate:
            return ["calendar_tool"]  # intentional failure

        if "schedule" in task and "email" in task:
            return ["calendar_tool", "email_tool"]
        elif "calculate" in task:
            return ["calculator_tool"]
        else:
            return []

    def execute(self, plan, input_data):
        """
        Execute the tools in the plan and combine their results.
        """
        results = []
        for step in plan:
            if step in self.tools:
                result = self.tools[step](input_data)
                results.append(result)
        return " ".join(results)