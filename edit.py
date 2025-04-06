input_filename = input("Enter the name of the file to read: ")
with open(input_filename, 'r') as infile:
    output_filename = input("Enter the name for the new modified file: ")
    with open(output_filename, 'w') as outfile:
        for line in infile:
            modified_line = line.strip() + " [MODIFIED]\n"
            outfile.write(modified_line)
    print(f"Successfully read '{input_filename}' and wrote modified content to '{output_filename}'.")

print("File processing complete.")