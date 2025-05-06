class Lable_Encoding:

    def __init__(self,data):
        self.data = data

    def basic_encoder(self,feature_name):
        """
                Applies basic label encoding to a single categorical feature.

                Parameters:
                -----------
                feature_name : str
                    The name of the feature/column to encode.

                Returns:
                --------
                pandas.DataFrame
            DataFrame with the encoded feature.
        """
        temp = self.data
        from sklearn.preprocessing import LabelEncoder

        b_encoder = LabelEncoder()
        temp[feature_name] = b_encoder.fit_transform(temp[feature_name])

        return temp

    def hot_encoder(self,feature_name):
        """
            Applies one-hot encoding to a single categorical feature.

            Parameters:
            -----------
            feature_name : str
                The name of the feature/column to encode.

            Returns:
            --------
            pandas.DataFrame
                DataFrame with one-hot encoded columns.
        """
        temp = self.data
        from sklearn.preprocessing import OneHotEncoder

        h_encoder = OneHotEncoder(sparse_output=False) 
        temp[feature_name] = h_encoder.fit_transform(temp[feature_name])

        return temp

    def manual_encoder(self,feature_name):
        """
            Placeholder for manual encoding using a custom dictionary mapping.
            You need to define your own dictionary to map values manually.

            Parameters:
            -----------
            feature_name : str
                The name of the feature/column to encode.

            Returns:
            --------
            pandas.DataFrame
                DataFrame with manually mapped values.
        """
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
    

    def ordinal_encoding(self,feature_name,sequence):
        """
            Applies ordinal encoding with a custom sequence.

            Parameters:
            -----------
            feature_name : str
                The name of the feature/column to encode.
            sequence : list of lists
                Ordered list of categories for encoding.

            Returns:
            --------
            pandas.DataFrame
                DataFrame with ordinal encoded values.
        """
        from sklearn.preprocessing import OrdinalEncoder

        temp = self.data

        encoder = OrdinalEncoder(categories=sequence)
        temp[feature_name] = encoder.fit_transform(temp[feature_name])

        return temp 
    

    def target_based_encoding(self,feature_name,target):
        """
            Encodes the feature using the mean of the target variable.

            Parameters:
            -----------
            feature_name : str
                The categorical feature to encode.
            target : str
                The target variable name used for encoding.

            Returns:
            --------
            pandas.DataFrame
            DataFrame with target-encoded feature.
        """
        temp = self.data
        mean_target = temp.groupby(feature_name)[target].mean()
        temp[feature_name] = temp[feature_name].map(mean_target)
        return temp
    

    def frequency_encoding(self,feature_name):
        """
            Encodes categories by their frequency in the dataset.

            Parameters:
            -----------
            feature_name : str
                The feature to encode.

            Returns:
            --------
            pandas.DataFrame
                DataFrame with frequency-encoded feature.
        """
        temp = self.data
        temp[feature_name] = temp[feature_name].map(temp[feature_name].value_counts())

        return temp
    

    def binary_encoder(self,feature_name):
        """
            Applies binary encoding to a categorical feature.

            Parameters:
            -----------
            feature_name : str
                The name of the feature/column to encode.

            Returns:
            --------
            pandas.DataFrame
                DataFrame with binary encoded columns.
        """

        import category_encoders as ce

        temp = self.data

        encoder = ce.BinaryEncoder(cols=['Category'])

        temp[feature_name] = encoder.fit_transform(temp[feature_name])

        return temp
    

    def hash_encoding(self,feature_name):

        """
            Applies hashing encoding to a categorical feature using a fixed number of components.

            Parameters:
            -----------
            feature_name : str
                The name of the feature/column to encode.

            Returns:
            --------
            pandas.DataFrame
                DataFrame with hash encoded columns.
        """
        import category_encoders as ce

        temp = self.data

        encoder = ce.HashingEncoder(cols = ['Category'], n_components = 3)

        temp[feature_name] = encoder.fit_transform(temp[feature_name])

        return temp    

    