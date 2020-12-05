#Instructions:https://adventofcode.com/2020/day/3

import os

def get_data(filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(folder, filename)
    map_trees=[]
    with open(input_file, 'r') as filehandle:
        for line in filehandle:
            map_trees.append(line.rstrip())
    return map_trees



def count_trees(map_trees,right_shift,down_shift):
    pos=0
    x=0
    count=0
    line_length=len(map_trees[0])
    while x<len(map_trees):
        x+=down_shift
        if x>=len(map_trees):
            break
        pos=right_shift+pos
        
        if pos>=line_length:
            pos=pos-line_length

        if map_trees[x][pos]=="#":
           count+=1
    return count



def tests():
    test_sets=[[1,1],[3,1],[5,1],[7,1],[1,2]]
    test_answers=[2,7,3,4,2]

    for i in range(len(test_sets)):
        map_trees=get_data('test.txt')
        right_shift=test_sets[i][0]
        down_shift=test_sets[i][1]
        if count_trees(map_trees,right_shift,down_shift)== test_answers[i]:
            print("Test",right_shift,",",down_shift,"Passed")
        else:
            print("Test",right_shift,",",down_shift,"Failed")
    


tests()


sets=[[1,1],[3,1],[5,1],[7,1],[1,2]]
trees_count=1
for i in range(len(sets)):
    map_trees=get_data('input.txt')
    right_shift=sets[i][0]
    down_shift=sets[i][1]
    print(count_trees(map_trees,right_shift,down_shift))
    trees_count=trees_count*count_trees(map_trees,right_shift,down_shift)

print("Product of all trees_count",trees_count)








    

