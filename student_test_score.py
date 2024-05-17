import matplotlib.pyplot as plt
import os
import numpy as np

def visualize_distribution(mean, std_dev, num_samples, bins=30, output_file='distribution_plot.png'):
    # Generate a dataset of random scores following a normal distribution
    scores = np.random.normal(mean, std_dev, num_samples)

    # Create the histogram
    plt.figure(figsize=(10, 6))
    plt.hist(scores, bins=bins, edgecolor='black', alpha=0.7)
    plt.title('Distribution Plot')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True)

    # Define the directory and file name to save the plot
    output_dir = 'plots'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the plot to the specified file
    file_path = os.path.join(output_dir, output_file)
    plt.savefig(file_path)
    plt.show()

    print(f"The plot has been saved to {file_path}")

def main():
    # Parameters for the distribution
    mean = 75
    std_dev = 10
    num_samples = 1000
    bins = 30
    output_file = 'test_scores_distribution.png'

    # Visualize the distribution
    visualize_distribution(mean, std_dev, num_samples, bins, output_file)

if __name__ == "__main__":
    main()
