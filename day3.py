""" --- Day 3: Mull It Over --- """
import re

def mul(string: str):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    match = re.findall(pattern, string)
    return [int(a)*int(b) for a, b in match] 

file_name = "day3_input.txt"
with open(file_name) as new_file:
    ans = 0
    for line in new_file:
         ans += sum(mul(line))

print(ans)

