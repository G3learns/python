import numpy as np
def sigmoid(z):
  return 1/(1+np.exp(-z))
def derv_sigmoid(dz):
  return (np.exp(-dz)/((1+np.exp(-dz))**2))
def MSEloss(y,yp):
  return np.sum(np.square(y-yp))/yp.shape[0]
def derv_MSEloss(y,yp):
  return 2*(y-yp)
def cross_entropy(y,yp):
  return np.mean(np.multiply(y,np.log2(yp))+np.multiply((1-y),np.log2(1-yp)))
def derv_cross_entropy(y,yp):
  return np.sum((yp-y)/yp*(1-yp))
class FullyConnectedLayer(object):
  def __init__(self,input,hidden,activation_function,derv_acti=None):
    super().__init__()
    self.w=np.random.standard_normal((input,hidden))
    self.b=np.random.standard_normal(hidden)
    self.activation_function=activation_function
    self.derv_acti=derv_acti
    self.size=hidden
    self.x,self.y=None,None
    self.dL_dw,self.dL_db=None,None
  
  def forward(self,x):
    self.x=x
    z=np.dot(x,self.w)+self.b
    self.y= self.activation_function(z)
    return self.y
  
  def backward(self,dy_dz):
    dL_dy=self.derv_acti(self.y)
    dL_dz=dL_dy*dy_dz
    dz_dw=self.x
    dz_dx=self.w
    dz_db=np.ones(dL_dz.shape[0])
    self.dL_dw=np.dot(dz_dw.T,dL_dz)
    self.dL_db=np.dot(dz_db,dL_dz)
    dL_dx=np.dot(dz_dx.T,dL_dz)
    return dL_dx

  def optimize(self,epsilon):
    self.w-=epsilon*self.dL_dw
    self.b-=epsilon*self.dL_db
class SimpleNeuralNetwork(object):
  def __init__(self,input,output,layer=(64,32),actfun=sigmoid,dervact=derv_sigmoid,lossfun=MSEloss,dervloss=derv_MSEloss):
    super().__init__()
    layersize=[input,*layer,output]
    self.layer=[
                FullyConnectedLayer(layersize[i],layersize[i+1],actfun,dervact) for i in range(len(layersize)-1)]
    self.lossfun=lossfun
    self.dervloss=dervloss
  
  def forward(self,x):
    for i in self.layer:
      x=i.forward(x)
    return x

  def predict(self,x):
    y=self.forward(x)
    chosen=np.argmax(y,0)
    return chosen
  
  def backward(self,dL_dy):
    for i in reversed(self.layer):
      dL_dy=i.backward(dL_dy)

  def optimize(self,epsilon):
    for i in reversed(self.layer):
      i.optimize(epsilon)

  def evaluate_accuracy(self,x,y):
    accuracy=0
    for i in range(len(x)):
      yp=self.predict(x[i])
      if y[i]==yp:
        accuracy+=1
    return accuracy/len(x)
  def train(self,xtrain,ytrain,xval,yval,batchsize=32,epoch=5,learningrate=5e-3):
    batchnum=len(xtrain)//batchsize
    losses,accuracies=[],[]
    for i in range(epoch):
      epochloss=0
      for b in range(batchnum):
        batchbegin=b*batchsize
        batchend=batchbegin+batchsize
        x=xtrain[batchbegin:batchend]
        yp=ytrain[batchbegin:batchend]
        y=self.forward(x)
        loss=self.lossfun(y,yp)
        dy_dz=self.dervloss(y,yp)
        self.backward(dy_dz)
        self.optimize(learningrate)
        epochloss+=loss
      epochloss/=batchnum
      loss.append(epochloss)
      accuracy=self.evaluate_accuracy(xval,yval)
      accuracies.append(accuracy)
    return losses,accuracy

from matplotlib import pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
mnist=fetch_openml('mnist_784', cache=False)
x=mnist.data.astype('float32')
y=mnist.target.astype('int64')
x/=255.0
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=42)
y_train = np.eye(10)[y_train]

