import app
from bank_account import BankAccount


def test_add_new_account():
    # given
    new_account = BankAccount("rec", "add1", "add2", "short")

    # when
    app.add_account(new_account)

    # then
    assert len(app.all_accounts) == 1, "No account added to all_accounts"
    assert len(app.last_used_accounts) == 1, "No account added to last_used_accounts"
    assert app.all_accounts[0] == app.last_used_accounts[0] == new_account, "Wrong account added"


def test_add_new_accounts_alphabetically():
    # given
    new_account1 = BankAccount("rec", "add1", "add2", "bbb")
    new_account2 = BankAccount("rec", "add1", "add2", "aaa")

    # when
    app.add_account(new_account1)
    app.add_account(new_account2)

    # then
    assert app.all_accounts[0] == new_account2, "Not alphabetically added account"
    assert app.all_accounts[1] == new_account1, "Not alphabetically added account"


def test_update_last_used_accounts():
    # given
    new_account1 = BankAccount("rec", "add1", "add2", "bbb")
    new_account2 = BankAccount("rec", "add1", "add2", "aaa")
    new_account3 = BankAccount("rec", "add1", "add2", "ccc")

    app.add_account(new_account1)
    app.add_account(new_account2)
    app.add_account(new_account3)

    # when
    app.update_last_used_account(new_account2)

    # then
    assert app.last_used_accounts[0] == new_account2, "Incorrectly updated last_used_accounts"


def test_find_accounts_by_short_name():
    # given
    short_name = "bc"
    new_account1 = BankAccount("rec", "add1", "add2", "abc")
    new_account2 = BankAccount("rec", "add1", "add2", "bcd")
    new_account3 = BankAccount("rec", "add1", "add2", "cde")

    app.add_account(new_account1)
    app.add_account(new_account2)
    app.add_account(new_account3)

    # when
    filtered_accounts = app.find_accounts_by_phrase(short_name)

    # then
    assert len(filtered_accounts) == 2, "Incorrectly filtered accounts by short name"
    assert new_account1 in filtered_accounts and new_account2 in filtered_accounts, "Incorrectly filtered accounts by short name"


def test_find_correct_new_account_index():
    # given
    new_account1 = BankAccount("rec", "add1", "add2", "aaa")
    new_account2 = BankAccount("rec", "add1", "add2", "bbb")
    new_account3 = BankAccount("rec", "add1", "add2", "ddd")

    app.add_account(new_account1)
    app.add_account(new_account2)
    app.add_account(new_account3)

    new_account4 = BankAccount("rec", "add1", "add2", "ccc")

    # when
    new_index = app.get_new_account_index(new_account4)

    # then
    assert new_index == 2, "Incorrectly found index for new account"


def test_find_correct_new_account_index_for_empty_list():
    # given
    new_account4 = BankAccount("rec", "add1", "add2", "ccc")

    # when
    new_index = app.get_new_account_index(new_account4)

    # then
    assert new_index == 0, "Incorrectly found index for new account"


def clear_accounts():
    app.all_accounts = []
    app.last_used_accounts = []


test_add_new_account()
clear_accounts()

test_add_new_accounts_alphabetically()
clear_accounts()

test_find_accounts_by_short_name()
clear_accounts()

test_find_correct_new_account_index()
clear_accounts()

test_find_correct_new_account_index_for_empty_list()
clear_accounts()

test_update_last_used_accounts()
clear_accounts()

print("All tests passed")