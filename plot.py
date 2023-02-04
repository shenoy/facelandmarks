import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('normalized_csv/markzuckerberg.csv')
plt.scatter(df['x_value'], df['y_value'])
plt.title('Face Landmarks')
plt.xlabel('X coordinates')
plt.ylabel('Y coordinates')
plt.show()