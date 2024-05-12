def generate_code_block(group_index):
    code_block = f"""defined_text = {{
    name = GetTag_{group_index}
    random = no
"""
    for i in range(1, 101):  # for 100 costs
        cost_letter = chr(64 + i)  # Convert 1 to 'A', 2 to 'B', and so on
        code_block += f"""
    text = {{
        localisation_key = as_tag_{i}{chr(64 + group_index)}
        trigger = {{
            has_country_flag = as_alliance_group_{i}
        }}
    }}"""
    code_block += "\n}\n"
    return code_block

# Writing code blocks to file with UTF-8 encoding
with open("output.txt", "w", encoding="utf-8") as file:
    for group_index in range(1, 11):  # for 10 alliance groups
        code_block = generate_code_block(group_index)
        file.write(code_block + "\n\n")
