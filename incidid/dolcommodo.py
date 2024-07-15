lines_with_values = []
with open('file.txt', 'r') as file:
    for line_number, line in enumerate(file, start=1):
        value = '1'  # Replace '1' with the desired value
        line = line.strip() + ',' + value + '\n'
        lines_with_values.append(line)

with open('file.txt', 'w') as file:
    file.writelines(lines_with_values)
