def validate_pswd(pswd):
    pswd_length = len(pswd)
    invalid_char_count = 0  #not in {0-9,a-z,A-Z,special_char}, password should be invalid in that case
    lower_case_count = 0
    upper_case_count = 0
    digit_count = 0
    special_char_count = 0
    flag = True            #for checking if any one of the conditions gets negated
    special_char = ['!','"','#','$','%','&','\'','(',')','*','+',',','-','.','/',':',';','<',
    '=','>','?','@','[','\\',']','^','_','`','{','|','}','~']

    for c in pswd:                    #counts individual types of character in the password
        if c in special_char:
            special_char_count+=1
        elif c>='0' and c<='9':
            digit_count+=1
        elif c>='a' and c<='z':
            lower_case_count+=1
        elif c>='A' and c<='Z':
            upper_case_count+=1
        else:
            invalid_char_count+=1

    if pswd_length<6 or pswd_length>16:   #conditions for checking if password is valid
        flag = False                      #flag is set to false, denoting condition violated
        print("Password should have min len 6 and max 16")
    if lower_case_count == 0:
        flag = False
        print("Password should contain atleast one lower case character (a-z)")
    if upper_case_count == 0:
        flag = False
        print("Password should contain atleast one upper case character (A-Z)")
    if digit_count == 0:
        flag = False
        print("Password should contain atleast one digit (0-9)")
    if invalid_char_count > 0:
        flag = False
        print("You have provided an invalid chracter")
    
    return "Valid Password" if flag else "Invalid Password"


pswd = input("Enter a password :\n")
print(validate_pswd(pswd))
    

