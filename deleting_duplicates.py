class Duplicate_Removal:

    def __init__(self,data):
        self.data = data

    def duplicate_removal(self):
        """
            Removes duplicate rows from the dataset.

            This method drops all duplicate entries from the `self.data` DataFrame,
            retaining the first occurrence of each duplicate. It modifies the DataFrame
            in place and returns the cleaned DataFrame.

            Returns:
                pd.DataFrame: The DataFrame after removing duplicate rows.
        """
        self.data = self.data.drop_duplicates()
        return self.data



    


import pandas as pd

data = pd.read_csv('Raw_Housing_Prices.csv')
print(data.shape[0])
duplicate = Duplicate_Removal(data)

data = duplicate.duplicate_removal()
print(data.shape[0])



