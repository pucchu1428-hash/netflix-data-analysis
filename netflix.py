import pandas as pd
df=pd.read_csv('mymoviedb (2).csv')
print(df.head())
print(df.shape)
df.info()
print(df.isnull().sum())
df.duplicated().sum()
df.drop_duplicates()
print(df.head())
print(df.isnull().sum())
print(df.columns.tolist())
print(df.describe())
import matplotlib.pyplot as plt
df.head(10).plot(
    kind="bar",
    figsize=(10,5)
)
plt.title("movie data analysis")
plt.xlabel("movie index")
plt.ylabel("values")
plt.tight_layout()
plt.show()
print(df.columns.tolist())
df.info()
print(df.head(10))
print ("available columns")
for columns in df.columns:
    print(columns)
import pandas as pd
import matplotlib.pyplot as plt
numeric_columns = df.select_dtypes(include="number").columns

print("Numerical Columns:")
print(numeric_columns.tolist())

print("\nStatistical Summary:")
print(df[numeric_columns].describe())





