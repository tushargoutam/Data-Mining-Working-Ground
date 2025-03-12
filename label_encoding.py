class Lable_Encoding:

    def __init__(self,data):
        self.data = data

    def basic_encoder(self,feature_name):
        temp = self.data
        from sklearn.preprocessing import LabelEncoder

        b_encoder = LabelEncoder()
        temp[feature_name] = b_encoder.fit_transform(temp[feature_name])

        return temp
        