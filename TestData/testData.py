valid_users = [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
    ("visual_user", "secret_sauce"),
    ("error_user", "secret_sauce"),
]

invalid_users=[ 
    ("standardUser", "secret_sauce"),
    ("standard_user", "secret_user"),
    ("standard_use", "secret_user"),
    ("", "")
]

locked_user = ("locked_out_user", "secret_sauce")
