import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer

# Assuming the data is stored in a CSV file named 'data.csv'
data = pd.read_excel("data.xlsx")
data.columns = [
    "id", "status", "date_submitted", "gender", "age", "region", "watch_options",
    "preferred_cinema", "language_options", "watch_duration", "weekly_duration",
    "top_genres", "preferred_screen_size", "romantic_preference",
    "horror_preference", "monthly_expense", "ott_subscription",
    "preferred_time"
]
data['date_submitted'] = pd.to_datetime(data['date_submitted'])

# data['top_genres'] = data['top_genres'].apply(lambda x: x.split(', '))
# data['preferred_time'] = data['preferred_time'].apply(lambda x: x.split(', '))
# data['monthly_expense'] = data['monthly_expense'].apply(lambda x: x.split('AED ')[1])
data.replace("", np.nan, inplace=True)
data.fillna(value='Other cinema', inplace=True)
print(data)
single_option_columns=['gender', 'region', 'preferred_cinema', 'preferred_screen_size', 'romantic_preference', 'horror_preference', 'ott_subscription']
multi_option_columns=['top_genres', 'preferred_time', 'watch_options', 'language_options']
data[multi_option_columns] = data[multi_option_columns].apply(lambda x: x.str.split(','))
mlb = MultiLabelBinarizer()
le = LabelEncoder()
data[single_option_columns] = data[single_option_columns].apply(le.fit_transform)
print(data[single_option_columns])
encoded_lang_options = mlb.fit_transform(data['language_options'])
print(pd.DataFrame(encoded_lang_options, columns=mlb.classes_))
data[multi_option_columns] = data[multi_option_columns].apply(mlb.fit_transform)
print(data[multi_option_columns])

