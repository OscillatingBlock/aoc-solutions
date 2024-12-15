def get_rules_update(filename):
    with open("day5.txt") as new_file:
        rules = {}
        update = []
        for lines in new_file:
            lines = lines.replace("\n", "")
            if "|" in lines:
                parts = lines.split("|")
                if parts[0] not in rules:
                    rules[parts[0]] = [] 
                    rules[parts[0]].append(parts[1])
                else:
                    rules[parts[0]].append(parts[1])
            if "," in lines:
                updates = lines.split(",")
                update.append(updates)
    return rules, update

def check_update(update: list, rules: dict):
    i, sum = 0, 0
    for i in range(len(update)):
        check = 0
        j = 0
        for j in range(len(update[i])) :
            if update[i][j] not in rules:
                check += 1
            else:
                if check_list(update[i], j):
                    check += 1
            if check == len(update[i]):
                middle = len(update[i]) // 2
                sum += int(update[i][middle])
    return sum

def check_list(line: list, rank: int):
    for item in rules[line[rank]]:
        if item in line:
            item_rank = find_rank(item, line)
            if item_rank < rank:
                return False
    return True

def find_rank(item: int, rule_list: list):
    i = 0
    for i in range(len(rule_list)):
        if rule_list[i] == item:
            return i 

rules, update = get_rules_update("day5.txt")
print(check_update(update, rules))
