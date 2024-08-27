# Загрузите набор данных из CSV-файла в DataFrame.
# Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
# Выведите информацию о данных (.info()) и статистическое описание (.describe()).
# Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз
import pandas as pd

df = pd.read_csv('ai_job_market_insights.csv')
print(df.head())

print(df.info())

print(df.describe())

df_dz = pd.read_csv('dz.csv')
print(df_dz)

group = df_dz.groupby('City')['Salary'].mean()
print(group)
