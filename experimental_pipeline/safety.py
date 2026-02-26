# safety.py
"""
Safety module to detect unsafe tasks.
"""
unsafe_keywords = ["delete", "hack", "steal", "drop table"]

def safety_check(task):
    for word in unsafe_keywords:
        if word.lower() in task.lower():
            return False
    return True