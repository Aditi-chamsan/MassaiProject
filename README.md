# MassaiProject
**Project Name**  : Banking system.
### **Class: BankingSystem**
This class manages the core functionalities of the banking system.
1. **`__init__` Method**:
   - Initializes an empty dictionary `self.users` to store user data.
   - User data includes their password and account balance.

2. **`create_account` Method**:
   - Takes `username` and `password` as inputs.
   - Checks if the username already exists in `self.users`. If it does, it prints an error message.
   - If the username is new, it creates an entry in `self.users` with the password and initializes the balance to 0.

3. **`login` Method**:
   - Takes `username` and `password` as inputs.
   - Validates the username and password against the stored data.
   - Prints success or failure messages based on the validation.

4. **`deposit` Method**:
   - Allows a user to deposit a specified amount into their account.
   - Validates that the deposit amount is positive.
   - Updates the user's balance and displays the new balance.

5. **`withdraw` Method**:
   - Allows a user to withdraw a specified amount from their account.
   - Validates that the amount is positive and that the user has sufficient funds.
   - Updates the user's balance and displays the new balance.

6. **`check_balance` Method**:
   - Displays the current balance of the user's account.

7. **`view_transactions` Method**:
   - Placeholder method; prints a message indicating transaction history is not supported in this version.
### **Function: `main`**
This function provides a user interface for interacting with the banking system.

1. **Main Menu**:
   - Displays three options: 
     1. Create an Account
     2. Login
     3. Exit
   - Prompts the user to choose an option and calls the appropriate method from the `BankingSystem` class.

2. **Account Menu**:
   - Once a user logs in, they access the account menu, which includes options to:
     1. Deposit
     2. Withdraw
     3. Check Balance
     4. Logout

3. **Loop**:
   - Both menus run in a loop, allowing the user to perform multiple actions until they choose to logout or exit.
   - 
### **WORKING **
1. **Account Creation**:
   - Users can create accounts by entering a username and password. Each username must be unique.

2. **Login**:
   - Users can log in using their username and password. Successful login grants access to the account menu.

3. **Account Actions**:
   - Users can deposit or withdraw money and check their balance.

4. **Exit**:
   - Users can exit the application from the main menu.
This code provides a simple console-based banking system. Here's a summary:

- **Purpose**: The program allows users to create accounts, log in, deposit and withdraw money, check their balance, and manage basic banking activities.
- **Key Features**:
  - Users can create accounts with a username and password.
  - Login functionality ensures only authorized users can access their accounts.
  - Deposit and withdrawal options allow users to manage their account balances.
  - Users can check their current balance at any time.

   
