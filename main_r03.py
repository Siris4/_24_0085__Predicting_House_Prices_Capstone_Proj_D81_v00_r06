import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv(r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0085__Day81_Predicting_House_Prices_Capstone_Proj__240902\NewProject\r00_env_START\boston.csv', index_col=0)

# Visualize the distribution of the average number of rooms per dwelling with KDE
sns.displot(data['RM'], kde=True, height=6, aspect=1.5, bins=30)

# Add labels and title for clarity
plt.xlabel('Average Number of Rooms per Dwelling (RM)')
plt.ylabel('Frequency')
plt.title('Distribution of Average Number of Rooms per Dwelling with KDE')

# Save the plot to the specified path
plt.savefig(r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0085__Day81_Predicting_House_Prices_Capstone_Proj__240902\NewProject\r00_env_START\rooms_distribution.png')
