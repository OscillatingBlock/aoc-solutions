def sort_input_in_columns(file_name: str):
    with open(file_name) as new_file:
        column1 = []
        column2 = []
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split("  ")
            column1.append(parts[0])
            column2.append(parts[1])
    
    column1.sort()
    print(column1)
    column2.sort()
    return [column1, column2]

def compare_columns(column1: list, column2: list):
    if len(column1) != len(column2):
        return ValueError("Column length should be same")
    distances = [abs(int(column1[i]) - int(column2[i])) for i in range(len(column1))]
    return distances

column = sort_input_in_columns("day1_input.txt")
column1, column2 = column[0] , column[1]
print(sum(compare_columns(column1, column2)))
