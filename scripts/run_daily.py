
import random
import os
from datetime import datetime

# Create a folder for daily reports
os.makedirs("reports", exist_ok=True)

# Task 1: Mathematical analysis
def math_analysis():
    numbers = [random.randint(1, 1000) for _ in range(100)]

    return f"""
    TASK: Mathematical Analysis
    Total numbers: {len(numbers)}
    Sum: {sum(numbers)}
    Average: {sum(numbers) / len(numbers):.2f}
    Maximum: {max(numbers)}
    Minimum: {min(numbers)}
    """

# Task 2: Statistical analysis
def statistics():
    numbers = [random.randint(1, 500) for _ in range(50)]

    return f"""
    TASK: Statistical Analysis
    Dataset size: {len(numbers)}
    Mean: {sum(numbers) / len(numbers):.2f}
    Median: {sorted(numbers)[len(numbers)//2]}
    Range: {max(numbers) - min(numbers)}
    """

# Task 3: Text analysis
def text_analysis():
    text = "Python automation makes repetitive tasks easier and faster."
    words = text.split()

    return f"""
    TASK: Text Analysis
    Total words: {len(words)}
    Total characters: {len(text)}
    Unique words: {len(set(words))}
    Longest word: {max(words, key=len)}
    """

# Task 4: Sorting algorithm
def sorting_analysis():
    numbers = [random.randint(1, 10000) for _ in range(100)]

    sorted_numbers = sorted(numbers)

    return f"""
    TASK: Sorting Analysis
    Original dataset size: {len(numbers)}
    First 10 sorted values: {sorted_numbers[:10]}
    Last 10 sorted values: {sorted_numbers[-10:]}
    """

# Task 5: Data processing
def data_processing():
    numbers = [random.randint(1, 100) for _ in range(100)]

    even = [n for n in numbers if n % 2 == 0]
    odd = [n for n in numbers if n % 2 != 0]

    return f"""
    TASK: Data Processing
    Total values: {len(numbers)}
    Even numbers: {len(even)}
    Odd numbers: {len(odd)}
    Even sum: {sum(even)}
    Odd sum: {sum(odd)}
    """

# Available Python tasks
tasks = [
    math_analysis,
    statistics,
    text_analysis,
    sorting_analysis,
    data_processing
]

# Randomly select one task
selected_task = random.choice(tasks)
result = selected_task()

# Generate today's report
today = datetime.now().strftime("%Y-%m-%d")

report = f"""
DAILY PYTHON AUTOMATION REPORT
Date: {today}
Selected Script: {selected_task.__name__}

{result}
"""

# Save the report
with open(f"reports/{today}.md", "w") as file:
    file.write(report)

print(report)
