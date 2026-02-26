# analysis.py
"""
Run experiments, generate confusion matrix, statistical tests, and plots.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
from scipy import stats

def analyze_results(df):
    """
    Generates confusion matrix, classification report, and plots.
    """
    # Confusion matrix
    cm = confusion_matrix(df["true_safe"], df["pred_safe"])
    print("Confusion Matrix:\n", cm)
    print("\nClassification Report:\n", classification_report(df["true_safe"], df["pred_safe"]))

    # Statistical significance
    correct = df[df["behavior_valid"] == True]["semantic_score"]
    incorrect = df[df["behavior_valid"] == False]["semantic_score"]
    t_stat, p_value = stats.ttest_ind(correct, incorrect, equal_var=False)
    print("T-statistic:", t_stat)
    print("P-value:", p_value)

    # Execution time distribution
    plt.figure()
    sns.histplot(df["execution_time"], bins=20)
    plt.title("Execution Time Distribution")
    plt.show()