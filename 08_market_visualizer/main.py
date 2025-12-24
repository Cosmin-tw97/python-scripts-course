from data_engine import generate_market_data
from plotter import create_market_plot


def main():
    print("--- Market Data Visualizer ---")

    # 1. Generate 100 days of synthetic data
    days, prices = generate_market_data(days=100)

    # 2. Create and save the visual report
    create_market_plot(days, prices)


if __name__ == "__main__":
    main()