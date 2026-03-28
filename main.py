import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import tkinter as tk
from tkinter import messagebox
data = pd.read_csv(r"c:\Users\awata\Desktop\python\vitpython_project\students.csv")

X = data[["hours_studied", "attendance", "previous_score"]]
y = data["final_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


def predict_score():
    try:
        h = float(hours_entry.get())
        a = float(attendance_entry.get())
        p = float(previous_entry.get())

        new_data = pd.DataFrame([[h, a, p]],
                                columns=["hours_studied", "attendance", "previous_score"])

        predicted = model.predict(new_data)[0]

        result_label.config(text=f"Predicted Final Score: {predicted:.2f} / 100")


        if predicted >= 75:
            comment = "Very good performance expected."
        elif predicted >= 60:
            comment = "Good, but you can still improve."
        elif predicted >= 40:
            comment = "At risk — you should study more."
        else:
            comment = "High risk of failing — urgent improvement needed."

        comment_label.config(text=comment)

    except Exception:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")


root = tk.Tk()
root.title("Student Performance Prediction")
root.geometry("400x400")
root.config(bg="#eef2f3")

title_label = tk.Label(root, text="Student Performance Predictor",
                       font=("Arial", 16, "bold"), bg="#eef2f3")
title_label.pack(pady=10)

tk.Label(root, text="Hours Studied per Day:", bg="#eef2f3").pack()
hours_entry = tk.Entry(root)
hours_entry.pack(pady=5)

tk.Label(root, text="Attendance (%) :", bg="#eef2f3").pack()
attendance_entry = tk.Entry(root)
attendance_entry.pack(pady=5)

tk.Label(root, text="Previous Exam Score:", bg="#eef2f3").pack()
previous_entry = tk.Entry(root)
previous_entry.pack(pady=5)

predict_btn = tk.Button(root, text="Predict Final Score", command=predict_score,
                        bg="#4CAF50", fg="white", font=("Arial", 12))
predict_btn.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#eef2f3")
result_label.pack(pady=5)

comment_label = tk.Label(root, text="", font=("Arial", 12), bg="#eef2f3")
comment_label.pack(pady=5)

metrics = f"MSE: {mse:.2f} | R²: {r2:.2f}"
metrics_label = tk.Label(root, text=metrics, bg="#eef2f3", fg="gray")
metrics_label.pack(side="bottom", pady=10)

root.mainloop()