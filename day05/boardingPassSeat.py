import os
import math 

def get_data(filename):
    folder = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(folder, filename)
    data=[]
    with open(input_file, 'r') as filehandle:
        for line in filehandle:
            data.append(line.rstrip())
    return data

def seat_row(entry):    
    min_row=0
    max_row=127
    entry_segment=entry[:7]
    for i in range(len(entry_segment)):
        if entry_segment[i]=='F':
            max_row=round((max_row - min_row+1)/2 + min_row-1,0)
        if entry_segment[i]=='B':
            min_row=round((max_row - min_row+1)/2 + min_row,0)
        row=int(round(min_row,0))

    return row

def seat_column(entry):    
    min_column=0
    max_column=7
    column=0
    entry_segment=entry[7:]
    for i in range(len(entry_segment)):
        if entry_segment[i]=='R':
            min_column=round((max_column - min_column+1)/2 + min_column ,0)
        if entry_segment[i]=='L':
            max_column=round((max_column- min_column+1)/2 + min_column -1,0)
        column=int(round(min_column,0))

    return column

def run_tests():
    data=get_data('test.txt')
    test_row=[44,70,14,102]
    test_column=[5,7,7,4]
    test_seat_id=[357,567,119,820]
    for i in range(len(data)):
        entry=data[i]
        row=seat_row(entry)
        column=seat_column(entry)
        seat_id=row*8+column
        print(row, column)
        if row==test_row[i] and column==test_column[i] and seat_id==test_seat_id[i]:
            print("Test passed for", entry)
        else:
            print("Test failed for", entry)


def max_seat_id(filename):

    data=get_data(filename)
    max_seat_id=0
    for i in range(len(data)):
        entry=data[i]
        row=seat_row(entry)
        column=seat_column(entry)
        seat_id=row*8+column
        if seat_id>max_seat_id:
            max_seat_id=seat_id
            
    return max_seat_id


run_tests()
print("Max seat id is:",max_seat_id("input.txt"))

