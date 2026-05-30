import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create sample dataset
data = {
    'Student_ID': [101, 102, 103, 104, 104, 105],
    'Name': ['Arun', 'Priya', 'Kavin', 'Divya', 'Divya', 'Rahul'],
    'Age': [18, 19, 18, 20, 20, np.nan],
    'Marks': [85, np.nan, 78, 120, 120, 65],
    'Attendance': [90, 95, 85, 92, 92, 80]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Handle Missing Values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Marks'].fillna(df['Marks'].mean(), inplace=True)

# Remove Duplicate Rows
df.drop_duplicates(inplace=True)

# Remove Outliers using IQR
Q1 = df['Marks'].quantile(0.25)
Q3 = df['Marks'].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

df = df[(df['Marks'] >= lower_limit) &
        (df['Marks'] <= upper_limit)]

print("\nCleaned Dataset:")
print(df)

# ----------------------------
# Visualization 1: Bar Chart
# ----------------------------
plt.figure(figsize=(6, 4))
plt.bar(df['Name'], df['Marks'])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.savefig("bar_chart.png")
plt.show()

# ----------------------------
# Visualization 2: Histogram
# ----------------------------
plt.figure(figsize=(6, 4))
plt.hist(df['Marks'], bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.show()

# ----------------------------
# Visualization 3: Scatter Plot
# ----------------------------
plt.figure(figsize=(6, 4))
plt.scatter(df['Attendance'], df['Marks'])
plt.title("Attendance vs Marks")
plt.xlabel("Attendance")
plt.ylabel("Marks")
plt.savefig("scatter_plot.png")
plt.show()

# ----------------------------
# Visualization 4: Pie Chart
# ----------------------------
plt.figure(figsize=(6, 6))
plt.pie(
    df['Attendance'],
    labels=df['Name'],
    autopct='%1.1f%%'
)
plt.title("Attendance Distribution")
plt.savefig("pie_chart.png")
plt.show()

print("\nProject Completed Successfully!")
print("Charts saved as PNG files.")
