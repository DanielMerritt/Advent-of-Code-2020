def process_input():
    plan = []
    with open("11-1_input.txt") as f:
        for i in f:
            i = i.strip()
            temp = [j for j in i]
            plan.append(list(temp))
    return plan


def count_adjacent_people(index, plan):
    total = 0
    if index[1] < len(plan[index[0]])-1: ## right
        if plan[index[0]][index[1]+1] == "#":
            total += 1

    if index[1] > 0: ## left
        if plan[index[0]][index[1]-1] == "#":
            total += 1

    if index[0] < len(plan)-1: ## down
        if plan[index[0]+1][index[1]] == "#":
            total += 1

    if index[0] > 0: ## up
        if plan[index[0]-1][index[1]] == "#":
            total += 1
            
    if index[0] > 0 and index[1] < len(plan[index[0]])-1: ##up right
        if plan[index[0]-1][index[1]+1] == "#":
            total += 1

    if index[1] > 0 and index[0] > 0: ##up left
        if plan[index[0]-1][index[1]-1] == "#":
            total += 1

    if index[0] < len(plan)-1 and index[1] < len(plan[index[0]])-1: # down right
        if plan[index[0]+1][index[1]+1] == "#":
            total += 1

    if index[0] < len(plan)-1 and index[1] > 0: # down left
        if plan[index[0]+1][index[1]-1] == "#":
            total += 1
    return total


def main():
    plan = process_input()
    while True:
        new_plan = []
        for i in range(len(plan)):
            temp = []
            for j in range(len(plan[0])):
                if plan[i][j] == ".":
                    temp.append(".")
                    
                elif plan[i][j] == "L":
                    if count_adjacent_people((i,j), plan) == 0:
                        temp.append("#")
                    else:
                        temp.append("L")
                        
                elif plan[i][j] == "#":
                    if count_adjacent_people((i,j), plan) >= 4:
                        temp.append("L")
                    else:
                        temp.append("#")
            new_plan.append(list(temp))
        if plan == new_plan:
            break
        plan = list(new_plan)

    occupied = 0
    for i in plan:
        for j in i:
            if j == "#":
                occupied += 1

    print(occupied)
        
if __name__ == "__main__":
    main() 
                      
                      
