def calc():
    operators = ['-', '+', '/', '*', '%']
    operationList = []
    user = "active"
    print('|\n|\n|')
    while(user == 'active'):
        num = input("\nEnter '=' at any moment to quit.\n\nEnter a number: ")
        if num == '=':
            user = "dead"
            break
        try:
            int(num)
            operationList.append(num)

        except:
            print("Invalid input")
            continue

        op = input("\nEnter '=' at any moment to quit.\n\nEnter an operator: ")        

        if op == '=':
            user = "dead"
            break
        elif op not in operators:
            Exception("Invalid input")
        else: operationList.append(op)


    print(''.join(operationList))
    ans = ''
    try:
        ans = eval(''.join(operationList))
    except:
        print("Invalid operation! Try again.")
    
    print(ans)


calc()