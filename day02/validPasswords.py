import os
import numpy as np

folder = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(folder, 'input.txt')
data = np.loadtxt(input_file, dtype=str)

def is_password_valid(password,policy_letter,min_frq,max_frq):
    policy_letter_count=0
    for j in range(len(password)):
        if password[j:j+1]==policy_letter:
            policy_letter_count+=1
        else: 
            continue
    if policy_letter_count<=max_frq and policy_letter_count>=min_frq:
        return 1
    else:
        return 0


def valid_passwords(input_data):
    valid_pass_count=0 
    for i in range(len(input_data)):
        min_frq=int(input_data[i][0].split('-')[0])
        max_frq=int(input_data[i][0].split('-')[1])
        policy_letter=input_data[i][1][:1]
        password = input_data[i][2]
        valid_pass_count+=is_password_valid(password,policy_letter,min_frq,max_frq)
        print("Processing",input_data[i])
        print("Is password valid (1/0):",is_password_valid(password,policy_letter,min_frq,max_frq))
            
    print("Total number of valid passwords",valid_pass_count)



valid_passwords(data)