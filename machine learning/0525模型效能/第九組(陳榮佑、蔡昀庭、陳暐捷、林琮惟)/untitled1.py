import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import tree

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
#
df=pd.read_csv("./diamonds.csv")
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
df = df.drop(['depth', 'table', 'x', 'y', 'z'], axis=1)
#
labelencoder = LabelEncoder()
data_le=pd.DataFrame(df)
data_le['cut'] = labelencoder.fit_transform(data_le['cut'])
data_le['color'] = labelencoder.fit_transform(data_le['color'])
data_le['clarity'] = labelencoder.fit_transform(data_le['clarity'])
data_le['carat'] = labelencoder.fit_transform(data_le['carat'])
# data_le['depth'] = labelencoder.fit_transform(data_le['depth'])
# data_le['table'] = labelencoder.fit_transform(data_le['table'])
# data_le['x'] = labelencoder.fit_transform(data_le['x'])
# data_le['y'] = labelencoder.fit_transform(data_le['y'])
# data_le['z'] = labelencoder.fit_transform(data_le['z'])
#
price = [0,1,1000,5000,10000,15000,20000]
data_le['price'] = pd.cut(data_le['price'],price,labels=[0,1,2,3,4,5])
data_le = data_le[data_le['price']!=0]

x = np.array(data_le.drop(['price'], axis=1))
y = np.array(data_le['price'])
label =np.array(df["price"])

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


x_train,x_test, y_train, y_test =train_test_split(x,y,test_size=0.455, random_state=0)


def main(df):
    df = df.dropna()
    df = df.drop(columns = ['price'])
    df = sc.fit_transform(df)
    Churnlist = label.tolist()
    x = np.array(df)
    y = np.array(Churnlist)
    gini(x,y)
    
def gini(x,y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 0, stratify = y)
    gini = tree.DecisionTreeClassifier(criterion = "gini", random_state = 0)
    gini.fit(x_train, y_train)
    confusion_matrix_table(gini, x_test, y_test)
    
def confusion_matrix_table(model, x_test, y_test):
    arr = []; sum = 0; stt = []
    y_pred = model.predict(x_test)
    labels = list(set(y_test))
    cm = confusion_matrix(y_test, y_pred)
    
    arr.append("")
    for j in range(0, len(labels)):
        arr.append(str(labels[j]))
    stt.append(arr)
    
    for j in range(len(cm)):
        arr=[]
        arr.append(str(j))
        for k in range(len(cm[j])):
            arr.append(str(cm[j][k]))
            sum += int(cm[j][k])
        stt.append(arr)
    
    acc = accuracy_score(y_test, y_pred)
    pre = precision_score(y_test, y_pred, average = 'weighted')
    recall = recall_score(y_test, y_pred, average = 'weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    # print(cm)
    
    stt.append([])
    stt.append(["Total amount", sum])
    stt.append(["Accuracy", acc])
    stt.append(["Precision", pre])
    stt.append(["Recall", recall])
    stt.append(["F1", f1])
    # data = pd.DataFrame(stt, columns = [' '] * 3)
    # data.to_csv('result.csv', index = False)
    for i in stt:
        print(i)

main(df)

