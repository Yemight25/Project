
from tkinter import *

root = Tk()
root.title("Banking System")
root.geometry("500x300")

label = Label(
    text="What transaction do you want to perform?",
    font=("Verdana", 18, "bold"),
    fg="black",
)
label.grid(row=1, column=1, columnspan=5, pady=10)


# Create a class for the Bank System
class BankSystemGui:
    def __init__(self):
        self.balance = 0
        self.user_input = Entry(font=("Cambria", 16, "bold"))
        self.prompt_label = Label(
            root,
            text="",  # Empty initially, will be updated dynamically
            font=("Cambria", 14),
            fg="blue",
        )
        self.prompt_label.grid(row=2, column=1, columnspan=6, pady=5)

        # Buttons for Yes/No options
        self.yes_btn = Button(
            text="Yes", font=("Verdana", 14), bg="green", fg="white", command=self.restart
        )
        self.no_btn = Button(
            text="No", font=("Verdana", 14), bg="red", fg="white", command=self.exit_app
        )

        # Placeholder for Confirm Button
        self.confirm_btn = None

    def deposit(self):
        withdraw_btn.grid_forget()
        deposit_btn.grid_forget()
        self.prompt_label.configure(text="How much do you want to deposit?")
        self.user_input.grid(row=3, column=1, columnspan=6, pady=5)

        self.confirm_btn = Button(
            text="Confirm",
            font=("Verdana", 14),
            bg="orange",
            fg="white",
            command=self.confirm_deposit,
        )
        self.confirm_btn.grid(row=4, column=3, pady=5)

    def confirm_deposit(self):
        try:
            d_input = float(self.user_input.get())
            self.balance += d_input
            label.configure(
                text=f"Deposit successful! Your account balance is now {self.balance}"
            )
            self.user_input.delete(0, END)
            self.user_input.grid_forget()
            self.confirm_btn.grid_forget()  # Hide Confirm button
            self.ask_continue()
        except ValueError:
            label.configure(text="Invalid input. Please enter a valid amount.")

    def withdraw(self):
        withdraw_btn.grid_forget()
        deposit_btn.grid_forget()
        self.prompt_label.configure(text="How much do you want to withdraw?")
        self.user_input.grid(row=3, column=1, columnspan=6, pady=5)

        self.confirm_btn = Button(
            text="Confirm",
            font=("Verdana", 14),
            bg="orange",
            fg="white",
            command=self.confirm_withdraw,
        )
        self.confirm_btn.grid(row=4, column=3, pady=5)

    def confirm_withdraw(self):
        try:
            d_input = float(self.user_input.get())
            if d_input > self.balance:
                label.configure(text="You do not have sufficient balance.")
            else:
                self.balance -= d_input
                label.configure(
                    text=f"Withdraw successful! Your account balance is now {self.balance}"
                )
            self.user_input.delete(0, END)
            self.user_input.grid_forget()
            self.confirm_btn.grid_forget()  # Hide Confirm button
            self.ask_continue()
        except ValueError:
            label.configure(text="Invalid input. Please enter a valid amount.")

    def ask_continue(self):
        # Ask the user if they want to continue
        self.prompt_label.configure(text="Do you want to continue your transaction?")
        self.yes_btn.grid(row=5, column=2, pady=10)
        self.no_btn.grid(row=5, column=4, pady=10)

    def restart(self):
        # Reset the UI to initial state
        self.prompt_label.configure(text="")
        self.yes_btn.grid_forget()
        self.no_btn.grid_forget()
        deposit_btn.grid(row=4, column=2)
        withdraw_btn.grid(row=4, column=4)

    def exit_app(self):
        # Exit the application
        label.configure(text="Have a wonderful day!")
        self.prompt_label.configure(text="")
        self.yes_btn.grid_forget()
        self.no_btn.grid_forget()


# Create an instance of the BankSystemGui
bank = BankSystemGui()

# Buttons for deposit and withdraw
deposit_btn = Button(
    text="Deposit",
    font=("Verdana", 18, "bold"),
    bg="green",
    command=bank.deposit,
    fg="black",
)
withdraw_btn = Button(
    text="Withdraw",
    font=("Verdana", 18, "bold"),
    bg="blue",
    command=bank.withdraw,
    fg="black",
)

deposit_btn.grid(row=4, column=2, pady=10)
withdraw_btn.grid(row=4, column=4, pady=10)

mainloop()