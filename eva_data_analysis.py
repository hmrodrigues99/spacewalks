import matplotlib.pyplot as plt
import pandas as pd

# Data source: https://data.nasa.gov/resource/eva.json (with modifications)

input_file = open('./eva-data.json', 'r')
output_file = open('./eva-data.csv', 'w')
graph_file = './cumulative_eva_graph.png'

eva_df = pd.read_json(input_file, convert_dates=['date'])  # Make sure date column contains values formatted as dates
eva_df['eva'] = eva_df['eva'].astype(float)
eva_df.dropna(axis=0, inplace=True)  # Drop rows with missing values
eva_df.sort_values('date', inplace=True)

eva_df.to_csv(output_file, index=False)

eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)  # Convert duration from HH:MM to hours
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()  # Add cumulative hours for each year
plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')  #Explaining ko- here would be nice, I don't know what it means
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()