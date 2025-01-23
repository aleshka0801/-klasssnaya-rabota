import pandas as pd


# Чтение Excel-файла
df_excel = pd.read_excel('data1.xlsx')

# Посмотреть первые 10 строк
print(df_excel.iloc[2])


