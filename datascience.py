import tensorflow as tf
from sklearn.datasets import  load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

iris = load_iris()
x = iris.data
y = iris.target

enc = OneHotEncoder()

y = enc.fit_transform(y.reshape(-1,1)).toarray()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = tf.keras.models.Sequential([
tf.keras.layers.Dense (10, activation='relu', input_shape=(4,)),
tf.keras.layers. Dense (10, activation='relu'),
tf.keras.layers.Dense(3, activation='softmax')
 ])

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=['accuracy'])

model.fit(x_train, y_train, epochs=50, batch_size=1, verbose=1)


loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
print("Précision du modèle: (2)%",format(accuracy * 100))
