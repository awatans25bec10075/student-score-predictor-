# Student Performance Predictor

This project is a simple Student Performance Predictor made using Python. It predicts a student's final exam score based on study hours, attendance, and previous exam marks.

The main purpose of this project is to understand how Machine Learning can be used in real-life situations like predicting academic performance.

## What This Project Does

The user enters:

- Hours studied per day
- Attendance percentage
- Previous exam score

After entering these values, the program predicts the final exam score and also gives a small comment about the student's expected performance.

For example:

- A high predicted score means the student is likely to perform well
- A low predicted score means the student may need to improve their studies

## Technologies Used

This project is made using:

- Python
- Pandas
- Scikit-learn
- Tkinter

## Files Used

```text
vitpython_project/

 main.py
 students.csv
 README.md
```

## About the Dataset

The dataset contains the following columns:

- hours_studied
- attendance
- previous_score
- final_score

These values are used to train the Linear Regression model.

## How the Project Works

1. The program reads the student data from the CSV file
2. The data is divided into training and testing parts
3. A Linear Regression model is trained
4. The user enters new values in the GUI
5. The model predicts the final score
6. A performance message is displayed

## Example

If a student studies 5 hours daily, has 80% attendance, and scored 65 in the previous exam, the predicted score may be around 70 to 75.

## Installation

Install the required libraries using:

```bash
pip install pandas scikit-learn
```

If pip does not work:

```bash
python -m pip install pandas scikit-learn
```

## Run the Project

```bash
python main.py
```

Or:

```bash
& "C:\Users\awata\AppData\Local\Python\pythoncore-3.14-64\python.exe" main.py
```

## Future Improvements

In the future, this project can be improved by:

- Adding better UI design
- Using a bigger dataset
- Adding graphs and charts
- Saving prediction history
- Using more advanced Machine Learning models

## Conclusion

This project is useful for understanding the basics of Machine Learning, GUI development, and working with datasets in Python. It is a good beginner-level project because it combines both prediction and user interaction in one program.

## Author

Made by Awatans Asthana
