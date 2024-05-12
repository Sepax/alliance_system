def generate_code_block(index):
    code_block = f"""else_if = {{ limit = {{ ROOT = {{ has_country_flag = as_alliance_group_{index} }} }}
    if = {{ limit = {{ ROOT = {{ check_variable = {{ which = event_target_counter value = 1 }} NOT = {{ check_variable = {{ which = event_target_counter value = 2 }} }} }} }} save_global_event_target_as = treaty_{index}A }}
    else_if = {{ limit = {{ ROOT = {{ check_variable = {{ which = event_target_counter value = 2 }} NOT = {{ check_variable = {{ which = event_target_counter value = 3 }} }} }} }} save_global_event_target_as = treaty_{index}B }}
    else_if = {{ limit = {{ ROOT = {{ check_variable = {{ which = event_target_counter value = 3 }} NOT = {{ check_variable = {{ which = event_target_counter value = 4 }} }} }} }} save_global_event_target_as = treaty_{index}C }}
    else_if = {{ limit = {{ ROOT = {{ check_variable = {{ which = event_target_counter value = 4 }} NOT = {{ check_variable = {{ which = event_target_counter value = 5 }} }} }} }} save_global_event_target_as = treaty_{index}D }}
    else_if = {{ limit = {{ ROOT = {{ check_variable = {{ which = event_target_counter value = 5 }} NOT = {{ check_variable = {{ which = event_target_counter value = 6 }} }} }} }} save_global_event_target_as = treaty_{index}E }}
    else_if = {{ limit = {{ ROOT = {{ check_variable = {{ which = event_target_counter value = 6 }} NOT = {{ check_variable = {{ which = event_target_counter value = 7 }} }} }} }} save_global_event_target_as = treaty_{index}F }}
    else_if = {{ limit = {{ ROOT = {{ check_variable = {{ which = event_target_counter value = 7 }} NOT = {{ check_variable = {{ which = event_target_counter value = 8 }} }} }} }} save_global_event_target_as = treaty_{index}G }}
    else_if = {{ limit = {{ ROOT = {{ check_variable = {{ which = event_target_counter value = 8 }} NOT = {{ check_variable = {{ which = event_target_counter value = 9 }} }} }} }} save_global_event_target_as = treaty_{index}H }}
    else_if = {{ limit = {{ ROOT = {{ check_variable = {{ which = event_target_counter value = 9 }} NOT = {{ check_variable = {{ which = event_target_counter value = 10 }} }} }} }} save_global_event_target_as = treaty_{index}I }}
    else_if = {{ limit = {{ ROOT = {{ check_variable = {{ which = event_target_counter value = 10 }} NOT = {{ check_variable = {{ which = event_target_counter value = 11 }} }} }} }} save_global_event_target_as = treaty_{index}J }}
}}"""
    return code_block

# Writing code blocks to file
with open("output.txt", "w") as file:
    for i in range(1, 101):
        code_block = generate_code_block(i)
        file.write(code_block + "\n\n")
