import pandas as pd
import matplotlib.pyplot as plt  

def plot_regression_line(X,m,b):
	regression_x = X.values
	regression_y = []
	for x in regression_x:
		y = m*x + b
		regression_y.append(y)

	plt.plot(regression_x,regression_y)
	plt.pause(1)

##Step 1: Read the CSV file and plot
df = pd.read_csv('student_scores.csv')

x = df['Hours']
y = df['Scores']

plt.plot(x,y,'*')


##Step2: Def a func grad_desc such that it takes m,b and returns a better value of m,b 
##so that the error reduces

m = 0

b = 0

def grad_desc(x,y,m,b):
    for point in zip(x,y):
        x = point[0]
        y_actual = point[1]
        y_prediction = m*x + b
        error = y_prediction - y_actual
        delta_m = -1*(error*x)*0.0005
        delta_b = -1*(error)*0.0005
        m = m + delta_m 
        b = b + delta_b 
    return m,b
for i in range(0,10):
    m,b = grad_desc(x,y,m,b)
    print("slope: ",m)
    print("Intersect: ",b)
    plot_regression_line(x,m,b)
    
plt.show()

#Learning rate is 0.0005
#slope:  3.2787698956535585
#Intersect:  0.5324586229347614
#slope:  5.473679350461276
#Intersect:  0.8894634649470654
#slope:  6.942990209497915
#Intersect:  1.1290080963087354
#slope:  7.926543652983409
#Intersect:  1.2899167671814629
#slope:  8.584903225319987
#Intersect:  1.398180677166502
#slope:  9.025559440552358
#Intersect:  1.4711998402733362
#slope:  9.320472659457623
#Intersect:  1.5206228344396873
#slope:  9.517817305158756
#Intersect:  1.5542478939510072
#slope:  9.649844119678608
#Intersect:  1.5772956105579505
#slope:  9.738143612786182
#Intersect:  1.5932609531456048
