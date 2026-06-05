import pandas as pd
df = pd.read_csv("movies.csv")
print(len(df))



#task 1- which movie have highest rating ?
print(df.columns)
print("---------")
movie_have_highest_rating=df[df["vote_count"]==df["vote_count"].max()]
print(movie_have_highest_rating)

print("---------")
#task 2-  what is average rating?
average_rating= df["vote_count"].mean()
print("average rating =",average_rating)

print("---------")
#task 3 Top 10 highest-rated movies?
top_10_highest_rated_ovie= df.sort_values(by="vote_count",ascending=False).head(10)["title"]
print(top_10_highest_rated_ovie)

print("---------")
#task 3 Movies released after 2015?

df["release_date"] = pd.to_datetime(df["release_date"])
movie_after_2020=df[df["release_date"].dt.year > 2015]["title"]
print(movie_after_2020)