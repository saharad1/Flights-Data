import pandas


class Data:
    def __init__(self, path):
        """
        This i the constructor of the class, it reads the data file and makes a dictionary od the data set.
        :param path:
        """
        self.path = path
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient="list")

    def select_features(self, features):
        """
        This function deletes all the features in the dictionary that are not in the input list(features)
        :param features:
        """
        out = []
        for key in self.data.keys():
            if key not in features:
                out.append(key)
        for item in out:
            del self.data[item]
