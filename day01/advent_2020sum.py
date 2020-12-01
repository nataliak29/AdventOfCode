import os
import numpy as np

folder = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(folder, 'test.txt')
data = np.loadtxt(input_file, dtype=int)

  
def sum_of_two(input_data, target_int): 
    for i in range(len(input_data)):
        for j in range(len(input_data)):
            if input_data[i]+input_data[j] == target_int:
                print("Numbers are ", input_data[i],input_data[j])
                print("Answer for 2 number sum is", input_data[i]*input_data[j])
                break
        

def sum_of_three(input_data, target_int): 
    for i in range(len(input_data)):
        for j in range(len(input_data)):
            for k in range(len(input_data)):
                if input_data[i]+input_data[j]+ input_data[k] == target_int:
                    print("Numbers are ", input_data[i],input_data[j],input_data[k] )
                    print("Answer for 3 number sum is", input_data[i]*input_data[j]*input_data[k] )
                    break
            

sum_of_two(data,2020)
sum_of_three(data,2020)
    