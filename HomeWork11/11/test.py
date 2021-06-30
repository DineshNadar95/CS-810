def braces(values):
    result = []
    map = {")": "(", "}": "{", "]": "["}
    for value in values:
        stack = []
        flag = True
        for c in value:
            if flag == True:
                if c in map:
                    t_element = stack.pop() if stack else '#'
                    if map[c] != t_element:
                        result.append("NO")
                        flag = False
                else:
                    stack.append(c)

            if stack == []:
                    result.append("Yes")
    return result


if __name__ == "__main__":
    s = ['2',
         '{}[]()',
         "{[}]]"]
    print(braces(s))
