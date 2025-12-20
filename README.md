
#  Student Performance & Prediction Analysis

A Python data analysis project that evaluates student academic performance using **NumPy, Pandas, and Matplotlib**, and predicts performance categories based on attendance and marks.

---

##  Tech Stack

* **Python**
* **NumPy**
* **Pandas**
* **Matplotlib**

---

## Project Features

* Subject-wise average marks analysis
* Attendance vs average marks correlation
* Top & weak student identification
* Grade distribution visualization
* Logic-based performance prediction

---

##  Dataset

Synthetic student data generated using NumPy.

**Columns:**

* `name`
* `math`, `english`, `physics`
* `Attendance`
* `TotalMarks`
* `Average`
* `AverageGrade`
* `PerformanceCategory`

---

##  Visualizations

* Horizontal bar chart (Subject vs Marks)
* Scatter plot (Attendance vs Average Marks)
* Pie chart (Grade Distribution)

---

## 🔍 Performance Prediction Logic

```python
if attendance >= 85 and avg_marks >= 75:
    High Performer
elif attendance >= 70 and avg_marks >= 60:
    Medium Performer
else:
    Low Performer
```

---

##  How to Run

```bash
pip install numpy pandas matplotlib
python student_performance_analysis.py
```

---

##  Key Learnings

* Data manipulation with Pandas
* Numerical analysis using NumPy
* Data visualization with Matplotlib
* Correlation analysis
* Rule-based prediction logic

---

##  Future Improvements

* Machine learning prediction model
* Streamlit dashboard
* CSV export
* Real-world dataset integration


## 👤 Author

**Govardhan**

---
