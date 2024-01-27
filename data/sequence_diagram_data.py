# Keys
# sq1 and sq2

sequence_diagrams = ["sq1", "sq2"]

objects_map = {
    "sq1": ["cust", "atm", "account", "check_in"],
    "sq2": ["client", "atm", "account", "check_in"],
}

object_message_map_1 = {
    "cust":     [],
    "atm":      ["enter_option", "request_amount", "enter_amount", "success", "dispense_cash", "request_take_action", "take_cash", "request_continuation", "terminate"],
    "account":  ["process_transaction"],
    "check_in": ["withdraw_from_checking_account"]
}

object_message_map_2 = {
    "client":   ["request_amount", "request_take_cash", "request_continuation"],
    "atm":      ["enter_kind", "enter_amount", "process_successful", "dispense_cash", "take_cash", "terminate", "print_receipt"],
    "account":  ["process_transaction", "withdraw_successful"],
    "check_in": ["withdraw_from_checking_account"]
}

messages_1 = [
                ["cust", "Customer", "async_call", "enter_option", "atm", "ATM"],
                ["atm",  "ATM", "sync_call", "request_amount", "atm", "ATM"],
                ["cust", "Customer", "async_call", "enter_amount", "atm", "ATM"],
                ["atm", "ATM", "sync_call", "process_transaction", "account", "Account"],
                ["account", "Account", "sync_call", "withdraw_from_checking_account", "check_in", "CheckInAccount"],
                ["account", "Account", "reply", "success", "atm", "ATM"],
                ["atm", "ATM", "sync_call", "dispense_cash", "atm", "ATM"],
                ["atm", "ATM", "sync_call", "request_take_action", "atm", "ATM"],
                ["cust", "Customer", "async_call", "take_cash", "atm", "ATM"],
                ["atm", "ATM", "sync_call", "request_continuation", "atm", "ATM"],
                ["cust", "Customer", "async_call", "terminate", "atm", "ATM"],
             ]

messages_2 = [
                ["client", "Client", "async_call", "enter_kind", "atm", "ATM"],
                ["atm",  "ATM", "reply", "request_amount", "client", "Client"],
                ["client", "Client", "async_call", "enter_amount", "atm", "ATM"],
                ["atm", "ATM", "sync_call", "process_transaction", "account", "Account"],
                ["account", "Account", "sync_call", "withdraw_from_checking_account", "check_in", "CheckInAccount"],
                ["check_in", "CheckInAccount", "reply", "withdraw_successful", "account", "Account"],
                ["account", "Account", "reply", "process_successful", "atm", "ATM"],
                ["atm", "ATM", "sync_call", "dispense_cash", "atm", "ATM"],
                ["atm", "ATM", "reply", "request_take_action", "client", "Client"],
                ["client", "Client", "async_call", "take_cash", "atm", "ATM"],
                ["atm", "ATM", "sync_call", "request_continuation", "client", "Client"],
                ["client", "Client", "async_call", "terminate", "atm", "ATM"],
                ["atm", "ATM", "sync_call", "print_receipt", "atm", "ATM"],
             ]