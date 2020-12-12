#Instructions:https://adventofcode.com/2020/day/12
import os

def get_data(filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(folder, filename)
    data=[]

    with open(input_file, 'r') as filehandle:
        for line in filehandle:
            data.append( (line.rstrip()) )
    return data


def ship_position(data):
    position ={"N":0,"W":0,"S":0,"E":0}
    direction="E"
    directions =["E","S","W","N"]

    for instr in data:
        action=instr[0]
        value=int(instr[1:])
        if action=="F":
            position[direction]=position.get(direction)+value
        if action in ["N","W","S","E"]:
            position[action]=position.get(action)+value
        if action =="R":
            jump=int(value/90)
            next_direction_index=directions.index(direction)+jump
            if next_direction_index >= len(directions):
                next_direction_index=next_direction_index-len(directions)
            direction=directions[next_direction_index]
        if action =="L":
            jump=int(value/90)
            next_direction_index=directions.index(direction)-jump
            if next_direction_index >= len(directions):
                next_direction_index=next_direction_index-len(directions)
            direction=directions[next_direction_index]
    return position
        
def manth_dist(position):
    manth_dist=abs(position["E"]-position["W"])+abs(position["N"]-position["S"])
    return manth_dist


data=get_data("input.txt")
position=ship_position(data)
print("answer",position)
print(manth_dist(position))


