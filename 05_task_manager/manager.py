from decorators import log_task_completion


class TaskManager:
    """Manages a queue of tasks using a list."""

    def __init__(self):
        self.tasks = []

    def add_task(self, task_name: str) -> None:
        """
        Adds a task to the end of the list (Queue).
        :param task_name: The name of the task to add.
        :return: None
        """
        self.tasks.append(task_name)
        print(f"Added task: {task_name}")

    @log_task_completion
    def process_task(self) -> None:
        """
        Removes and returns the first task in the list.
        :return: None
        """
        if not self.tasks:
            print("The queue is empty.")
            return None
        # Using pop(0) to implement Queue behavior (FIFO)
        return self.tasks.pop(0)

    def show_pending(self) -> None:
        """
        Uses List Comprehension to show pending tasks.
        :return: None
        """
        pending = [f"- {t}" for t in self.tasks]
        print("\nPending Tasks:\n" + ("\n".join(pending) if pending else "Empty"))