""" --- Day 4: Ceres Search --- """
import re

def search_word(input: list):
    match = []
    for strings in input:
        """ search left and right """
        pattern = r'(?=(XMAS|SAMX))'
        if re.findall(pattern, strings):
            match.append(re.findall(pattern, strings))
    return match

def vertical_strings(input: list):
    verticals = []
    j  = 0
    while j < len(input[0]):
        i = 0
        string = ""
        while i < len(input):
            string += input[i][j]
            i += 1
        verticals.append(string)
        j += 1
    return verticals

def diagonal_strings(input: list):
    length , width = len(input) , len(input[0])
    diagonals = []
    i = 0
    while i < length:
        string = ""
        j = i
        k = 0
        while j < length:
            string += input[j][k]
            if k < width:
                k += 1
            j += 1
        diagonals.append(string)
        i += 1
    for j in range(1, width):
        string = ""
        row, col = 0, j
        while row < length and col < width:
            string += input[row][col]
            row += 1
            col += 1
        diagonals.append(string)
    return diagonals 


def file_to_list(filename):
    try:
        with open(filename, 'r') as file:  # Open the file in read mode
            lines = [line.strip() for line in file]  # Strip newline characters and create a list
        return lines
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

input = file_to_list("day4.txt")
all_results = (
    search_word(input) +
    search_word(vertical_strings(input)) +
    search_word(diagonal_strings(input)) +
    search_word(diagonal_strings([string[::-1] for string in input])) 
)
def count_matches(results):
    count = 0
    for item in results:
        if isinstance(item, list):  # If the item is a list, sum its length
            count += count_matches(item)
        else:  # Otherwise, it's a single match
            count += 1
    return count
total_matches = count_matches(all_results)
print(total_matches)
