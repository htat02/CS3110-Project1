def is_valid_literal(input_string):

    #decimal integer literal 
    if input_string[0] != '0' and all(c.isdigit() for c in input_string):
        return "Decimal Integer Literal"
    
    else: 
        return "Invalid Literal"
    

input_string = input("Enter a string: ")
print(is_valid_literal(input_string))
