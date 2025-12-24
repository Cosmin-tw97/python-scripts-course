from clicker import ClickerBot
import time


def main():
    print("--- Multithreaded Auto-Clicker ---")
    print("Press Ctrl+C to stop the program safely.")

    # Initialize the bot with a 2-second interval
    bot = ClickerBot(delay=2.0)

    try:
        bot.start()
        while bot.is_alive():
            # We wait with a short timeout to allow
            # the main thread to listen for signals (Ctrl+C)
            bot.join(timeout=0.1)
    except KeyboardInterrupt:
        print("\n[STOP] KeyboardInterrupt detected!")
        bot.stop_clicking()
        bot.join()

if __name__ == "__main__":
    main()