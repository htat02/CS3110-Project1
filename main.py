def is_valid_literal(input_string):

    #check for exponent
    if 'e' in input_string.lower():
        parts = input_string.lower().split('e')
        if len(parts) != 2:
            return "Invalid Literal"
        base, exponent = parts
        if (base.isdigit() or ('.' in base and all(c.isdigit() for c in base.replace('.', '', 1)))) and exponent.isdigit():
            return "Floating Point Literal"
            
    #decimal integer literal 
    if input_string[0] != '0' and all(c.isdigit() for c in input_string):
        return "Decimal Integer Literal"
    #octal integer literal 
    elif input_string[:2] == '0o' and all (c in '01234567' for c in input_string[2:]):
        return "Octal Integer Literal"
    #hexadecimal integer literal 
    elif input_string[:2] == '0x' and all((c.isdigit() or c.lower() in 'abcdef') for c in input_string[2:]):
        return "Hexadecimal Integer Literal" 
    
    else: 
        return "Invalid Literal"
    

input_string = input("Enter a string: ")
print(is_valid_literal(input_string))
