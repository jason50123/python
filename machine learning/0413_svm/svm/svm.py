import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from mlxtend.plotting import plot_decision_regions
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

C=100
sc= StandardScaler()
#有0的資料全部刪掉,並且提出'district','rps01','rps11','rps13','rps22'作參考
df=pd.read_csv("diamonds.csv")
df = df[['carat','cut','color','clarity','price']]
df = df.fillna(0)

cut_mapping = {
    'Very Good':0,
    'Good':1,
    'Premium':2,
    'Ideal':3,
    'Fair':4
    }
df['cut']=df['cut'].map(cut_mapping)


color_mapping = {
    'D':0,
    'G':1,
    'F':2,
    'H':3,
    'J':4,
    'I':5,
    'E':6
    }
df['color']=df['color'].map(color_mapping)


clarity_mapping = {
    'VVS2':0,
    'VVS1':1,
    'VS2':2,
    'VS1':3,
    'SI2':4,
    'SI1':5,
    'I1':6
    }
df['clarity']=df['clarity'].map(clarity_mapping)
# df = df.drop(['depth', 'table', 'x', 'y', 'z'], axis=1)
#
#改名目變數
labelencoder = LabelEncoder()
data_le=pd.DataFrame(df)
data_le['carat'] = labelencoder.fit_transform(data_le['carat'])
data_le['cut'] = labelencoder.fit_transform(data_le['cut'])
data_le['color'] = labelencoder.fit_transform(data_le['color'])
data_le['clarity'] = labelencoder.fit_transform(data_le['clarity'])
#設區間,價格等於0刪掉
price = [0,1,1000,5000,10000,15000,20000]
data_le['price'] = pd.cut(data_le['price'],price,labels=[0,1,2,3,4,5])
data_le = data_le[data_le['price']!=0]

x = np.array(data_le.drop(['price'], axis=1))
y = np.array(data_le['price'])
#分割資料,訓練,測試
def p_d_r(clf,x_train,y_train):
    value=1
    width=10
    plot_decision_regions(
    x_train,
    y_train,
    clf=clf,
    filler_feature_values={0: value, 1: value, 2:value, 3:value},
    filler_feature_ranges={0: width, 1: width, 2:width, 3:width}
    )
    plt.ylim(-1, 4)
    plt.xlim(-1, 12)
    plt.show()
    plt.clf()


X_train,X_test, y_train, y_test =train_test_split(x,y,test_size=0.455, random_state=0)

### SVM------------------------------------------------------------------------------------------------------
svm=SVC(kernel='linear',C=C,random_state=0)
svm.fit(X_train,y_train)
print("svm.score=",svm.score(X_train,y_train))

p_d_r(svm,X_train,y_train)
####### LOGISTIC-------------------------------------------------------------------------------------------------
logistic= LogisticRegression(C=C,
                        solver="lbfgs",
                        multi_class="ovr",                        
                        max_iter=500
                        )
logistic.fit(X_train,y_train)
print("羅吉斯score=",logistic.score(X_train,y_train))

p_d_r(logistic,X_train,y_train)
###### KNN-------------------------------------------------------------------------------------------
knn = KNeighborsClassifier(n_neighbors=5,p=2,metric='minkowski')
knn.fit(X_train,y_train)
print("knn.score=",knn.score(X_train,y_train))

p_d_r(knn,X_train,y_train)

