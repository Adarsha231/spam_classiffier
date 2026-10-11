import pandas as pd

df = pd.read_csv(r"C:\Users\adars\Downloads\email-classifier\dataset\email_origin.csv")

print(df.head())

print("Dataset info\n")
print(df.info())

print("column\n")
print(df.columns)

print("Lable distribution\n")
print(df['label'].value_counts())

print("Missing values\n")
print(df.isnull().sum())

print("Duplicates")
print(df.duplicated().sum())
