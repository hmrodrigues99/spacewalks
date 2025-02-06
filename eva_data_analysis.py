
import matplotlib.pyplot as plt
import pandas as pd

def read_json_to_dataframe(input_file):
    """
    Read the data from a JSON file into a Pandas dataframe
    Clean the data by removing rows with missing values, and sort dataframe by date

    Args:
        input_file (str): The path to the JSON file
    
    Returns:
        eva_df (pd.DataFrame): The cleaned and sorted Pandas dataframe
    """
    print(f'Reading JSON file {input_file}')
    # Read the data from a JSON file into a Pandas dataframe
    eva_df = pd.read_json(input_file, convert_dates=['date'])
    eva_df['eva'] = eva_df['eva'].astype(float)
    # Clean the data by removing any incomplete rows and sort by date
    eva_df.dropna(axis=0, inplace=True)
    eva_df.sort_values('date', inplace=True)
    return eva_df


def write_dataframe_to_csv(df, output_file):
    """
    Write the Pandas dataframe previously obtained to a CSV file

    Args:
        df (pd.DataFrame): The input dataframe
        output_file (str): The path to the output CSV file

    Returns:
        None
    """
    print(f'Saving to CSV file {output_file}')
    df.to_csv(output_file, index=False)


def plot_cumulative_time_in_space(eva_data, graph_file):
    """
    Process the pandas dataframe and create a plot cumulative time spent
    in space over years and save the graph to a file

    Args:
        eva_data (pd.DataFrame): The input dataframe
        graph_file (str): The path to the output graph file

    Returns:
        None
    """
    print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')
    # Process the duration column from a string (00:00) to get the total time in hours in float
    eva_data['duration_hours'] = eva_data['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
    #Plot cumulative time spent in space over years
    eva_data['cumulative_time'] = eva_data['duration_hours'].cumsum()
    plt.plot(eva_data['date'], eva_data['cumulative_time'], 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(graph_file)
    plt.show()


# Main code

print("--START--")

input_file = open('./eva-data.json', 'r')
output_file = open('./eva-data.csv', 'w')
graph_file = './cumulative_eva_graph.png'

# Read the data from JSON file
eva_data = read_json_to_dataframe(input_file)

# Convert and export data to CSV file
write_dataframe_to_csv(eva_data, output_file)

# Plot cumulative time spent in space over years
plot_cumulative_time_in_space(eva_data, graph_file)

print("--END--")
