file = open("input/day-10-input.txt")
lines = [list(line.strip()) for line in file.readlines()]

stack = []
error_score = 0
corrupted = []

for i, line in enumerate(lines):
    for c in line:
        if c == "(" or c == "[" or c == "{" or c == "<":
            stack.append(c)
        elif c == ")":
            if stack[-1] != "(":
                error_score += 3
                corrupted.append(i)
                break
            else:
                stack.pop()
        elif c == "]":
            if stack[-1] != "[":
                error_score += 57
                corrupted.append(i)
                break
            else:
                stack.pop()
        elif c == "}":
            if stack[-1] != "{":
                error_score += 1197
                corrupted.append(i)
                break
            else:
                stack.pop()
        elif c == ">":
            if stack[-1] != "<":
                error_score += 25137
                corrupted.append(i)
                break
            else:
                stack.pop()

    stack = []

# print("syntax error score: {}".format(error_score))     # part 1

n = len(corrupted)
for i in range(n - 1, -1, -1):
    lines.pop(corrupted[i])

scores = []
score = 0

def delete(c, stack):
    for i in range(len(stack) -1, -1, -1):
        if stack[i] == c:
            stack.pop(i)
            break

for line in lines:
    for c in line:
        if c == "(" or c == "[" or c == "{" or c == "<":
            stack.append(c)
        elif c == ")":
            delete("(", stack)
        elif c == "]":
            delete("[", stack)
        elif c == "}":
            delete("{", stack)
        elif c == ">":
            delete("<", stack)

    for i in range(len(stack) - 1, -1, -1):
        s = stack[i]
        if s == "(":
            score = score * 5 + 1
        elif s == "[":
            score = score * 5 + 2
        elif s == "{":
            score = score * 5 + 3
        elif s == "<":
            score = score * 5 + 4

    scores.append(score)
    score = 0
    stack = []

scores.sort()
middle = int(len(scores) / 2)

print("median score: {}".format(scores[middle]))    # part 2
