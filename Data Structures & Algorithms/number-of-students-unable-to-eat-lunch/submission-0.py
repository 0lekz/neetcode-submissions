from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        students = deque(students)
        sandwiches = deque(sandwiches)
        flag = 0

        while flag < n:
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                n -= 1
                flag = 0
                continue
            students.append(students.popleft())
            flag += 1
        return len(students)
