from typing import List, Union
import pickle
import warnings

warnings.filterwarnings('ignore', category=UserWarning, append=True)


class Model:

    def __init__(self):
        with open('model.pickle', 'rb') as f:
            self.clf = pickle.load(f)

    def predict_proba(self, x: List[List[Union[int, float]]]) -> List[float]:
        """
        Predict the probability of each class for a given input sample.

        Parameters
        ----------
        x : List[List[Union[int, float]]]
            The input sample, represented as a list of integers or floats.

        Returns
        -------
        List[float]
            The probability of each class for the input sample.
        """
        return self.clf.predict_proba(x)

    def predict(self, x: List[List[Union[int, float]]]) -> List[float]:
        """
        Predict the class for a given input sample.

        Parameters
        ----------
        x : List[List[Union[int, float]]]
            The input sample, represented as a list of lists of integers or floats.

        Returns
        -------
        List[float]
            The predicted class for each input sample.
        """
        return self.clf.predict(x)


if __name__ == '__main__':
    model = Model()
    print(model.predict([[21, 1, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]))
