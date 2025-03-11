class Duplicate_Removal:

    def __init__(self,data):
        self.data = data

    def duplicate_removal(self):
        '''
        
        '''
        self.data = self.data.drop_duplicates()
        return self.data



    


import pandas as pd

data = pd.read_csv('Raw_Housing_Prices.csv')
print(data.shape[0])
duplicate = Duplicate_Removal(data)

data = duplicate.duplicate_removal()
print(data.shape[0])



