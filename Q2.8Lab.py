# 8. Given a list of products and prices: products = [("laptop", 75000), ("mouse", 1200), 
# ("keyboard", 3500)] 
#  Use map and lambda to apply 18% GST to all prices 
#  Use filter and lambda to get products costing more than ₹5000 
#  Print both results 

product = [("laptop",75000),("mouse",1200),("keyboard",3500)]

gst = list(map(lambda p:(p[0],round(p[1]*1.18,2)),product))

for p in gst:
    print(p)
print()

cost = filter(lambda x: x[1]>5000,product)
for x in cost:
    print(x)

