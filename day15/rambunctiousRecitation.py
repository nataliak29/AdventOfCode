#Instructions:https://adventofcode.com/2020/day/15

def create_dict(data):
    last_occur={}
    for i,item in enumerate(data[:-1]):
        last_occur[item]=i+1

    return last_occur



def nth_number(data,n):
    last_occur=create_dict(data)
    next_num=data[-1]
    next_num_order=len(data)
       

    while next_num_order<n:
        prev_indx=last_occur.get(next_num)
        if prev_indx == None:
            last_occur[next_num]=next_num_order
            next_num=0
            
        else:
            indx_diff=next_num_order-prev_indx
            last_occur[next_num]=next_num_order
            next_num=indx_diff

        next_num_order+=1
    return next_num



data=[0,3,6]

print("Test answer - 2020th number:",nth_number(data,2020))
print("Test answer - 30000000th number:",nth_number(data,30000000))


data=[0,8,15,2,12,1,4]

print("Test answer - 2020th number:",nth_number(data,2020))
print("Test answer - 30000000th number:",nth_number(data,30000000))