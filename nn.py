import pandas as pd
from pandas.core.arrays.base import try_cast_to_ea
from sklearn.model_selection import train_test_split

fp = "./NLP/data/train_df.csv"
df = pd.read_csv(fp)

X = df['headlines'].values
Y = df['is_sarcastic'].values
X_trains, X_test, Y_train, T_test = train_test_split(X,Y, test_size=0.3, random_state=42)

