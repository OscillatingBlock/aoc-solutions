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
    column2.sort()
    return [column1, column2]

def compare_columns(column1: list, column2: list):
    if len(column1) != len(column2):
        raise ValueError("Column length should be same")
    distances = [abs(int(column1[i]) - int(column2[i])) for i in range(len(column1))]
    return distances

def main():
    file_name = "day1_input.txt"
    columns = sort_input_in_columns(file_name)
    column1, column2 = columns[0], columns[1]
    total_distance = sum(compare_columns(column1, column2))
    print(f"The total distance is: {total_distance}")

if __name__ == "__main__":
    main()

