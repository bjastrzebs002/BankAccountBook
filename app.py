from bank_account import BankAccount

all_accounts = []
last_used_accounts = []

options_names = ["Add new bank account", "Get all bank accounts", "Get last used accounts", "Find account",
                 "Remove account"]


def show_detailed_info(account):
    print(f'Recipient: {account.recipient}. \nRecipient Address: {account.recipient_address}. \n'
          f'Recipient account address: {account.account_address}. \nRecipient short name: {account.short_name}')


def show_short_names(accounts):
    for i, account in enumerate(accounts):
        print(f'{i + 1}. {account.short_name}')


def get_new_account_index(bank_account: BankAccount):
    # just add to list when is empty
    if len(all_accounts) == 0:
        return 0
    # start binary search
    left, right = 0, len(all_accounts) - 1

    while left <= right:
        middle = (left + right) // 2

        if all_accounts[middle].short_name == bank_account.short_name:
            return middle

        if all_accounts[middle].short_name < bank_account.short_name:
            left = middle + 1
        elif all_accounts[middle].short_name > bank_account.short_name:
            right = middle - 1
    # binary search would not find an index for given element, but we need to add element to the list at `left` index
    # (it should be alphabetically)
    return left


def add_account(bank_account: BankAccount):
    # initial add BankAccount object to the list
    index = get_new_account_index(bank_account)
    all_accounts.insert(index, bank_account)

    # add new bank account to `last used` stack
    # pop all elements from stack
    stack_accounts, last_used_accounts[:] = last_used_accounts[:], []
    last_used_accounts.append(bank_account)
    for acc in stack_accounts:
        last_used_accounts.append(acc)


def update_last_used_account(account):
    # pop all items
    stack_accounts, last_used_accounts[:] = last_used_accounts[:], []
    # remove given item from stack items
    stack_accounts.remove(account)
    # push item as a first
    last_used_accounts.append(account)
    # push other items
    for acc in stack_accounts:
        last_used_accounts.append(acc)


def get_chosen_account(choice, accounts):
    if choice.isnumeric() and 0 < int(choice) <= len(accounts):
        chosen_account = accounts[int(choice) - 1]
        show_detailed_info(chosen_account)
        # update last used account
        update_last_used_account(chosen_account)
    else:
        print("Wrong number.")


def find_accounts_by_phrase(phrase):
    return [account for account in all_accounts if phrase in account.short_name.lower()]


def remove_account(choice):
    if choice.isnumeric() and 0 < int(choice) <= len(all_accounts):
        chosen_account = all_accounts[int(choice) - 1]
        all_accounts.remove(all_accounts[int(choice) - 1])
        # remove account from last used accounts
        last_used_accounts.remove(chosen_account)
    else:
        print("Wrong number.")


def provide_new_account_info():
    # User provide information about bank account
    recipient, address, acc_address, short_name = input("Provide recipient name: "), input(
        "Provide recipient address: "), input("Provide recipient account address: "), input(
        "Provide recipient short name: ")
    return BankAccount(recipient, address, acc_address, short_name)


def base_options():
    for i in range(len(options_names)):
        print(str(i + 1) + ". " + options_names[i])
    print("Type anything else to quit.\n")
    choice = input("Your option: ")
    if choice == "1":
        new_account = provide_new_account_info()
        add_account(new_account)
    elif choice == "2":
        show_short_names(all_accounts)
        choice = input("Choose number to get info about")
        get_chosen_account(choice, all_accounts)
    elif choice == "3":
        show_short_names(last_used_accounts)
        choice = input("Choose number to get info about")
        get_chosen_account(choice, last_used_accounts)
    elif choice == "4":
        short_name_substring = input("Provide account's short name phrase: ").lower()
        filter_accounts = find_accounts_by_phrase(short_name_substring)
        show_short_names(filter_accounts)
        choice = input("Choose number to get info about")
        get_chosen_account(choice, filter_accounts)
    elif choice == "5":
        show_short_names(all_accounts)
        choice = input("Choose number to remove: ")
        remove_account(choice)
    else:
        return -1


if __name__ == "__main__":
    while True:
        if base_options() == -1:
            break
