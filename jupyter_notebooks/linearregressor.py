import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix as cm,f1_score,roc_curve,auc,classification_report

classifier = SVC(kernel = 'linear')

normal_data = np.genfromtxt('/samp_latest_nor.csv',delimiter=',')
attack_data = np.genfromtxt('/test_samp_4.csv',delimiter=',')

'''print(normal_data.shape)
print(attack_data.shape)
print(int(normal_data.size/2))
print(attack_data)'''

normal_class = np.zeros(int(normal_data.size/2))
attack_class = np.ones(int(attack_data.size/2))

'''print("\n")
print(normal_class.shape)
print(attack_class.shape)
print("\n")'''

X = np.append(normal_data,attack_data,axis=0)
Y = np.append(normal_class,attack_class,axis=0)
#X = X[:3000,:3]
print(X.shape)
#Y = Y[:3000]
print(Y.shape)
'''print(X.shape)
print(Y.shape)'''
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.25,random_state=4)

nscatter = plt.scatter(normal_data[:,0],normal_data[:,1],c='b',marker='o')
ascatter = plt.scatter(attack_data[:,0],attack_data[:,1],c='r',marker='x')
plt.legend((nscatter,ascatter),('Normal Traffic','Attack Traffic'))

plt.title('Packet Reception Rate at target Machine')
plt.ylabel('Time in Seconds')
plt.xlabel('Number of Packets')

x = np.linspace(0,20000)
m = 1/200
h = 20
y = m*x+h
d = 0.3
p1 = [80,20000]
p2 = [30,130]
plt.plot(p1,p2,'-k')

plt.show()

X_train = np.logical_not(np.isnan(X_train))
#print(np.isnan(X_train))
#X_train = np.ma.masked_array(X_train,mask=np.isnan(X_train))
#y_train.astype('int64')
#print(X_train.shape,y_train.shape)
#print(np.all(np.isfinite(X_train)),np.any(np.isnan(X_train)))
#print(X_train.filln)
classifier.fit(X_train,y_train)
y_predict=classifier.predict(X_test)
#print(classifier.predict([[4000,32.1482]]))
#print(classifier.predict([[4000,65.4566]]))
print(classification_report(y_test,y_predict))
#print(cm(y_test,y_predict))
x = list( int(x) for x in y_test)
y = list( int(x) for x in y_predict)
print(x)
print(y)
data = { 'y_Actual': x ,'y_Predicted': y}
df = pd.DataFrame(data, columns=['y_Actual','y_Predicted'])
confusion_matrix = pd.crosstab(df['y_Actual'], df['y_Predicted'], rownames=['Actual'], colnames=['Predicted'])
print (confusion_matrix)


svm_fpr, svm_tpr, threshold = roc_curve(y_test,y_predict)
auc_svm = auc(svm_fpr, svm_tpr)

plt.figure(figsize=(5, 5), dpi=100)
plt.plot(svm_fpr, svm_tpr, linestyle='-', label='SVM (auc = %0.3f)' % auc_svm)
plt.xlabel('False Positive Rate -->')
plt.ylabel('True Positive Rate -->')

plt.legend()

plt.show()


