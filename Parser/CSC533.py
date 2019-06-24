rules = {}
no_grammar_input = input("Please input number of lines of your grammar : ")
print(no_grammar_input)

for i in range(int(no_grammar_input)):
    grammar = input("Please input your grammar : ")
    new_grammar = grammar.split(":=>")
    keys = new_grammar[1].split("|")
    for i in keys:
        rules[i] = new_grammar[0]
    
print(rules)


input_string = input("Please enter the string to be tested by your grammar: ")
stack = ""

for x in range(len(input_string)):
    stack += input_string[x]
    for i in range(len(stack)-1, -1, -1):
        not_reduce = False
        while not not_reduce:
            not_reduce = True
            if stack[i:] in rules:
                value_in_rules = rules[stack[i:]]
                print('{}->{}'.format(value_in_rules, stack[i:]))
                stack = stack.replace(stack[i:], value_in_rules, -1)
                not_reduce = False
    print("{}{}".format(stack, input_string[x + 1:]))
        
        


