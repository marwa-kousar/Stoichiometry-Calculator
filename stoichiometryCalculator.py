# Assignment 1
# Name: Marwa Kousar

# This code solves a chemistry solution problem using the equation M1V1=M2V2
# Converts mL to L when needed
# And tells the user how many significant digits the answer should be rounded to

ques = input("Do you want to solve a dilution question? Yes or No. ")
if ques == "Yes":
    m1 = float(input("What is your initial concentration? If there is not one, type 0. "))
    v1 = float(input("What is your initial volume? If there is not one, type 0. "))
    m2 = float(input("What is your final concentration? If there is not one, type 0. "))
    v2 = float(input("What is your final volume? If there is not one, type 0. "))
    # these codes ask the user what values they have
    # if the user input is 0, this program will solve for that missing value
    if m1 == 0:
        # if the user does not have a value for M1 and had input 0, then this code continues to solve for M1
        unitm = input("Are your units for concentration L/mol? Yes or no. ")
        # asks the user to confirm if concentration units are L/mol
        if unitm == "Yes":
            # if the user inputs 'Yes' to the units of concentration
            unitv = input("Are your units for volume in L? If not what unit. ")
            # asks the user to confirm if volume units are L
            # if user has a different volume unit, which is mL, then the user must print 'mL'
            if unitv == "Yes":
                # if the user inputs 'Yes' to the units of volume being 'L', then this code continues to solve for M1
                print("V1 =", v1, "L ", "M2 =", m2, "L/mol ", "V2 =", v2, "L ", "M1 = ?")
                # prints the values with the units, showing the missing value
                solve = input("Solving for initial concentration.... ")
                m1 = (m2 * v2) / v1
                # solves for m1, by using the rearranged equation of M1V1=M2V2
                print("Therefore, M1 =", m1, "L/mol")
                # prints the final answer with its unit
                list1 = [v1, m2, v2]
                # collects the values given, excluding the answer, into a list to begin finding the number of sig. digs.
                count = 0
                if min(list1) < 1:
                    # the min(list1) function finds the smallest number within the list
                    # if the smallest number within the list is less than 1 (e.x. 0.67), then this code continues to
                    # find sig. digs.
                    for i in str(min(list1)):
                        # the for loop uses a counter to find the number of digits in the smallest value
                        # the function str(min(list1)) converts the smallest value to a str
                        if i != ".":
                            # a decimal '.' does not count as a sig. dig.
                            # if the values are not a decimal, then they are counted as a digit
                            count += 1
                    print("Round answer to", count - 1,
                          "significant digits. Thank you for using dilution calculator :) ")
                    # Since the smallest number is less than 1, and contains a zero to the left of the decimal,
                    # the 0 is not counted as a sig. dig. (e.x. 0.67)
                    # Because the counter, includes 0 as a digit, to get the right sig. digs. subtract 1
                    # The print tells the user how many sig. digs. they should round to
                    # Calculations are done
                if min(list1) >= 1:
                    # If the smallest number within the list is greater or equal to 1 (e.x. 1.23)
                    # then this code continues to find sig. digs.
                    for i in str(min(list1)):
                        if i != ".":
                            count += 1
                    print("Round answer to", count, "significant digits. Thank you for using dilution calculator :) ")
                    # Since the smallest number is greater than 1, all digits counted are sig. digs.
                    # The print tells the user how many sig. digs. they should round to
                    # Calculations are done
            elif unitv == "mL":
                # If the user inputs 'mL' to the units of volume instead of 'L'
                # then the program converts the units, then solves
                v1 = v1 / 1000
                v2 = v2 / 1000
                # To convert mL, the volume values are to be divided by 1000 to get L
                print("V1 =", v1, "L ", "M2 =", m2, "L/mol ", "V2 =", v2, "L ", "M1 = ?")
                # prints the values converted with the units, showing the missing value
                solve = input("Solving for initial concentration.... ")
                m1 = (m2 * v2) / v1
                print("Therefore, M1 =", m1, "L/mol")
                list1 = [v1, m2, v2]
                count = 0
                if min(list1) < 1:
                    for i in str(min(list1)):
                        if i != ".":
                            count += 1
                    print("Round answer to", count - 1,
                          "significant digits. Thank you for using dilution calculator :) ")
                if min(list1) >= 1:
                    for i in str(min(list1)):
                        if i != ".":
                            count += 1
                    print("Round answer to", count, "significant digits. Thank you for using dilution calculator :) ")
    elif v1 == 0:
        # if the user does not have a value for V1 and had input 0, then this code continues to solve for V1
        unitm = input("Are your units for concentration L/mol? Yes or No. ")
        if unitm == "Yes":
            unitv = input("Are your units for concentration in L? If not what unit. ")
            if unitv == "Yes":
                print("M1 =", m1, "L/mol ", "v2 =", v2, "L ", "m2 =", m2, "L/mol ", "V1 = ?")
                solve = input("Solving for initial volume.... ")
                v1 = (m2 * v2) / m1
                # solves for v1, by using the rearranged equation of M1V1=M2V2
                print("Therefore, V1 =", v1, "L")
                list1 = [m1, m2, v2]
                count = 0
                if min(list1) < 1:
                    for i in str(min(list1)):
                        if i != ".":
                            count += 1
                    print("Round answer to", count - 1,
                          "significant digits. Thank you for using dilution calculator :) ")
                if min(list1) >= 1:
                    for i in str(min(list1)):
                        if i != ".":
                            count += 1
                    print("Round answer to", count, "significant digits. Thank you for using dilution calculator :) ")
            elif unitv == "mL":
                v2 = v2 / 1000
                # only one value given for volume, so only the given value will be converted
                print("M1 =", m1, "L/mol ", "v2 =", v2, "L ", "m2 =", m2, "L/mol ", "V1 = ?")
                solve = input("Solving for initial volume.... ")
                v1 = (m2 * v2) / m1
                print("Therefore, V1 =", v1, "L")
                list1 = [m1, m2, v2]
                count = 0
                if min(list1) < 1:
                    for i in str(min(list1)):
                        if i != ".":
                            count += 1
                    print("Round answer to", count - 1,
                          "significant digits. Thank you for using dilution calculator :) ")
                if min(list1) >= 1:
                    for i in str(min(list1)):
                        if i != ".":
                            count += 1
                    print("Round answer to", count, "significant digits. Thank you for using dilution calculator :) ")
    elif m2 == 0:
        # if the user does not have a value for M2 and had input 0, then this code continues to solve for M2
        unitm = input("Are your units for concentration L/mol? Yes or No. ")
        if unitm == "Yes":
            unitv = input("Are your units for concentration in L? If not what unit. ")
            if unitv == "Yes":
                print("M1 =", m1, "L/mol ", "V1 =", v1, "L ", "V2 =", v2, "L ", "M2 = ?")
                solve = input("Solving for final concentration.... ")
                m2 = (m1 * v1) / v2
                # solves for m2, by using the rearranged equation of M1V1=M2V2
                print("Therefore, M2 =", m2, "L/mol")
                list1 = [m1, v1, v2]
                count = 0
                if min(list1) < 1:
                    for i in str(min(list1)):
                        if i != ".":
                            count += 1
                    print("Round answer to", count - 1,
                          "significant digits. Thank you for using dilution calculator :) ")
                if min(list1) >= 1:
                    for i in str(min(list1)):
                        if i != ".":
                            count += 1
                    print("Round answer to", count, "significant digits. Thank you for using dilution calculator :) ")
            elif unitv == "mL":
                v1 = v1 / 1000
                v2 = v2 / 1000
                print("M1 =", m1, "L/mol ", "V1 =", v1, "L ", "V2 =", v2, "L ", "M2 = ?")
                solve = input("Solving for final concentration.... ")
                m2 = (m1 * v1) / v2
                print("Therefore, M2 =", m2, "L/mol")
                list1 = [m1, v1, v2]
                count = 0
                if min(list1) < 1:
                    for i in str(min(list1)):
                        if i != ".":
                            count += 1
                    print("Round answer to", count - 1,
                          "significant digits. Thank you for using dilution calculator :) ")
                if min(list1) >= 1:
                    for i in str(min(list1)):
                        if i != ".":
                            count += 1
                    print("Round answer to", count, "significant digits. Thank you for using dilution calculator :) ")
    elif v2 == 0:
        # if the user does not have a value for v2 and had input 0, then this code continues to solve for v2
        unitm = input("Are your units for concentration L/mol? Yes or No. ")
        if unitm == "Yes":
            unitv = input("Are your units for concentration in L? If not what unit. ")
            if unitv == "Yes":
                print("M1 =", m1, "L/mol ", "v1 =", v1, "L ", "m2 =", m2, "L/mol ", "V2 = ?")
                solve = input("Solving for final volume.... ")
                v2 = (m1 * v1) / m2
                # solves for v2, by using the rearranged equation of M1V1=M2V2
                print("Therefore, V2 =", v2, "L")
                list1 = [m1, v1, m2]
                count = 0
                if min(list1) < 1:
                    for i in str(min(list1)):
                        if i != ".":
                            count += 1
                    print("Round answer to", count - 1,
                          "significant digits. Thank you for using dilution calculator :) ")
                if min(list1) >= 1:
                    for i in str(min(list1)):
                        if i != ".":
                            count += 1
                    print("Round answer to", count, "significant digits. Thank you for using dilution calculator :) ")
            elif unitv == "mL":
                v1 = v1 / 1000
                print("M1 =", m1, "L/mol ", "v1 =", v1, "L ", "m2 =", m2, "L/mol ", "V2 = ?")
                solve = input("Solving for final volume.... ")
                v2 = (m1 * v1) / m2
                print("Therefore, V2 =", v2, "L")
                list1 = [m1, v1, m2]
                count = 0
                if min(list1) < 1:
                    for i in str(min(list1)):
                        if i != ".":
                            count += 1
                    print("Round answer to", count - 1,
                          "significant digits. Thank you for using dilution calculator :) ")
                if min(list1) >= 1:
                    for i in str(min(list1)):
                        if i != ".":
                            count += 1
                    print("Round answer to", count, "significant digits. Thank you for using dilution calculator :) ")
else:
    print("Calculator not applicable.")
