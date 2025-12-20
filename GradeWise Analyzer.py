import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
np.random.seed(42)
data = {
    "name": [f"student{i}" for i in range(1, 31)],
    "math": np.random.randint(60, 100, 30),
    "english": np.random.randint(60, 100, 30),
    "physics": np.random.randint(60, 100, 30),
    "Attendance": np.random.randint(70, 100, 30),
}
df = pd.DataFrame(data)
df["TotalMarks"] = df[["math", "english", "physics"]].sum(axis=1)
df["Average"] = df["TotalMarks"] / 3
def setGrade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

df["AverageGrade"] = df["Average"].apply(setGrade)

subject_avg = df[["math", "english", "physics"]].mean()
plt.barh(subject_avg.index, subject_avg.values, height=0.5)
plt.title("Subject vs Marks")
plt.xlabel("Average Marks")
plt.ylabel("Subjects")
plt.show()

correlation = np.corrcoef(df["Attendance"], df["Average"])[0, 1]
plt.title("Correlation of Attendance vs Average marks {:.2f}".format(correlation))
plt.scatter(df["Average"], df["Attendance"])
plt.xlabel("Average")
plt.ylabel("Attendance")
plt.show()
top_students = df.sort_values(by=["Average"], ascending=False).head(5)
weak_students = df[df["Average"] < 70]
print("\Top Performing Students:\n")
print(top_students[["name", "Average", "AverageGrade"]])
print("\nWeak Students (At Risk):")
print(weak_students[["name", "Average", "AverageGrade"]])

grade_count = df["AverageGrade"].value_counts().sort_index()
print("Grade Distribution:\n")
plt.pie(grade_count, labels=grade_count.index, autopct="%1.1f%%")
plt.title("Grade Distribution")
plt.show()
def predict_performance(attendance, avg_marks):
    if attendance >= 85 and avg_marks >= 75:
        return "High Performer"
    elif attendance >= 70 and avg_marks >= 60:
        return "Medium Performer"
    else:
        return "Low Performer"
df["PerformanceCategory"] = df.apply(
    lambda x: predict_performance(x["Attendance"], x["Average"]),
    axis=1
)
print("Final Student Performance Summary:\n")

print(df[["name", "Attendance", "Average", "AverageGrade", "PerformanceCategory"]])

