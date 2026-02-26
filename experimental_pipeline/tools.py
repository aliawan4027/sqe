# tools.py
"""
This module contains the basic tools that the SimpleAgent can use.
"""
def calendar_tool(data):
    return "Meeting scheduled at 10 AM"

def email_tool(data):
    return "Email sent successfully"

def calculator_tool(data):
    try:
        return str(eval(data))
    except:
        return "Calculation error"

tools = {
    "calendar_tool": calendar_tool,
    "email_tool": email_tool,
    "calculator_tool": calculator_tool
}