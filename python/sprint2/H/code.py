
strinput = input()
stack = []
Verify = True

for lt in strinput:
    if lt in "([{":
        stack.append(lt)
    elif lt in ")]}":
        if len(stack) == 0:
            Verify = False
            break
        br = stack.pop()
        if br == '(' and lt == ')':
            continue
        if br == '[' and lt == ']':
            continue
        if br == '{' and lt == '}':
            continue

        Verify = False
        break

if Verify and len(stack) == 0:
    print("True")
else:
    print("False")
