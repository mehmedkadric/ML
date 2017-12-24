import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model

xls = pd.ExcelFile("RealEstate.xls")
sheetX=xls.parse(1)
var1 = sheetX['Size']
var2 = sheetX['Price']
size = var1[:150]
price = var2[:150]
regr = linear_model.LinearRegression()
regr.fit(size,price)
assert isinstance(regr.coef_)
print(regr.coef_)
plt.plot(size,price,'ro')
plt.xlabel('Size')
plt.ylabel('Price')
plt.grid(True)
plt.show()

