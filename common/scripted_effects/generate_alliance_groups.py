def generate_code_block(index):
    code_block = f"""else_if = {{
    limit = {{ NOT = {{ has_global_flag = as_alliance_group_{index}_set }} }}
    set_country_flag = as_alliance_group_{index}
    set_global_flag = as_alliance_group_{index}_set
}}"""
    return code_block

# Writing code blocks to file
with open("output.txt", "w") as file:
    for i in range(1, 101):  # Change 101 to the desired number of blocks
        code_block = generate_code_block(i)
        file.write(code_block + "\n\n")
