import pandas as pd

from bentoml import env, artifacts, api, BentoService
from bentoml.adapters import DataframeInput
from bentoml.frameworks.sklearn import SklearnModelArtifact

"""
1. @env 데코레이터
2. @artifacts 데코레이터
    - BentoML에서 미리 만든 artifacts를 사용
    - 여기서 model은 prediction Service Class에서 부를 이름
    - predict 함수에서 self.artifacts.model.predict가 있는데 이 model을 의미함
"""
@env(infer_pip_packages=True)
@artifacts([SklearnModelArtifact("model")])
class IrisClassifier(BentoService):
    """
    A minimum prediction service exposing a Scikit-learn model
    """
    # 데코레이터 설정시 추후 inference API로 만들어줌
    # API의 input, output 설정. batch 유무를 인자로 받을 수 있음
    @api(input=DataframeInput(), batch=True)
    def predict(self, df: pd.DataFrame):
        """
        An inference API named `predict` with Dataframe input adapter, which codifies
        how HTTP requests or CSV files are converted to a pandas Dataframe object as the
        inference API function input
        """
        return self.artifacts.model.predict(df)