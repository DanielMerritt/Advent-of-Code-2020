import re


def short_eval(match):
    pattern = re.compile(r"(\d+) ([+*]) (\d+)")
    newmatch = pattern.search(match[0])
    if newmatch[2] == "+":
        return str(int(newmatch[1]) + int(newmatch[3]))
    elif newmatch[2] == "*":
        return str(int(newmatch[1]) * int(newmatch[3]))
    

def simplify(match):
    pattern = re.compile(r"\d+ [+*] \d+")
    return pattern.sub(short_eval, match[0], count=1)


def eval_expression(expression):
    pattern = re.compile(r"\([^(]*?\)")
    done_pattern = re.compile(r"\d+$")
    while not done_pattern.match(expression):
        new = pattern.sub(simplify, expression)
        if expression != new:
            expression = new
        else:
            expression = re.sub(r"\d+ [+*] \d+", short_eval, expression, count=1)
            
        expression = re.sub(r"\((\d+)\)", lambda x: x[1], expression)
    return int(expression)
    

def main():
    total = 0
    with open("18-1_input.txt") as f:
        for i in f:
            i = i.strip()
            total += eval_expression(i)
    print(total)

if __name__ == "__main__":
    main()
