import pandas as pd
import matpoltlib.pploy as pllt


#e lexon filen edhe e run ne df
df = pd.read_csv('../lesson14.2/avgIQpercountry.csv')


filtered_df = df[df["Average IQ"]>=100]

filtered_df = filtered_df.sort_values(by="Average IQ", ascending=False)


print(filtered_df)

plt.figure(figsize=(14,8))

bar = plt.bar(filtered_df["Country"], filtered_df["Average IQ"],color="skyblue")


plt.title("Average IQ by country(IQ>=100)",fontsize=16)

plt.xlabel("Country",fontsize=14)
plt.xlabel("Average IQ",fontsize=14)

plt.xlabel(rotation=90,fontsize=14)
plt.yticks(fontsize=10)

plt.grid(axis="y",linestyle="--",alpha=0.8)

plt.bar_label(bars,fmt="%.2f",fontsize=10,color="black")

plt.show()


































