import sys
from collections import deque

n = sys.stdin.readline().strip()
left_stack = deque(n) 
right_stack = deque()  

m = int(sys.stdin.readline())
for _ in range(m):
    cmd = sys.stdin.readline().split()
    if cmd[0] == "L" and left_stack:
        right_stack.appendleft(left_stack.pop())
    elif cmd[0] == "D" and right_stack:
        left_stack.append(right_stack.popleft())
    elif cmd[0] == "B" and left_stack:
        left_stack.pop()
    elif cmd[0] == "P":
        left_stack.append(cmd[1])
        
print("".join(left_stack) + "".join(right_stack))
