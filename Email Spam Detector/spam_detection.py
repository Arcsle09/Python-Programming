import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn import svm
from sklearn.model_selection import GridSearchCV
import time 

start_time = time.time()
##Step1: Load Dataset
df = pd.read_csv('spam.csv')
print(df.head())

##Step2: Split in to Training and Test Data
x = df['EmailText']
y = df['Label']

x_train,y_train = x[0:4457],y[0:4457]

x_test,y_test = x[4458:],y[4458:]

##Step3: Extract Features
cv = CountVectorizer()
features = cv.fit_transform(x_train)
##Step4: Build a model
#model = svm.SVC()
#Accuracy of the model is: 0.86983842010772
#In order to improve, we will use GridSearchCV
tuned_parameters = {'kernel':['linear','rbf'],'gamma':[1e-3,1e-4],'C':[1,10,100,1000]}
model = GridSearchCV(svm.SVC(),tuned_parameters)
model.fit(features,y_train)
print(model.best_params_)
##Step5: Test Accuracy
features_test = cv.transform(x_test)
print('Accuracy of the model is:',model.score(features_test,y_test))

end_time = time.time() - start_time

print('Finished in',end_time,'seconds')

##output:
#{'C': 1000, 'gamma': 0.0001, 'kernel': 'rbf'}
#Accuracy of the model is: 0.9865350089766607
#Finished in 108.60660099983215 seconds
