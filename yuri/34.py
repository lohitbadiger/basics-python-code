
def names(dictionary):
    for key, val in dictionary.items():
        print(f' At spiceup {key} is handled to {val}')




assignment={}

while True:
    program=input("enter the name of Progrmming Language")
    
    student=input('enter the name of the student')
    
    assignment[program]=student
    
    another=input('do u want to Add one more item (y/n) ')
    if another=='y':
        continue
    else:
        break


names(assignment)