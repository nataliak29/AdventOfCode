import os

folder = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(folder, 'input.txt')
map_trees=[]
with open(input_file, 'r') as filehandle:
    for line in filehandle:
        map_trees.append(line.rstrip())


def update_map(map_trees):
    for i in range(len(map_trees)):
        if len(map_trees[i])< i*3:
            orig_length=len(map_trees[i])
            for j in range( len(map_trees[i]),i*3+1 ):
                map_trees[i]=map_trees[i]+map_trees[i][j-orig_length]
    return map_trees


def count_trees(updated_map):
    max_length=len(updated_map[-1:][0])
    tree_count=0
    i=0
    while i<=len(updated_map):
        i+=1
        if i*3>max_length:
            break
        if updated_map[i][i*3]=='#':
            tree_count+=1
    return  tree_count    



updated_map=update_map(map_trees)
print(updated_map)
print('Number of trees:',count_trees(updated_map))




    

