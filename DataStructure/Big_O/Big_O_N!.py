import cProfile

def faculty(n):
    if n <= 1:
        return 1
    return n * faculty(n - 1)

def counter(n):
    cnt = 0
    for i in range(n):
        cnt += 1
    return cnt
print(f"for (10)! = {faculty(10)}")
cProfile.run("counter(faculty(10))")
print(f"for (11)! = {faculty(11)}")
cProfile.run("counter(faculty(11))")
print(f"for (12)! = {faculty(12)}")
cProfile.run("counter(faculty(12))")
print(f"for (13)! = {faculty(13)}")
cProfile.run("counter(faculty(13))")
