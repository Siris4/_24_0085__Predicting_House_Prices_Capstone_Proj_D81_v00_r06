import pandas as pd
import plotly.express as px

# Load the dataset
data = pd.read_csv(r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0085__Day81_Predicting_House_Prices_Capstone_Proj__240902\NewProject\r00_env_START\boston.csv', index_col=0)

# Count the number of homes near the river and away from the river
chas_counts = data['CHAS'].value_counts().reset_index()

# Rename the columns to something more meaningful
chas_counts.columns = ['CHAS', 'count']

# Create the bar chart
fig = px.bar(chas_counts,
             x='CHAS',
             y='count',
             labels={'CHAS':'CHAS (0 = Away from River, 1 = Next to River)', 'count':'Number of Homes'},
             title='Number of Homes Near vs. Away from the River')

# Update the x-axis labels to be more descriptive
fig.update_xaxes(tickvals=[0, 1], ticktext=['Away from River', 'Next to River'])

# Show the plot
fig.show()

# Save the plot as an HTML file
fig.write_html(r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0085__Day81_Predicting_House_Prices_Capstone_Proj__240902\NewProject\homes_near_river.html')
