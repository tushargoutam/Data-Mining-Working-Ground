class Treating_outliers:

    def __init__(self,data,target_variable):
        self.data = data
        self.target_variable = target_variable

    def outliers_deletion(self):
        '''
            Removes outliers from the dataset using the Interquartile Range (IQR) method.
        
            This method calculates the first quartile (Q1) and third quartile (Q3) of the
            target variable to determine the interquartile range (IQR). It then defines 
            lower and upper bounds as:

                Lower Bound = Q1 - 1.5 * IQR
                Upper Bound = Q3 + 1.5 * IQR

            Any data points outside these bounds are considered outliers and removed
            from the dataset.

            Returns:
                pd.DataFrame: A DataFrame with outliers removed.

        '''
        # Calculating lower and upper quantiles 
        q1 = self.data[self.target_variable].quantile(0.25)
        q3 = self.data[self.target_variable].quantile(0.75)

        # calculating Inter Quantile Range for Calculating Upper_Extreme and Lower_Extreme
        iqr = q3-q1

        #Lower Extreme
        lower_extreme = q1 - (1.5*iqr)
        upper_extreme = q3 + (1.5*iqr)
        # Getting Number of rows and creating a list to store dorpping index
        dim = self.data.shape[0]
        drop_indexs = []

        #getting all the indexes where Outliers exists
        for i in range(dim):
            val = self.data[self.target_variable][i]
            if val> upper_extreme or val<lower_extreme:
                drop_indexs.append(i)

        #dropping the rows with outliers
        self.data = self.data.drop(self.data.index[drop_indexs])

        return self.data
    
    def outliers_imputation_mean(self):
        '''
            Removes outliers from the dataset using the Interquartile Range (IQR) method.
        
            This method calculates the first quartile (Q1) and third quartile (Q3) of the
            target variable to determine the interquartile range (IQR). It then defines 
            lower and upper bounds as:

                Lower Bound = Q1 - 1.5 * IQR
                Upper Bound = Q3 + 1.5 * IQR

            Any data points outside these bounds are considered outliers and are replaced with
            the mean of the target variable.

            Returns:
                pd.DataFrame: A DataFrame with outliers removed.

        '''
        # Calculating lower and upper quantiles 
        q1 = self.data[self.target_variable].quantile(0.25)
        q3 = self.data[self.target_variable].quantile(0.75)

        # calculating Inter Quantile Range for Calculating Upper_Extreme and Lower_Extreme
        iqr = q3-q1

        #Lower Extreme
        lower_extreme = q1 - (1.5*iqr)
        upper_extreme = q3 + (1.5*iqr)

        #Getting Dimension of data
        dim = self.data.shape[0]
        avg = self.data[self.target_variable].mean()


        # Replacing outliers with mean
        for i in range(dim):
            val = self.data[self.target_variable][i]
            if val>upper_extreme or val<lower_extreme:
                self.data.loc[i,self.target_variable] = avg

        return self.data 
    
    def outliers_imputation_median(self):
        '''
            Removes outliers from the dataset using the Interquartile Range (IQR) method.
        
            This method calculates the first quartile (Q1) and third quartile (Q3) of the
            target variable to determine the interquartile range (IQR). It then defines 
            lower and upper bounds as:

                Lower Bound = Q1 - 1.5 * IQR
                Upper Bound = Q3 + 1.5 * IQR

            Any data points outside these bounds are considered outliers and are replaced with
            the median of the target variable.

            Returns:
                pd.DataFrame: A DataFrame with outliers removed.

        '''
        # Calculating lower and upper quantiles 
        q1 = self.data[self.target_variable].quantile(0.25)
        q3 = self.data[self.target_variable].quantile(0.75)

        # calculating Inter Quantile Range for Calculating Upper_Extreme and Lower_Extreme
        iqr = q3-q1

        #Lower Extreme
        lower_extreme = q1 - (1.5*iqr)
        upper_extreme = q3 + (1.5*iqr)

        
        #Getting Dimension of data
        dim = self.data.shape[0]
        avg = self.data[self.target_variable].median()


        # Replacing outliers with median
        for i in range(dim):
            val = self.data[self.target_variable][i]
            if val>upper_extreme or val<lower_extreme:
                self.data.loc[i,self.target_variable] = avg

        return self.data 
    
    def outliers_capping(self):

        '''
            Caps outliers in the target variable using the Interquartile Range (IQR) method.

            This method identifies outliers by calculating the first quartile (Q1) and third quartile (Q3) 
            to determine the interquartile range (IQR). The lower and upper bounds for outlier detection are:

                Lower Bound = Q1 - 1.5 * IQR
                Upper Bound = Q3 + 1.5 * IQR

            Any values lower than the lower bound are replaced with the lower bound, 
            and any values higher than the upper bound are replaced with the upper bound.

            Returns:
                pd.DataFrame: A DataFrame with outliers capped within the lower and upper extreme values.
        
        '''

        # Calculating lower and upper quantiles
        q1 = self.data[self.target_variable].quantile(0.25)
        q3 = self.data[self.target_variable].quantile(0.75)

        # calculating Inter Quantile Range for Calculating Upper_Extreme and Lower_Extreme
        iqr = q3-q1

        #Lower Extreme
        lower_extreme = q1 - (1.5*iqr)
        upper_extreme = q3 + (1.5*iqr)

        #getting the dimension
        dim = self.data.shape[0]

        #Replacing value lower than lower_extreme with lower_extreme
        #Replacing value higer that upper_extreme with upper_extrme

        for i in range(dim):
            val = self.data[self.target_variable][i]

            if val<lower_extreme:
                self.data.loc[i,self.target_variable] = lower_extreme

            if val>upper_extreme:
                self.data.loc[i,self.target_variable] = upper_extreme

        
        return self.data
    
    def outliers_log10_transformation(self):
        '''
            Applies a base-10 logarithmic transformation to the target variable in the dataset.

            This transformation is useful for reducing skewness in positively skewed data. However, 
            it should not be applied if the target variable contains zero or negative values, 
            as logarithms values are negative for such values.

            Returns:
                pandas.DataFrame: The dataset with the target variable transformed using log base 10.
        '''
        import numpy as np
        # Replacing all the values with logbase10 values
        self.data[self.target_variable] = np.log10(self.data[self.target_variable])
        return self.data
    
    def outliers_binning(self):
        '''
            Performs outlier detection, scaling, and imputation on the target variable to enhance data quality.

            This method applies robust statistical techniques to handle outliers and missing values, ensuring 
            the dataset is well-prepared for downstream analysis or modeling.

            Processing Steps:
            1. **Outlier Detection and Handling**:
            - Computes the interquartile range (IQR) to identify potential outliers.
            - Defines lower and upper bounds using the 1.5 * IQR rule.
            - Replaces detected outliers with NaN values.

            2. **Data Scaling**:
            - Applies `RobustScaler` to mitigate the influence of outliers while preserving the data distribution.

            3. **Missing Value Imputation**:
            - Uses `KNNImputer` with k=5 to estimate and replace missing values based on nearest neighbors.

            4. **Inverse Transformation**:
            - Restores the scaled values back to their original range using inverse transformation.

            Returns:
                pd.DataFrame: The processed dataset with outliers addressed and missing values imputed.

            Notes:
            - The function operates on `self.data`, modifying the target variable (`self.target_variable`) in place.
            - It assumes `self.target_variable` is numeric and free of categorical or non-continuous values.
            - If the target variable contains pre-existing NaN values, they will also be imputed.
            - This method is particularly effective for datasets with skewed distributions and extreme values.
                
        '''

        import pandas as pd
        import numpy as np
        from sklearn.preprocessing import RobustScaler
        from sklearn.impute import KNNImputer
        # Calculating lower and upper quantiles 
        q1 = self.data[self.target_variable].quantile(0.25)
        q3 = self.data[self.target_variable].quantile(0.75)

        # calculating Inter Quantile Range for Calculating Upper_Extreme and Lower_Extreme
        iqr = q3-q1

        #Lower Extreme
        lower_extreme = q1 - (1.5*iqr)
        upper_extreme = q3 + (1.5*iqr)

        
        #Getting Dimension of data
        dim = self.data.shape[0]

        #The data should contain no missing value priorly
        #Changing every outlier value to null Value
        for i in range(dim):
            val = self.data[self.target_variable][i]
            if val<lower_extreme or val>upper_extreme:
                self.data.loc[i,self.target_variable] = np.nan


        #Applying RobustScaler to handle Outliers
        scaler = RobustScaler()
        scaled_data = scaler.fit_transform(self.data[[self.target_variable]])
        scaled_df = pd.DataFrame(scaled_data,columns = [self.target_variable])
        
        #Createing a KNNImputer instance
        knn_imputer = KNNImputer(n_neighbors=5)
        
        #Using KNNImputer to impute missing Values
        imputed_data = knn_imputer.fit_transform(scaled_df)
        imputed_df = pd.DataFrame(imputed_data,columns=scaled_df.columns)

        #Inverse transforming to get back the original data
        original = scaler.inverse_transform(imputed_df)
        orignial_df = pd.DataFrame(original,columns = [self.target_variable])

        self.data[self.target_variable] = orignial_df[[self.target_variable]]

        return self.data






import pandas as pd  
data = pd.read_csv('Raw_Housing_Prices.csv')
outlier_treatment = Treating_outliers(data,"Sale Price")

print("Data Information Before Outlier deletion")
print("Rows",data.shape[0])
print("Min of Target Variable",min(data['Sale Price']))
print("Max of Target Variable",max(data['Sale Price']))
print("Measure of Central Tendencies")
print(data.describe())

data = outlier_treatment.outliers_deletion()

print("Data Information after Outlier deletion")
print("Rows",data.shape[0])
print("Min of Target Variable",min(data['Sale Price']))
print("Max of Target Variable",max(data['Sale Price']))
print("Measure of Central Tendencies")
print(data.describe())

