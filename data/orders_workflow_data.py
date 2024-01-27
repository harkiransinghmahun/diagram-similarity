# Keys
# sq1 and sq2


client_workflow_map = {
    "ntex": ["order_filled", "order_partial_filled", "cancel_order", "cancel_partial_fill_order", "order_rejected"],
    "ubs":  ["order_filled", "order_partial_filled", "cancel_order", "cancel_partial_fill_order", "order_rejected", "order_expired", "amend_order"]
}

workflow_messages_map_1 = {
    "order_filled":              ["submit_order", "pending_new_order", "order_accept", "order_fill"],
    "order_partial_filled":      ["submit_order", "pending_new_order", "order_accept", "order_partial_fill", "order_fill"],
    "cancel_order":              ["submit_order", "pending_new_order", "order_accept", "cancel_request", "order_cancel"],
    "cancel_partial_fill_order": ["submit_order", "pending_new_order", "order_accept", "order_partial_fill", "order_cancel"],
    "order_rejected":            ["submit_order", "pending_new_order", "order_reject"]
}

workflow_messages_map_2 = {
    "order_filled":              ["submit_order", "order_accept",  "order_fill"],
    "order_partial_filled":      ["submit_order", "order_accept",  "order_partial_fill", "order_fill"],
    "cancel_order":              ["submit_order", "order_accept",  "cancel_request", "pending_cancel_request", "order_cancel"],
    "cancel_partial_fill_order": ["submit_order", "order_accept",  "order_partial_fill", "cancel_request", "pending_cancel_request", "order_cancel"],
    "order_rejected":            ["submit_order", "order_reject"],
    "order_expired":             ["submit_order", "order_accept", "order_expire"],
    "amend_order":               ["submit_order", "order_accept", "order_amend_request", "pending_order_amend_request", "order_amend", "order_fill"]
}


client_workflow_message_map = {
    "ntex": workflow_messages_map_1,
    "ubs":  workflow_messages_map_2
}


messages_1 = [
                ["Jefferies", "submit_order"       , "Client"]    ,
                ["Jefferies", "cancel_request"     , "Client"]    ,
                ["Client"   , "pending_new_order"  , "Jefferies"] ,
                ["Client"   , "order_accept"       , "Jefferies"] ,
                ["Client"   , "order_reject"       , "Jefferies"] ,
                ["Client"   , "order_fill"         , "Jefferies"] ,
                ["Client"   , "order_partial_fill" , "Jefferies"] ,
                ["Client"   , "order_cancel"       , "Jefferies"] ,
             ]

messages_2 = [
                ["Jefferies", "submit_order"             , "Client"]    ,
                ["Jefferies", "order_amend_request"      , "Client"]    ,
                ["Jefferies", "cancel_request"           , "Client"]    ,
                ["Client"   , "order_accept"                , "Jefferies"] ,
                ["Client"   , "order_reject"                , "Jefferies"] ,
                ["Client"   , "order_fill"                  , "Jefferies"] ,
                ["Client"   , "order_partial_fill"          , "Jefferies"] ,
                ["Client"   , "pending_order_amend_request" , "Jefferies"] ,
                ["Client"   , "order_amend_"                , "Jefferies"] ,
                ["Client"   , "pending_cancel_request"      , "Jefferies"] ,
                ["Client"   , "order_cancel"                , "Jefferies"] ,
                ["Client"   , "order_expire"                , "Jefferies"] ,
             ]

client_message_map = {
    "ntex": messages_1,
    "ubs":  messages_2
}