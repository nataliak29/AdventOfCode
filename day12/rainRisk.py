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
    try:
        manth_dist=abs(position["E"]-position["W"])+abs(position["N"]-position["S"])
    except:
        manth_dist=abs(position["E"])+abs(position["N"])
    return manth_dist

def ship_position_with_waypoint(data):

    s_position ={"N":0,"E":0}
    w_position ={"N":1,"E":10}

    for instr in data:
    
        action=instr[0]
        value=int(instr[1:])
        diff_n=w_position.get("N")-s_position.get("N")
        diff_e=w_position.get("E")-s_position.get("E")
        if action in ["N","E"]:
            w_position[action]=w_position.get(action)+value
        if action =="S":
            w_position["N"]=w_position.get("N")-value
        if action =="W":
            w_position["E"]=w_position.get("E")-value
        if action=="F":
            s_position["N"]=(w_position.get("N")-s_position.get("N"))*value+s_position["N"]
            s_position["E"]=(w_position.get("E")-s_position.get("E"))*value+s_position["E"]
            w_position["N"]=s_position["N"]+diff_n
            w_position["E"]=s_position["E"]+diff_e
        if instr=="R90" or instr=="L270":
            w_position["N"]=s_position["N"]-diff_e
            w_position["E"]=s_position["E"]+diff_n
        if instr=="R180" or instr=="L180":
            w_position["N"]=s_position["N"]-diff_n
            w_position["E"]=s_position["E"]-diff_e
        if instr=="R270"  or instr=="L90":
            w_position["N"]=s_position["N"]+diff_e
            w_position["E"]=s_position["E"]-diff_n
    return s_position
    


data=get_data("input.txt")
print("Part 1 answer:",manth_dist(ship_position(data)))
print("Part 2 answer:",manth_dist(ship_position_with_waypoint(data)))


