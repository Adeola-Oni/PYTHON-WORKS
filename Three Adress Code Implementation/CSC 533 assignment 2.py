order_of_precedence = {"=":-1,"(":-1, ")":-1, "~":0, "+":1, "-":1, "*":2, "/":2, "^":3}
user_input = input("Please input expression : ")

def inftoPost(expression):
    variable = []
    operands = []
    for x in range(len(expression)):
        if expression[x] not in order_of_precedence:
            variable.append(expression[x])
        else:
            if len(operands)!=0:
                while order_of_precedence[expression[x]] <= order_of_precedence[operands[-1]]:
                    variable.append(operands.pop())
                    if len(operands)==0:
                        break
            operands.append(expression[x])
    
    while len(operands)>0:
        variable.append(operands.pop())
    return variable
print(inftoPost(user_input))

collapsed = {}
def collapse(old_list):
    buffer = []
    if(len(old_list) > 2):
        while old_list[-2] in order_of_precedence.keys() or old_list[-3] in order_of_precedence.keys():
            if old_list[-2] in order_of_precedence.keys() and order_of_precedence[old_list[-2]] == 0:
                collapsed["t{}".format(len(collapsed) + 1)]=(old_list[-3], old_list[-2])
                buffer.append(old_list.pop())
                old_list = old_list[:-2] + ["t{}".format(len(collapsed))] + buffer[::-1]
            else:
                buffer.append(old_list.pop())
        collapsed["t{}".format(len(collapsed) + 1)]=(old_list[-3], old_list[-2], old_list[-1])
        old_list = old_list[:-3] + ["t{}".format(len(collapsed))] + buffer[::-1]
        collapse(old_list)
        
    return collapsed  
#print(collapse(['2', '3', '-', '4', '7', '*', '2', '2', '^', '/', '+']))


def Quadruple(input_):
    keys = input_.keys()
    print("QUADRUPLE CODE GENERATOR")
    print("OP   ||   ARG1   ||  ARG2   ||   RES")
    for key in keys:
        if len(input_[key]) > 2:
            print(input_[key][2],"   ||   ",input_[key][0],"   ||   ",input_[key][1],"   ||   ",key)
        else:            
            print(input_[key][1],"   ||   ",input_[key][0],"   ||   ",'--',"   ||   ",key)
    
    
#print(Quadruple({'t1': ('2', '2', '^'), 't2': ('4', '7', '*'), 't3': ('t2', 't1', '/'), 
                 #'t4': ('2', '3', '-'), 't5': ('t4', 't3', '+')}))


def Triple(input_):
    keys = input_.keys()
    index = {}
    print("TRIPLE CODE GENERATOR")
    print("     ||   OP    ||   ARG1   ||  ARG2   ")
    
    i = 0
    for key in keys:
        index[key] = i
        i += 1
                
    for x in keys:
        if x in index.keys():
            if len(input_[x]) > 2:
                if input_[x][0] in index:
                    first = "({})".format(index[input_[x][0]])
                else:
                    first = input_[x][0]
                #first =  index[input_[x][0]]  if input_[x][0] in index else input_[x][0]
                
                if input_[x][1] in index:
                    second = "({})".format(index[input_[x][1]])
                else:
                    second = input_[x][1]
                print(index[x],"   ||   ",input_[x][2],"   ||   ",first,"   ||   ",second)
            else:            
                if input_[x][0] in index:
                    first = "({})".format(index[input_[x][0]])
                else:
                    first = input_[x][0]
                print(index[x],"   ||   ",input_[x][1],"   ||   ", first ,"   ||   ", '--')

#print(Triple({'t1': ('2', '2', '^'), 't2': ('4', '7', '*'), 't3': ('t2', 't1', '/'), 
                # 't4': ('2', '3', '-'), 't5': ('t4', 't3', '+')}))