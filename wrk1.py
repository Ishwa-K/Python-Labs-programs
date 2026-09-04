stu=['A',"B","C","D"]
print(stu)
stu.append("X")
print(stu)
stu.extend("Y")
print(stu)
stu.insert(3,"Z")
print(stu)
stu=['A', 'B', 'C', 'Z', 'D', 'X', 'Y']
stu.remove('C')
print(stu)
stu=['A', 'B', 'C', 'D','Z', 'D', 'X', 'Y']
stu.remove('D')
print(stu)
stu.pop()
stu.clear()
print(stu)
stu=['A', 'B', 'C', 'D','Z', 'D', 'X', 'Y']
stu.reverse()
print(stu)
stu.sort()
print(stu)