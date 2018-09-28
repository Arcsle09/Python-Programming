# Real Time Example of Cartesian Product Of Sets

# Consider that you sell cars and a customer comes to you with the following request. 
#“I need a number of cars. The models I want are Toyota Corolla, Honda CRV, and Chevy Cruze. 
# And, for me to pay (putting food on the table)for your service I need my cars to be white, grey, and red and I want them to have 1.4, 1.6, and 1.8 engine capacities. 
# I want a combination of cars that satisfy the specifications I’ve stated.”

models = {"Toyota Corolla","Honda CRV","Chevy Cruze"}

colors = {"White","Grey","Red"}

capacities = {"1.4L","1.6L","1.8L"}

products = [print([model,color,capacity]) for model in models for color in colors for capacity in capacities] 
