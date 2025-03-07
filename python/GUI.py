from tkinter import*
root = Tk()
entry = Entry()
label =Label(text='What transaction do you want to perform?',font=('vardana',18,'bold',),fg='black')
label.grid(row=1,column=1,columnspan=5)


# create a class
class BanksystemGui():
    def __init__(self):
        self.balance = 0
        self.user_input = Entry(font=('cambria',16,'bold'))
        
        
        self.prompt_label = Label(
            root,
            text="",  # Empty initially, will be updated dynamically
            font=("Cambria", 14),
            fg="blue",
        )
        self.prompt_label.grid(row=2, column=1, columnspan=6)
        
    def deposit(self):
        withdraw_btn.grid_forget()
        self.prompt_label.configure(text="How much do you want to deposit?")
        self.user_input.grid(row=3, column=1,columnspan=6)
        d_input = eval(Entry.get(self.user_input))
        self.balance += d_input
        label.configure(text='Deposite succussful!! Your account balance is now {}'.format(self.balance))
        
    def withdraw(self):
        deposit_btn.grid_forget()
        self.prompt_label.configure(text="How much do you want to withdraw?")
        self.user_input.grid(row=3, column=1,columnspan=6)
        d_input =eval(Entry.get(self.user_input))
        if d_input > self.balance:
            label.configure(text='You do not have sufficient balance')
        else:
            self.balance-= d_input
            label.configure(text='withdraw succussful!! Your account balance is now {}'.format(self.balance))

        
        
bank =BanksystemGui()
deposit_btn = Button(text='deposit',font=('verdana',18,'bold'),bg='green',command =bank.deposit,fg='black')
withdraw_btn = Button(text='withdraw',font=('verdana',18,'bold'),bg='blue',command =bank.withdraw,fg='black')

deposit_btn.grid(row =4, column=2)
withdraw_btn.grid(row =4, column=4)
mainloop()
