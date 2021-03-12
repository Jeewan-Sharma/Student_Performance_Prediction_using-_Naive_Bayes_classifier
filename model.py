import pandas

#importing datas
dx = pandas.read_csv(r"F:/programme/Minor/student-math.csv", sep = ';')
dp = pandas.read_csv(r"F:/programme/Minor/student-port.csv", sep = ';')

# merge datasets
d = pandas.concat([dx,dp])

#droping the rows of student not appearing the any exam (i.e. scoring zero)
d = d.drop(d[d.G1 == 0].index)
d = d.drop(d[d.G2 == 0].index)
d = d.drop(d[d.G3 == 0].index)

#calculating the value of mean in each period for replacing the zero by mean.
m_g1 = d['G1'].mean()
m_g2 = d['G2'].mean()
m_g3 = d['G3'].mean()

#importing again the original data
dx = pandas.read_csv(r"F:/programme/Minor/student-math.csv", sep = ';')
dp = pandas.read_csv(r"F:/programme/Minor/student-port.csv", sep = ';')

# merge datasets
d = pandas.concat([dx,dp])

# 2. replacing the zero value of period by mean of each:
d['G1'] = d['G1'].replace(0, m_g1)
d['G2'] = d['G2'].replace(0, m_g2)
d['G3'] = d['G3'].replace(0, m_g3)

# convert G3 to categorical variable # Good:15~20 Fair:10~14 Poor:0~9
d['final_grade'] = 'na'
d.loc[(d.G3 >= 15) & (d.G3 <= 20), 'final_grade'] = 'good' 
d.loc[(d.G3 >= 10) & (d.G3 <= 14), 'final_grade'] = 'fair' 
d.loc[(d.G3 >= 0 ) & (d.G3 <= 9 ), 'final_grade'] = 'poor'

# 1. Removing the undesired attributes
d = d.drop(['school','sex','address','famsize','Pstatus','Mjob','Fjob','reason','guardian','studytime','nursery','higher','romantic','famrel','G3'], axis = 1)

# 2. normalization
# normalization function
def replace_yn(val):
    if val == 'no':
        return 0
    else:
        return 1
    
# normalizing the data (1 for yes & 0 for no)
d['famsup']     = d['famsup'].apply(replace_yn, 1)
d['schoolsup']  = d['schoolsup'].apply(replace_yn, 1)
d['paid']       = d['paid'].apply(replace_yn, 1)
d['internet']   = d['internet'].apply(replace_yn, 1)
d['activities'] = d['activities'].apply(replace_yn, 1)

y = d.final_grade
x = d.drop('final_grade', axis = 1)
#ydm = ydm.astype('int') # since, gnb.fit(xdm_train, ydm_train) takes only int

#splitting the data into train and test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
scalerx = StandardScaler()
scalery = StandardScaler()
x_train = scalerx.fit_transform(x_train)
x_test  = scalery.fit_transform(x_test)

#Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB

#Create a Gaussian Classifier
gnb = GaussianNB()

#Train the model using the training sets
gnb.fit(x_train, y_train)

#Predict the response for test dataset
y_pred = gnb.predict(x_test)

#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics

# Model Accuracy, how often is the classifier correct?
print("Merge-Accuracy\n:",metrics.accuracy_score(y_test, y_pred))

import pickle

#saving the model
naivebayes = 'NaiveBayesM.sav'
pickle.dump(gnb, open(naivebayes, 'wb'))

def get_input(data) ->int:
    import pandas
    df = pandas.DataFrame(data = data,index = [0])
    df = scalerx.transform(df)
    gnb = pickle.load(open(naivebayes, 'rb'))
    p = gnb.predict(df)
    if p == 'poor':
        return 0
    elif p == 'fair':
        return 1
    else:
        return 2