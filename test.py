import pandas as pd
df_train = pd.read_csv("train.csv")
print df_train[7*6*1115:].head()
print df_train.head()