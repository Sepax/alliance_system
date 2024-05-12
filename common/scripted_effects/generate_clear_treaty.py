def generate_code_block(index):
    code_block = f"""else_if = {{
    limit = {{ has_country_flag = as_alliance_group_{index} }}
"""
    for letter in "ABCDEFGHIJ":
        code_block += f"\tclear_global_event_target = treaty_{index}{letter}\n"
    code_block += "}"
    return code_block

# Writing code blocks to file
with open("output.txt", "w") as file:
    for i in range(1, 101):  # Change 3 to the number of blocks you want
        code_block = generate_code_block(i)
        file.write(code_block + "\n\n")
