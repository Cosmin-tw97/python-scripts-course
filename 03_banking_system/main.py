class InsufficientFundsError(Exception):
    """Custom exception for insufficient balance."""
    pass


class BankAccount:
    """Base class representing a generic bank account."""

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.__balance = balance  # Private attribute (Encapsulation)

    def deposit(self, amount: float) -> None:
        """
        Deposit an amount into the account.
        :param amount: The amount to deposit.
        :return: None
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount: float) -> None:
        """
        Withdraw an amount from the account.
        :param amount: The amount to withdraw.
        :return: None
        """
        if amount > self.__balance:
            raise InsufficientFundsError(f"Wait {self.owner}, you only have {self.__balance}!")
        self.__balance -= amount
        print(f"Withdrawn {amount}. Remaining balance: {self.__balance}")

    @property
    def balance(self) -> float:
        """
        Getter for the private balance.
        :return: The private balance in float type.
        """
        return self.__balance

    def __str__(self) -> str:
        return f"Account Owner: {self.owner} | Balance: {self.__balance}"


class SavingsAccount(BankAccount):
    """Subclass representing a savings account with interest."""

    def __init__(self, owner: str, balance: float = 0.0, interest_rate: float = 0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self) -> None:
        """
        Applies the interest rate to the savings account.
        :return: None
        """
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest applied: {interest}")


def main():
    try:
        # Creating a Savings Account
        my_savings = SavingsAccount("Cosmin", 1000.0)
        print(my_savings)

        my_savings.deposit(500)
        my_savings.apply_interest()
        my_savings.withdraw(2000)  # This will trigger our custom error

    except InsufficientFundsError as e:
        print(f"Banking Error: {e}")
    except Exception as e:
        print(f"General Error: {e}")


if __name__ == "__main__":
    main()