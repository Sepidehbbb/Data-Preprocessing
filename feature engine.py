from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np
from feature_engine.imputation import MeanMedianImputer
from feature_engine.encoding import OneHotEncoder
from feature_engine.transformation import LogTransformer
from feature_engine.creation import MathFeatures
from feature_engine.selection import DropConstantFeatures
from feature_engine.outliers import OutlierTrimmer

data = {
    "Severity" : [1,2,3,np.nan,5,6,7,np.nan,9,10],
    "Cost" : [10,20,30,40,50,np.nan,70,80,np.nan,100],
    "Color" : ["red", "Black","Blue" ,"Green" ,"red", "Black","red","Blue","Green", "Black"],
    "City" : ["Teh","Teh","Teh","Teh","Teh","Teh","Teh","Teh","Teh","Teh"]
}

df = pd.DataFrame(data)
# print(df)

# df["Severity"].fillna(method="bfill", inplace=True)
print(df)

# imputer = SimpleImputer(missing_values=np.nan,  strategy='median')
# df["Severity"] = imputer.fit_transform(df["Severity"].values.reshape(-1,1))

# df["Severity"].fillna(df["Severity"].mean(), inplace=True)

# imputer = MeanMedianImputer(variables=["Severity", "Cost" ] , imputation_method="mean")
# df = imputer.fit_transform(df)
#
# encoder = OneHotEncoder(variables=["Color"])
# df  = encoder.fit_transform(df)
#
# # MathFeatures()
#
# dropper = DropConstantFeatures()
# df = dropper.fit_transform(df)

#
# OutlierTrimmer()
# print(df)

# df.info()