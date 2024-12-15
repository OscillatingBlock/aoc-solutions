def check_file(file_name: str):
    answer = 0
    with open(file_name) as new_file:
        for line in new_file:
            parts = line.split(" ")
            if check(parts):
                answer += 1
    return answer

def check(series: list):
    i = 1
    new_series = [int(item) for item in series]
    series = new_series
    if series[i] < series[i-1]:
        """ decreasing order"""
        while i in range(len(series)) :
            if series[i] in range(series[i-1] -3, series[i-1]):
                if i == len(series) -1:
                    return True
                i += 1
            else:
                return False
    while i in range(len(series)):
            """increasing order"""
            if series[i] in range(series[i-1] +1, series[i-1] + 4):
                if i == len(series) - 1:
                    return True
                i += 1
            else:
                return False
                
if __name__ == "__main__":
    print(check_file("day2_input.txt"))
