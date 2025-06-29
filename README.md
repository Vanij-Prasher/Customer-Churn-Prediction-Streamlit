# 🎓 Celebal Tech Internship – Python & Data Science Projects

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Internship](https://img.shields.io/badge/Internship-Celebal%20Tech-%23007ACC?logo=github)](https://www.celebaltech.com/)
[![GitHub Repo](https://img.shields.io/badge/Repository-Vanij--Prasher/Celebal--Tech--Vanij-blue?logo=github)](https://github.com/Vanij-Prasher/Celebal-Tech-Vanij)

Welcome to my GitHub repository for the **Celebal Tech Data Science Internship**.  
This repo showcases my weekly progress, learning, and projects in Python, OOP, and data science foundations.

---

## 🔍 Overview

This internship involves solving hands-on problems using Python and essential CS fundamentals.  
Each task is structured to strengthen:

- 🐍 Python Programming
- 🧱 Data Structures & Algorithms
- 🧠 Object-Oriented Design
- 📈 Data Science Foundations
- 🛠️ Git & GitHub Project Workflows

---

## 🧠 Concepts Used

- `for` loops and range-based iteration
- String multiplication and spacing
- Printing formatted output to the console
- Data structures: Linked Lists
- Exploratory Data Analysis (EDA)
- Data Cleaning and Imputation
- Data Visualization using Seaborn and Matplotlib
- Correlation analysis and outlier detection

---

## 📚 Weekly Tasks & Explanations

### 📘 Week 1 – Pattern Printing with Python

**Goal:** Learn basic control structures (`for` loops) and output formatting.  
**Task:** Create 3 console-based patterns using `"*"`:

- **Lower Triangular Pattern**  
- **Upper Triangular Pattern**  
- **Pyramid Pattern**

**Concepts Used:**  
`for` loops, `range()`, string multiplication, alignment using spaces.

📌 **Purpose:**  
Build comfort with basic syntax and GitHub push-pull workflow.

---

### 🔹 Lower Triangular Pattern
```
* 
* * 
* * * 
* * * * 
* * * * *
```

### 🔹 Upper Triangular Pattern

```
* * * * * 
* * * * 
* * * 
* * 
*
```

### 🔹 Pyramid Pattern
```
    *
   * * 
  * * * 
 * * * * 
* * * * * 
```
---
### 📘 Week 2 – Singly Linked List using OOP

**Goal:** Understand and implement linked data structures with classes.  
**Task:** Create a Singly Linked List with:

- Node & LinkedList classes
- `add_node()` – Add node to end  
- `print_list()` – Print the linked list  
- `delete_nth_node(n)` – Delete the nth node (1-based index)
- Exception handling for empty list / invalid index

**Concepts Used:**  
Classes, object references, method definition, edge case handling.

---
### 📘 Week 3 – Titanic Dataset Visualization

**Goal:** Perform data visualization using Seaborn and Matplotlib on the Titanic dataset.  
**Task:** Load the Titanic dataset and generate multiple plots for EDA (Exploratory Data Analysis):

- Survival count (`countplot`)
- Survival by gender
- Survival by passenger class
- Age distribution by survival (`histplot`)
- Heatmap of missing values (`heatmap`)
- Save screenshots of each plot

**Concepts Used:**  
DataFrames, Seaborn visualizations, `matplotlib.pyplot`, categorical and continuous data plotting.

### 🖼️ Sample Visualizations

You’ll find the code and screenshots in the [`assignment3/`](assignment3/) folder.
___
### 📘 Week 4 – Advanced Titanic Data Visualization and Preprocessing

**Goal:** Perform in-depth data analysis, cleaning, imputation, outlier detection, and complex visualization using the Titanic dataset.

**Task:**  
=> Load the Titanic dataset using Seaborn.  
=> Handle missing values using heatmaps and imputation techniques.  
=> Impute missing ages based on passenger class.  
=> Drop irrelevant columns like `deck` and rows with remaining missing data.  
=> Perform univariate and multivariate visualizations:
- Survival count
- Gender distribution
- Passenger class distribution
- Age and fare distribution
- Boxplot for outlier detection
- Survival distribution by gender and class
- Violin plot for survival and age distribution
- Correlation heatmap (numeric columns only)

**Concepts Used:**
- Missing value handling and imputation
- Advanced Seaborn visualizations: violin plots, boxplots, heatmaps
- Outlier detection
- Correlation analysis
- Data cleaning workflows

**Purpose:**  
This task builds on Week 3 and introduces real-world data preprocessing steps, handling missing data, and advanced exploratory data analysis using visual techniques.

### 🖼️ Sample Visualizations

You’ll find the code and screenshots in the [`assignment4/`](assignment4/) folder.

---

## 📌 Purpose

This task is part of the **foundational training module** at **Celebal Tech**, meant to:
- Refresh basic Python syntax
- Ensure familiarity with Git and GitHub workflows
- Demonstrate readiness for further technical tasks in the internship
- Learn OOP fundamentals, data structure traversal, and class-based design.
- Understand dataset structure and build visual insights using plotting libraries. It forms the base of EDA in real-world data science workflows.

---
## 📁 File Structure

```text
Celebal-Tech-Vanij/
├── Week1.py                         # Pattern printing in Python
├── Week2.py                         # Singly Linked List using OOP
├── assignment3/
│   ├── data_visualization_week3.py  # Titanic dataset visualizations (Week 3)
│   ├── Screenshot 2025-06-22 at ... # Screenshots for Week 3 visualizations
│   └── ...
├── assignment4/
│   ├── week4.py                     # Advanced Titanic EDA (Week 4)
│   ├── Screenshot 1.png             # Screenshots for Week 4 visualizations
│   ├── Screenshot 2.png
│   └── ...
├── README.md                        # Internship overview and task breakdown
```
## 🙋‍♂️ Author
### 🙋‍♂️ Author

**Vanij Prasher**  
B.E. in Computer Science & Engineering (Artificial Intelligence & Machine Learning) – 4th Year  
**Intern @ [Celebal Tech](https://www.celebaltech.com/)**  
🌐 GitHub: [github.com/Vanij-Prasher](https://github.com/Vanij-Prasher)
---

## 📅 Internship Info

**Company**: Celebal Tech  
**Role**: Data Science Intern  
**Week**: 3 --Completed--  
**Focus**: Python basics and GitHub project structure

---

## 🔗 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/Celebal-Tech-Vanij.git
   cd Celebal-Tech-Vanij

