import bentoml

iris = bentoml.sklearn.get('iris_clf:latest').to_runner()
iris.init_local()
print(iris.predict.run([[5.9, 3., 5.1, 1.8]]))