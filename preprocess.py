import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer

# Assuming the data is stored in a CSV file named 'data.csv'
data1 = pd.read_excel("Data/data.xlsx")
data2 = pd.read_excel("Data/data2.xlsx")
all_clolumns = ["id", "status", "date_submitted", "gender", "age", "region", "watch_options", "preferred_cinema", "language_options", "watch_duration", "weekly_duration", "top_genres", "preferred_screen_size", "romantic_preference", "horror_preference", "monthly_expense", "ott_subscription", "preferred_time"]
data1.columns = all_clolumns
data2.columns = all_clolumns

data2.drop(['id', 'status', 'date_submitted'], axis=1, inplace=True)
data1.drop(['id', 'status', 'date_submitted'], axis=1, inplace=True)
data = pd.concat([data1, data2], ignore_index=True)
print(data)
single_option_columns=['gender', 'region', 'preferred_cinema', 'preferred_screen_size', 'romantic_preference', 'horror_preference', 'ott_subscription']
multi_option_columns=['top_genres', 'preferred_time', 'watch_options', 'language_options']
num_columns=['age', 'watch_duration', 'weekly_duration', 'monthly_expense']
data[multi_option_columns] = data[multi_option_columns].apply(lambda x: x.str.split(','))
le = LabelEncoder()
data[single_option_columns] = data[single_option_columns].apply(le.fit_transform)
print(data[single_option_columns])
print(data[multi_option_columns])

data.to_excel(excel_writer='preprocessed_data.xlsx')

