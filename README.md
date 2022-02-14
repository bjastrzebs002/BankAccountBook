# Bank Accounts book application

## Usage overview
### Application overview
Python application is prepared to usage by terminal. 
The book account book is the base application to use structured and well-defined information about bank accounts as a helper. The application could be used by users in a simple way to save, edit and re-use others’ bank accounts. The application is based on single application architecture with an in-memory database and processing on this kind of software.

### Adding new bank account
The insertion process is separated into two subprocesses after the created instance of BankAccount class:
1. Saving object to Book (list of all bank accounts sorted alphabetically). This process has to be proceed using some kind of search algorithm. 
The best option is a binary search on strings (short_name property in BankAccount class instance).  For searching the best index for our new bank account, binary search is one of the solutions for this problem. After finding the best place for a new object, the program can put it on the list or create a new list based on the old one.
2. Pushing new object to the stack of “recent” BankAccount objects.

### Filtering/searching bank accounts
Searching/Filtering bank accounts is based on substrings. User is able to input phrase which should be the part of short_name property of bank accounts. As a results, user get all of saved accounts where phrase is part of short name of account (case insensitive).
After filtering user can choose any of filtered accounts and get detailed information about given item.

### All Accounts and Last Used Accounts
Application stores bank accounts in two lists:
1. All Accounts list - the list of all bank accounts saved in memory by an user. Accounts are stored alphabetically, which lets user to easy read list of all accounts. 
  The process of adding alphabetically new account is based on binary search, which is one of the quickest methods to sort and find proper index for new account. The short representation of each account is its short name property.
2. Last Used Accounts stack - This list is the stack structure. The item which is on the top of the stack is the last used item (added or read). Stack stores all of accounts as the list above.
  Processes as reading detailed information about given account puts this account on the top of the Last Used Accounts stack. The stack saved in memory perfectly fits the idea of recently used bank accounts by the user. At the start order of poped accounts are in order of their insertion. In the situation of using a single account (getting its information, copying etc.) stack pops an element to the used one and fill itself again in the same order without a selected item, and pushes this used item on the top of the stack.

### Removing account
User is able to remove given bank account from all lists (All Accounts and Last Used Accounts). This is the one of 5 options in main menu.

## Software requirements
### Python
The main and only requirement for running this application is installed Python framework (>=3.6).

### Running application
To run application all the files has to be in the same directory. 
Then run command below in terminal: 
```
python3 app.py
```

## Application overview
### Menu
All of actions done by the user has to be proceed from terminal by selecting numbers presented on the screen. 
Below is presentation of main menu of the application with all available options.
```
1. Add new bank account
2. Get all bank accounts
3. Get last used accounts
4. Find account
5. Remove account
Type anything else to quit.
```

### Adding new account
After choosing option 1, which is adding new bank account, application will ask for a few properties of this account (randomly provided data in example below). 
```
Your option: 1
Provide recipient name: new Account
Provide recipient address: New York, street
Provide recipient account address: 4200003948291829381111
Provide recipient short name: new account1
```

### Getting all bank accounts
Under the option 2 application lets user to review all saved bank accounts alphabetically by short name:
```
Your option: 2
1. brother
2. new account1
3. sister
Choose number to get info about
```
Application also ask user to chose one number to get detailed information about account. After choosing one, info will be presented on the screen:
```
Choose number to get info about1
Recipient: new Account2. 
Recipient Address: New York, street. 
Recipient account address: 123343451321352135135. 
Recipient short name: brother
```

### Getting last used accounts
Under option 3 user is able to review list of last used application. The list, as described in section above, is updating on each operation (adding new account or reading detailed info from existing one):
```
Your option: 3
1. brother
2. sister
3. new account1
Choose number to get info about
```
Application also lets user to get information about single account.

### Searching bank accounts
The searching option is under number 4. The searching process is prepared as substring filtering. User can provide the string phrase, then application will filter all items and take only these with matching short name:
```
Your option: 4
Provide account's short name phrase: ther
1. brother
Choose number to get info about
```

```
Your option: 4
Provide account's short name phrase: er
1. brother
2. sister
Choose number to get info about
```

### Removing accounts
In the easy way user is able to remove any saved bank account. This option is available under number 5 in main menu. Application just ask for an account which has to be removed:
```
Your option: 5
1. brother
2. new Account2
3. sister
Choose number to remove: 2
```
and then for all accounts:
```
Your option: 2
1. brother
2. sister
Choose number to get info about
```
