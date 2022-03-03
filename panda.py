import tensorflow as tf
# GRADED FUNCTION: train_mnist
def train_mnist():
    # Please write your code only where you are indicated.
    # please do not remove # model fitting inline comments.

    class myCallback(tf.keras.callbacks.Callback):
        def on_epoch_end(self,epoch,logs={}):
            if logs.get('accuracy')>0.99:
                print("end")
                self.model.stop_training=True
    callback=myCallback()
    mnist = tf.keras.datasets.mnist
    (x_train, y_train),(x_test, y_test) = mnist.load_data()
    x_train=x_train/255.0
    y_train=y_train/255.0
    # YOUR CODE SHOULD END HERE
    model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128,activation=tf.nn.relu),
            tf.keras.layers.Dense(10,activation=tf.nn.softmax)
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    # model fitting
    history = model.fit(x_train,
                        y_train,epochs=10,callbacks=[callback]
    )
    # model fitting
    return history.epoch, history.history['acc'][-1]
train_mnist()