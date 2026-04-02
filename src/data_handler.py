from libraries_used import pd

class DataHandler:

    def __init__(self,filepath):
        self.filepath = filepath
        self.df = None
        

    #load data
    def load(self):
        self.df = pd.read_csv(self.filepath, keep_default_na=False)
        #keep_default_na=False is here so that "None" in the dataset isn't counted as a missing value

        #using this to visualize --Jayden 
        

    #clean data
    def clean(self):
        #remove duplicate datapoints
        self.df.drop_duplicates(inplace=True)

        #check for missing datapoints
        print("Number of missing datapoints: ", self.df.isnull().sum())
        


    #convert all categorical variables into discrete ordered/unordered values
    def transform(self, mapping = None):
        self.dfTransform = self.df.copy()
        #loop through columns to adjust for ordered values
        for col in self.dfTransform:
            if col in mapping:
                self.dfTransform[col] = self.dfTransform[col].map(mapping)
                
                #change column from object to float so that it is unaffected by get_dummies
                self.dfTransform[col] = pd.to_numeric(self.dfTransform[col], errors='coerce')
                
        
        #convert all remaining object columns into unordered values
        self.dfTransform = pd.get_dummies(self.dfTransform,drop_first=True)
        
        return self.dfTransform.copy()
       

    #condense n values into m<n bins
    def bin_variable(self,column,bins,labels):
        if column in self.df:
            self.df[column+"_Bin"] = pd.cut(self.df[column],bins=bins,labels=labels,include_lowest=True)
            

    #seperate target variable from the rest of the dataset
    def set_target(self,target):
        self.y = self.df[target]
        self.x = self.df.drop(columns=[target])


    #return cleaned data
    def get_data(self):
        return self.df.copy()


    #return x
    def get_variables(self):
        return self.x.copy()
    
    
    #return y
    def get_target(self):
        return self.y.copy()
