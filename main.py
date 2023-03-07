from sklearn import svm
from sklearn import datasets

from iris_classifier import IrisClassifier

iris = datasets.load_iris()
X, y = iris.data, iris.target

clf = svm.SVC(gamma='scale')
clf.fit(X, y)

print("Training Done.")

# Create a iris classifier service instance
iris_classifier_service = IrisClassifier()

# Pack the newly trained model artifact
# 생성한 모델인 clf를 iris_classifier_service에 pack함 (모델 주입)
iris_classifier_service.pack('model', clf)

# Save the prediction service to disk for model serving
# Prediction Serevice를 BENTOML_HOME에 저장하는 코드
save_path = iris_classifier_service.save()
