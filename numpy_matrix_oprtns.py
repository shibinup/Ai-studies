import numpy as np

quarter1 = np.array([
    [1, 8, 38],         #product A
    [9, 6, 87],         #product B
    [7, 25, 9]          #product C
])

quarter2= np.array([
    [10, 2, 30],        #product A
    [40, 78, 64],       #product B
    [45, 80, 76]        #product C
])

total= quarter1+quarter2
print(total)

# growth
growth= quarter2-quarter1
print(growth)

#percentage of increase
percentage = growth*100/quarter1
print("percentage is ",percentage)

#row are products and columns are countries
prices = np.array([
    [100,95, 120],        #product A
    [120, 90, 89],       #product B
    [89, 80, 98]        #product C
])

quarter1_revene = quarter1*prices
print(quarter1_revene)

# every where givving 20% discount then 
q1_discount_price= quarter1_revene*0.2
print(q1_discount_price)

net_revenue = quarter1_revene-q1_discount_price
print(net_revenue)


#total discount price 
sum_of_discount = np.sum(q1_discount_price)
print('total discoun given price',sum_of_discount)