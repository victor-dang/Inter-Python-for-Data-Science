# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn', 
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'australia':'vienna' }
          
# Iterate over europe
for key,value in europe.items():
    print("the capital of "+str(key)+" is "+str(value))

# Import numpy as np
import numpy as np

# For loop over np_height 
for h in np_height:
    print(str(h)+" inches")

# For loop over np_baseball that is 2D Numpy array
for b in np.nditer(np_baseball):
    print(str(b))


cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for rlabel, rcontent in cars.iterrows():
    print(rlabel)
    print(rcontent)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab+": "+str(row['cars_per_cap']))

# Code for loop that adds COUNTRY column
for rlabel,rcontent in cars.iterrows():
    cars.loc[rlabel, "COUNTRY"]=str(rcontent["country"]).upper()
# Print cars
print(cars)

# Use .apply(str.upper)
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"]
cars["COUNTRY"] = cars["country"].apply(str.upper)
print(cars)