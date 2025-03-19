
from collections import deque


q=deque()
q.append(1)
q.append(5)
q.append(4)
q.append(3)


print(q.popleft())
print(q)
