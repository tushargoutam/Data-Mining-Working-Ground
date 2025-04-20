class Lable_Encoding:

    def __init__(self,data):
        self.data = data

    def basic_encoder(self,feature_name):
        temp = self.data
        from sklearn.preprocessing import LabelEncoder

        b_encoder = LabelEncoder()
        temp[feature_name] = b_encoder.fit_transform(temp[feature_name])

        return temp

    def hot_encoder(self,feature_name):
        temp = self.data
        from sklearn.preprocessing import OneHotEncoder

        h_encoder = OneHotEncoder(sparse_output=False) 
        temp[feature_name] = h_encoder.fit_transform(temp[feature_name])

        return temp

    def manual_encoder(self,feature_name):
        temp = self.data
        unq = temp[feature_name].unique()
        dictonary = {}
        for unq_ele in unq:
            # for every unique element get mapping
            # map = value.get() from web page
            # dictonary[uni_ele] = map
            pass

        temp[feature_name] = temp[feature_name].map(dictonary)

        return temp 
    

    