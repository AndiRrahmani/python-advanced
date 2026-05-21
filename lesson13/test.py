import panda as pd

from array_manipulation import total_sum

product = ["Apples","Bananas","Oranges","Grapes","Pinaples"]

sales = [150,200,180.90,60]


sales_series = pd.Series(sales, index=product)


print(sales_series)

print(sales_series['Grapes'])

