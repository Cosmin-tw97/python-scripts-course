import matplotlib.pyplot as plt


def create_market_plot(x, y, filename="market_trend.png") -> None:
    """
    Creates and saves a professional line chart.
    Demonstrates: Matplotlib styling and file output.
    :param x: x-axis data
    :param y: y-axis data
    :param filename: filename to save to
    :return: None
    """
    plt.figure(figsize=(10, 6))

    # Plotting the data
    plt.plot(x, y, color='blue', linewidth=2, label='Asset Price')

    # Customizing the chart
    plt.title("Synthetic Market Analysis (100 Days)", fontsize=14)
    plt.xlabel("Days", fontsize=12)
    plt.ylabel("Price (USD)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # Save the plot as an image
    plt.savefig(filename)
    print(f"Chart saved successfully as {filename}")

    # Show the plot (optional, will open a window)
    plt.show()