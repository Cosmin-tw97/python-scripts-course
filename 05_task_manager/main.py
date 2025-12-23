from manager import TaskManager


def main():
    tracker = TaskManager()

    print("--- Priority Task Manager ---")

    # Adding tasks
    tracker.add_task("Send email to client")
    tracker.add_task("Update GitHub repository")
    tracker.add_task("Review Python documentation")

    tracker.show_pending()

    # Processing tasks (demonstrating the decorator)
    print("\nProcessing next task...")
    tracker.process_task()

    tracker.show_pending()


if __name__ == "__main__":
    main()