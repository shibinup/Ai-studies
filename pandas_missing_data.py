import pandas as pd
df = pd.read_csv("handle_missing_Movies_data.csv")
df= df.replace(8.5,999)

print(df)