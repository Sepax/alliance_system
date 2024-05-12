def generate_code_block(index):
    code_block = f"""custom_text_box = {{ 
    name = as_slot_cost_{index}
    potential = {{ 
        check_variable = {{
            which = as_treaty_count
            value = {index}
	    }}
    }}
}}"""
    return code_block

# Writing code blocks to file
with open("output.txt", "w") as file:
    for i in range(1, 11):  # Change 11 to the desired number of blocks
        code_block = generate_code_block(i)
        file.write(code_block + "\n\n")
