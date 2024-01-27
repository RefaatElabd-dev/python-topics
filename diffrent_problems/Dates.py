# Enter your code here. Read input from STDIN. Print output to STDOUT

actually_date = list(int(i) for i in input().strip().split())
due_date = list(int(i) for i in input().strip().split())

fine = 0
if(actually_date[2] > due_date[2]):
    fine = 10000
elif(actually_date[2] == due_date[2]):
    if(actually_date[1] > due_date[1]):
        fine = 500 * (actually_date[1] - due_date[1])
    elif(actually_date[1] == due_date[1]):
        if(actually_date[0] > due_date[0]):
            fine = 15 * (actually_date[0] - due_date[0])

print(fine)