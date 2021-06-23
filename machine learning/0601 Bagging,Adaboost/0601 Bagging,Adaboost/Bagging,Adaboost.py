import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import tree

from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from mlxtend.plotting import plot_decision_regions
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier


from sklearn.preprocessing import StandardScaler
from matplotlib.colors import ListedColormap
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

C=100
sc= StandardScaler()


pca = PCA(n_components=2) #PCA降維後的特徵維度數目


tree = DecisionTreeClassifier(criterion='entropy',
                                random_state=1,
                                max_depth=None)

bag = BaggingClassifier(base_estimator=tree,n_estimators=500,
                            max_samples=1.0,
                            max_features=1.0,
                            bootstrap=True,
                            bootstrap_features=False,
                            n_jobs=1,
                            random_state=1)

ada = AdaBoostClassifier(base_estimator=tree,n_estimators=500,
                            learning_rate=0.1,
                            random_state=1)

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

def prep(df):
    df = df.dropna()
    df = df.drop(columns = ["price"])
    df = sc.fit_transform(df)
    df = np.array(df)
    return df
x=prep(df)
label =np.array(df["price"])

x_train,x_test,y_train,y_test = train_test_split(x,label,test_size=0.2,random_state=0) #數據分割

x_train = pca.fit_transform(x_train, y_train)
x_test = pca.fit_transform(x_test, y_test)

def result(clf,name):
    formula = clf.fit(x_train,y_train)
    test_p =clf.predict(x_test)
    test_score= accuracy_score(y_test,test_p) 
    print(name,"test =",test_score)


result(tree,"tree")
result(bag,"bag")
result(ada,"ada")

x_min, x_max = x_train[:, 0].min() - 1, x_train[:, 0].max() + 1
y_min, y_max = x_train[:, 1].min() - 1, x_train[:, 1].max() + 1


#xx=x座標 yy=y座標
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1)
                     )

f, axarr = plt.subplots(1, 3, sharex='col', sharey='row', figsize=(8, 3)) #一行畫三張圖

#0,1,2這裡有幾類就填多少
for idx, clf, tt in zip([0,1,2],
                        [tree,bag,ada],
                        ["Decision tree","Bagging","ada"]):
    clf.fit(x_train, y_train)
    x_train= x_test
    y_train = y_test
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    Z = Z.reshape(xx.shape)

    
    cmap_light = ListedColormap(['blue', 'green', 'red']) #調色盤
    
    axarr[idx].pcolormesh(xx, yy, Z,cmap = cmap_light,alpha=0.5) #cmap=cmap_light要寫 不然會隨機顏色
    
    #畫點 幾類就要有幾個idx
    axarr[idx].scatter(x_train[y_train == 0, 0],
                       x_train[y_train == 0, 1],
                       c='blue', marker='^')
    axarr[idx].scatter(x_train[y_train == 1, 0],
                       x_train[y_train == 1, 1],
                       c='green', marker='o')

    axarr[idx].scatter(x_train[y_train == 2, 0],
                       x_train[y_train == 2, 1],
                       c='red', marker='x')

    axarr[idx].set_title(tt)
    

plt.tight_layout()


plt.savefig('result.png', dpi=300, bbox_inches='tight')
plt.show()


