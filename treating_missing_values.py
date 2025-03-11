class Treating_Missing_Values:

    def __init__(self,data,target_variable):
        self.data = data
        self.target_variable = target_variable

    def display_missing_value(self):
        '''
            Display the count of missing values for each column in the dataset.

            This method returns a list of lists, where each sublist contains a column name 
            and the corresponding count of missing (NaN) values in that column. 
            It provides a quick summary of missing data in the dataset.

            Returns
            -------
            list of list and total percentage of missing values
                A list of `[column_name, missing_value_count]` pairs.
                Toltal Percentage of Missing Values in whole data.

            Notes
            -----
            - This method helps in identifying columns with missing values, allowing 
            informed decisions about imputation or deletion strategies.
            - If no missing values are present, the function will return counts of `0` 
            for all columns.

            Examples
            --------
            >>> import pandas as pd
            >>> data = pd.DataFrame({
            ...     'A': [1, 2, None, 4],
            ...     'B': [10.5, None, 30.2, 40.1],
            ...     'C': ['x', 'y', 'z', None]
            ... })
            >>> treatment = Treating_Missing_Values(data, target_variable='A')

            # Display missing values per column
            >>> missing_values = treatment.display_missing_value()
            >>> print(missing_values)
            [['A', 1], ['B', 1], ['C', 1]]
        '''
        total_missing = ((self.data.isnull().sum().sum())/(self.data.shape[0]*self.data.shape[1]))*100
        return [[column,null_values] for column,null_values in zip(self.data.columns,list(self.data.isnull().sum()))],total_missing

    def missing_value_deletion_byrow(self):
        '''
            Remove rows containing missing values from the dataset.

            This method drops all rows that contain at least one missing (NaN) value.
            It is a simple yet aggressive approach to handling missing data, as it removes
            entire records that contain incomplete information.

            Returns
            -------
            pd.DataFrame
                The modified DataFrame with rows containing missing values removed.

            Notes
            -----
            - This method should be used with caution, as dropping rows can lead to 
            data loss, especially if missing values are present in a significant 
            portion of the dataset.
            - If all rows contain at least one missing value, the resulting DataFrame 
            will be empty.

            Examples
            --------
            >>> import pandas as pd
            >>> data = pd.DataFrame({
            ...     'A': [1, 2, None, 4],
            ...     'B': [10.5, None, 30.2, 40.1],
            ...     'C': ['x', 'y', 'z', None]
            ... })
            >>> treatment = Treating_Missing_Values(data, target_variable='A')

            # Remove all rows with at least one missing value
            >>> cleaned_data = treatment.missing_value_deletion_byrow()
        '''
        #Dropping every row that has even one missing value
        self.data.dropna(inplace=True,axis=0)
        return self.data
    
    def missing_value_deletion_bycolumn(self,column_name = None):
        '''
            Remove columns with missing values from the dataset.

            This method deletes columns containing missing values based on the provided criteria:
            
            - If `column_name` is `None` (default), it drops all columns that contain at least one missing value.
            - If a specific column name or a list of column names is provided, only those columns are dropped.

            Parameters
            ----------
            column_name : str, list of str, or None, optional
                The name or list of names of columns to drop. If `None`, all columns 
                containing missing values are removed. Default is `None`.

            Returns
            -------
            pd.DataFrame
                The modified DataFrame with the specified columns removed.

            Raises
            ------
            KeyError
                If any specified column in `column_name` does not exist in the DataFrame.

            Examples
            --------
            >>> import pandas as pd
            >>> data = pd.DataFrame({
            ...     'A': [1, 2, None, 4],
            ...     'B': [None, 2, 3, 4],
            ...     'C': [1, None, 3, 4]
            ... })
            >>> treatment = Treating_Missing_Values(data, target_variable='A')

            # Drop all columns with missing values
            >>> cleaned_data = treatment.missing_value_deletion_bycolumn()

            # Drop specific columns 'A' and 'B'
            >>> cleaned_data = treatment.missing_value_deletion_bycolumn(['A', 'B'])
        
        '''
        # Dropping every column that has even one missing value
        if column_name == None:
            self.data.dropna(inplace = True,axis = 1)
            return self.data
        # if columns name as list is passed then it drops all those columns
        self.data.drop(columns = column_name,inplace = True)
        return self.data
    
    def missing_value_imputation_mean(self):
        '''
            Impute missing values using the mean of each numerical column.

            This method replaces missing values in columns of type `int64` or `float64` with their respective column means.
            It ensures that numerical features with missing data are filled with a representative value instead of being removed.

            Returns
            -------
            pd.DataFrame
                The modified DataFrame with missing values in numerical columns replaced by their respective means.

            Notes
            -----
            - This method is only applied to columns with numeric data types (`int64` or `float64`).
            - If a column has all values as NaN, its mean will be NaN, and no imputation will occur.

            Examples
            --------
            >>> import pandas as pd
            >>> data = pd.DataFrame({
            ...     'A': [1, 2, None, 4],
            ...     'B': [10.5, None, 30.2, 40.1],
            ...     'C': ['x', 'y', 'z', None]  # Non-numeric column
            ... })
            >>> treatment = Treating_Missing_Values(data, target_variable='A')

            # Perform mean imputation on numeric columns
            >>> cleaned_data = treatment.missing_value_imputation_mean()
                
                
        '''
        # Imputing missing values with mean for columns with data type int64 or float64
        for ele in self.data:
            if self.data[ele].dtype == 'int64' or self.data[ele].dtype == 'float64':
                self.data[ele] = self.data[ele].fillna(self.data[ele].mean())
                
        return self.data
    
    def missing_value_imputation_median(self):
        '''
            Impute missing values using the median of each numerical column.

            This method replaces missing values in columns of type `int64` or `float64` with their respective column medians.
            The median is often preferred over the mean when dealing with skewed data or outliers, as it is less sensitive to extreme values.

            Returns
            -------
            pd.DataFrame
                The modified DataFrame with missing values in numerical columns replaced by their respective medians.

            Notes
            -----
            - This method applies only to columns with numeric data types (`int64` or `float64`).
            - If a column has all values as NaN, its median will be NaN, and no imputation will occur.
            - Median imputation is useful for handling missing values in skewed distributions.

            Examples
            --------
            >>> import pandas as pd
            >>> data = pd.DataFrame({
            ...     'A': [1, 2, None, 4],
            ...     'B': [10.5, None, 30.2, 40.1],
            ...     'C': ['x', 'y', 'z', None]  # Non-numeric column
            ... })
            >>> treatment = Treating_Missing_Values(data, target_variable='A')

            # Perform median imputation on numeric columns
            >>> cleaned_data = treatment.missing_value_imputation_median()
        '''

        # Imputing missing values with median for columns with data type int64 or float64
        for ele in self.data:
            if self.data[ele].dtype == 'int64' or self.data[ele].dtype == 'float64':
                self.data[ele] = self.data[ele].fillna(self.data[ele].median())
                
        return self.data

    def missing_value_imputation_mode(self):
        ''' 
            Impute missing values using the mode of each column.

            This method replaces missing values in each column with the most frequently occurring value (mode).
            Mode imputation is useful for categorical data and can also be applied to numerical data.

            Returns
            -------
            pd.DataFrame
                The modified DataFrame with missing values replaced by the mode of each column.

            Notes
            -----
            - If a column has multiple mode values, only the first mode is used for imputation.
            - This method can be applied to both numerical and categorical columns.
            - If a column contains only NaN values, mode imputation will not be possible and will raise an IndexError.

            Examples
            --------
            >>> import pandas as pd
            >>> data = pd.DataFrame({
            ...     'A': [1, 2, 2, None, 4],
            ...     'B': ['x', 'y', 'y', 'y', None],
            ...     'C': [None, None, 'z', 'z', 'z']
            ... })
            >>> treatment = Treating_Missing_Values(data, target_variable='A')

            # Perform mode imputation on all columns
            >>> cleaned_data = treatment.missing_value_imputation_mode()
        
        '''
        # Code aims to replace every missing value with mode values
        for ele in self.data.columns:
            # Ensure mode exists before indexing
            if not self.data[ele].mode().empty:  
                self.data[ele] = self.data[ele].fillna(self.data[ele].mode()[0])

        return self.data

    def missing_value_linear_interpolation(self):
        '''
            Impute missing values using linear interpolation for numerical columns.

            This method applies **linear interpolation** to estimate and fill missing values in numerical 
            columns (`int64` or `float64`). Linear interpolation assumes a **straight-line** relationship 
            between existing data points to compute missing values.

            The method uses **pandas.DataFrame.interpolate()** with `method='linear'`, which fills NaN values 
            by computing values along a straight line between the nearest known data points.

            Returns
            -------
            pd.DataFrame
                The modified DataFrame with missing values in numerical columns replaced using 
                **linear interpolation**.

            Parameters
            ----------
            None

            Notes
            -----
            - **Linear interpolation** estimates missing values by assuming a linear trend between known points.
            - **Only numerical columns (`int64`, `float64`) are interpolated**; categorical or object columns 
            remain unchanged.
            - If missing values exist at the **start or end** of a column, they will **not be filled** unless 
            additional arguments such as `limit_direction='both'` are provided.
            - Interpolation is performed **column-wise**, meaning values are computed based on each column 
            independently.
            - To handle time-series data, consider setting `method='time'` for time-aware interpolation.

            Examples
            --------
            >>> import pandas as pd
            >>> import numpy as np
            >>> data = pd.DataFrame({
            ...     'A': [1, 2, np.nan, 4, 5],
            ...     'B': [10, np.nan, np.nan, 40, 50],
            ...     'C': ['x', 'y', 'z', None, 'w']
            ... })
            >>> treatment = Treating_Missing_Values(data, target_variable='A')

            # Perform linear interpolation on numerical columns
            >>> cleaned_data = treatment.missing_value_linear_interpolation()
            >>> print(cleaned_data)

            Alternative Usage
            -----------------
            To fill missing values at the **beginning or end of a column**, use:

            >>> data.interpolate(method='linear', limit_direction='both')

            To perform interpolation along rows instead of columns:

            >>> data.interpolate(method='linear', axis=1)

            References
            ----------
            - Pandas Documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html

        '''
        for ele in self.data.columns:
            if self.data[ele].dtype == 'int64' or self.data[ele].dtype == 'float64':
                self.data[ele] = self.data[ele].interpolate(method="linear")
        return self.data
    
    def missing_value_polynomial_interploation(self,order_val):
        '''
            Impute missing values using **polynomial interpolation** of a given order for numerical columns.

            This method applies **polynomial interpolation** to estimate and fill missing values in 
            numerical columns (`int64` or `float64`). It uses `pandas.DataFrame.interpolate(method='polynomial', order=order_val)`, 
            which fits an `n`-degree polynomial to predict missing values.

            Parameters
            ----------
            order_val : int
                The degree of the polynomial used for interpolation.
                - `order_val=1`: Equivalent to **linear interpolation**.
                - `order_val=2`: **Quadratic interpolation** (parabolic curve).
                - `order_val=3`: **Cubic interpolation** (third-degree polynomial).
                - Higher values allow more complex interpolation but may cause overfitting.

            Returns
            -------
            pd.DataFrame
                The modified DataFrame with missing values in numerical columns replaced using 
                **polynomial interpolation** of the specified order.

            Notes
            -----
            - **Only numerical columns (`int64`, `float64`) are interpolated**; categorical or object columns remain unchanged.
            - **Requires at least (order_val + 1) known data points** in a column to perform interpolation.
            - Polynomial interpolation is useful for capturing trends but **higher orders may cause overfitting**.
            - If missing values exist at the **start or end** of a column, they **may not be filled correctly** unless 
            `limit_direction='both'` is used.
            - Consider using **spline interpolation** (`method='spline'`) for a smoother alternative.

            Examples
            --------
            >>> import pandas as pd
            >>> import numpy as np
            >>> data = pd.DataFrame({
            ...     'A': [1, np.nan, 3, np.nan, 5],
            ...     'B': [10, np.nan, np.nan, 40, 50],
            ...     'C': [100, 200, 300, np.nan, 500]
            ... })
            >>> treatment = Treating_Missing_Values(data, target_variable='A')

            # Perform quadratic (order 2) interpolation
            >>> cleaned_data = treatment.missing_value_polynomial_interpolation(order_val=2)
            >>> print(cleaned_data)

            Alternative Usage
            -----------------
            To perform cubic (third-order) polynomial interpolation:

            >>> data.interpolate(method='polynomial', order=3)

            To handle edge missing values more effectively:

            >>> data.interpolate(method='polynomial', order=2, limit_direction='both')

            References
            ----------
            - Pandas Documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html
        '''
        for ele in self.data.columns:
            if self.data[ele].dtype == 'int64' or self.data[ele].dtype == 'float64':
                self.data[ele] = self.data[ele].interpolate(method="polynomial",order = order_val)
        return self.data

    def missing_value_cubic_interpolation(self):
        '''
            Impute missing values using **cubic interpolation** for numerical columns.

            This method applies **cubic spline interpolation** to estimate and fill missing values in 
            numerical columns (`int64` or `float64`). It uses `pandas.DataFrame.interpolate(method='cubic')`, 
            which fits a smooth **third-degree polynomial (cubic function)** to predict missing values.

            Returns
            -------
            pd.DataFrame
                The modified DataFrame with missing values in numerical columns replaced using 
                **cubic interpolation**.

            Parameters
            ----------
            None

            Notes
            -----
            - **Cubic interpolation** fits a **third-degree polynomial** (cubic function) to estimate missing values.
            - **Only numerical columns (`int64`, `float64`) are interpolated**; categorical or object columns remain unchanged.
            - **Requires at least four known data points** in a column to perform a meaningful cubic interpolation.
            - Cubic interpolation is **smoother than linear or quadratic interpolation** and captures more complex trends.
            - If missing values exist at the **start or end** of a column, they **may not be filled correctly** 
            unless `limit_direction='both'` is used.
            - **Overfitting risk:** If the data has too much fluctuation, cubic interpolation may not generalize well.

            Examples
            --------
            >>> import pandas as pd
            >>> import numpy as np
            >>> data = pd.DataFrame({
            ...     'A': [1, np.nan, 3, np.nan, 5],
            ...     'B': [10, np.nan, np.nan, 40, 50],
            ...     'C': [100, 200, 300, np.nan, 500]
            ... })
            >>> treatment = Treating_Missing_Values(data, target_variable='A')

            # Perform cubic interpolation on numerical columns
            >>> cleaned_data = treatment.missing_value_cubic_interpolation()
            >>> print(cleaned_data)

            Alternative Usage
            -----------------
            To fill missing values at the **start or end of a column**, use:

            >>> data.interpolate(method='cubic', limit_direction='both')

            To perform cubic interpolation along rows instead of columns:

            >>> data.interpolate(method='cubic', axis=1)

            References
            ----------
            - Pandas Documentation: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.interpolate.html
        '''
        
        for ele in self.data.columns:
            if self.data[ele].dtype == 'int64' or self.data[ele].dtype == 'float64':
                self.data[ele] = self.data[ele].interpolate(method="cubic")
        return self.data
    
    def missing_value_forward_fill(self):
        '''
               def missing_value_forward_fill(
                        *,
                        axis: Axis | None = ...,
                        inplace: Literal[False] = ...,
                        limit: int | None = ...,
                        limit_area: Literal['inside', 'outside'] | None = ...,
                        downcast: dict | None = ...
                        ) -> DataFrame: ...
                        ,*

        '''
        return self.data.ffill()
    
    def missing_value_backward_fill(self):
        return self.data.bfill()






import pandas as pd

data = pd.read_csv('Raw_Housing_Prices.csv')
missing_values = Treating_Missing_Values(data,'Sale Price')

print(data.isnull().sum())
print()
data_null,missing_percentage = missing_values.display_missing_value()
print('After')
data.ffill()
print(data_null)
print(missing_percentage)


