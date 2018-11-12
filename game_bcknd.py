from __future__ import division
import numpy as np
import time
import random
import math

def data_count(intrvl,time_total):
    return time_total/intrvl

def array_generator(intrvl,time_total):
    total_data_true = 100
    total_data_1 = int(total_data_true)
    total_data_0 = int((data_count(intrvl,time_total) - total_data_true))
    arr = []
    for x in range(total_data_1):
        arr.append(1)
    for x in range(total_data_0):
        arr.append(0)
    return arr

def randomizer(array_of_numbers):
    for i in range(len(array_of_numbers)):
        random.shuffle(array_of_numbers)
    return array_of_numbers

def meanAverage(valueOfArray):
    return sum(valueOfArray)/len(valueOfArray)

def standev(arrayValue):
    x = 0
    for value in arrayValue:
        value = (value - meanAverage(arrayValue))**2
        x =+ value
    return math.sqrt(x/(len(arrayValue)-1))

def start_game_timer():
    print("get ready!")
    time.sleep(1)
    print("get set!")
    time.sleep(1)
    print("GO!")
    time.sleep(1)
    return

def game_info(info):
    print("This game has intrvl number of", info[0] , "seconds")
    time.sleep(1)
    return

def loop_data_point(indctr):
    count_1 = 0
    count_0 = 0
    rand = randomizer(indctr[1])
    game_info(indctr)
    start_game_timer()
    for i in rand:
        print(i)
        if i == 1:
            count_1 += 1
        if i == 0:
            count_0 += 1
        # time.sleep(indctr[0])
    # activate time.sleep() to activate timer
    return count_1,count_0

def execute(var):
    print(var)
    return

# TASK : SCORING BACKEND, DATABASE, UI, IMPLEMENT THIS CODE TO A FRAMEWORK!


#Time definition
time_def = 900 #default

#Level Definition
level_1 = [5,array_generator(5,time_def)] #180 soal
level_2 = [4,array_generator(4,time_def)] #225 soal
level_3 = [3,array_generator(3,time_def)] #300 soal
level_4 = [2,array_generator(2,time_def)] #450 soal

# main command
start_game_lvl4 = loop_data_point(level_4)

# test standev of data
array_test = level_1[1]
rndmd_nmbr = randomizer(array_test)
result_data = standev(rndmd_nmbr)

execute(start_game_lvl4)
execute(result_data)