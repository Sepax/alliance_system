def generate_code_block(group_index, treaty_index):
    code_block = f"""as_cost_{group_index}{treaty_index}: "£as_cost£ §R[treaty_{group_index}{treaty_index}.as_cost.GetValue]§!" """
    return code_block

# Writing code blocks to file
with open("output.txt", "w") as file:
    for group_index in range(1, 101):  # for 10 groups
        for treaty_index in "ABCDEFGHIJ":
            code_block = generate_code_block(group_index, treaty_index)
            file.write(code_block + "\n")
