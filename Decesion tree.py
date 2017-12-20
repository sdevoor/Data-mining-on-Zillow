import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

import matplotlib.pyplot as plt
file_path = 'G:\EE 608\Project\merged.csv'

try:
    df = pd.read_csv(file_path)
except OSError:
    pass

train=df.sample(frac=0.7,random_state=200)
test=df.drop(train.index)

def concat(city, zipcode):
    city_de = city + ' : ' + zipcode
    return city_de

def getcity(table):
    city_details = []
    a=[]
    for row in table.itertuples():
        city_details= concat(str(row[3]), str(row[11]))
        a.append(city_details)
    return a

   

def model(train_city, test_city, train_df, test_df):
    counter = CountVectorizer()
    counter.fit(train_city)
    
    counts_train = counter.transform(train_city)
    counts_test = counter.transform(test_city)
    
    dst=DecisionTreeClassifier()
    #dst=KNeighborsClassifier(n_neighbors=3)
    dst.fit(counts_train.todense(),train_df['range'])
    pred=dst.predict(counts_test.todense())
    print(pred)
    accuracy=accuracy_score(pred, test_df['range'])
    print('Accuracy of Decision Tree')
    print(accuracy)
    
train_city_details = getcity(train)
test_city_details = getcity(test)

model(train_city_details, test_city_details, train, test)

#Histogram Plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
#ax.hist(df[' lastSoldPrice'], bins = 10)
ax.scatter(df[' lotSizeSqFt'],df[' lastSoldPrice'])
plt.title('Lost Size VS House price')
plt.xlabel('Lot Size')
plt.ylabel(' Last Sold Price ')
plt.show()
