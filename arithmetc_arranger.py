def arithmetic_arranger(problems, show_asw):
    operands_1 = list()
    operands_2 = list()
    operators = list()
    answers = list()
    width = list()
    gap = 0
   
    # Check if there's too many problems.
    if len(problems) > 5:
        return "Error: Too many problems."
   
    for p in problems:
        # Check if is addition and/or subtraction. 
        if "*" in p or "/" in p:
            return "Error: Operator must be '+' or '-'."
        else:
            problem = p.split()
            # Is a digit?
            if problem[0].isdigit() and problem[2].isdigit():
                operands_1.append(problem[0])
                operands_2.append(problem[2])
                operators.append(problem[1])
            else:
                return "Error: Numbers must only contain digits."
               
            # Is the lenght hiegher than for?
            if len(problem[0]) > 4 or len(problem[2]) > 4:
                return "Error: Numbers cannot be more than four digits."

            # Get the answer for each equation
            if problem[1] == "+":
              answers.append(str(int(problem[0]) + int(problem[2])))
            else:
              answers.append(str(int(problem[0]) - int(problem[2])))
   
   
    # Get the width of each problem on screen
    for i in range(len(problems)):
      if len(operands_1[i]) >= len(operands_2[i]):
          width.append(len(operands_1[i]))
      else:
          width.append(len(operands_2[i]))

    # Print the problems on screen
    for i in range(len(problems)):
        print(operands_1[i].rjust(width[i]+2), end=" "*4)   

    print("") # Creats a new line

    for i in range(len(problems)):
        print(operators[i], operands_2[i].rjust(width[i]), end=" "*4)

    print("") # Creats a new line

    for i in range(len(problems)):
        print("-"*(width[i]+2), end=" "*4)

    print("") # Creats a new line

    if show_asw:
        for i in range(len(problems)):
            print(answers[i].rjust(width[i]+2), end=" "*4)


    
    return ""