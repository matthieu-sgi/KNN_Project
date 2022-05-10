import csv
import random
import math
import numpy as np
# from matplotlib import testing

def ExtractFile(path) :
    with open(path,newline='') as file :
        global y,x
        filereader = csv.reader(file)
        filereader = [i[0].split(';') for i in list(filereader)]
        filereader = [list(map(float,i)) for i in filereader]
        y = np.array([i[-1] for i in filereader])
        x = np.array([i[:-1] for i in filereader])
        random.shuffle(filereader)
        return filereader


def KNN(dataset: list, data : list, accuracy=4 ) :
    distance = []
    # print(data)
    for ex in dataset :
        distance_temp = 0
        for i in range(len(data)-1):
            # print(ex[i])
            # print()
            distance_temp += (float(data[i])-float(ex[i]) )**2


        distance.append([ex[-1],distance_temp])
    distance.sort(key=lambda x: x[1], reverse=False)
    distance = distance[:accuracy:]
    # return distance
    sol = []
    for it_distance in distance :
        for it_temp in sol :
            if it_distance[0] in it_temp :
                it_temp[1] +=1
                break
        else :
            sol.append([it_distance[0],1])
    sol.sort(key=lambda x: x[1], reverse=False)
    return sol[0][0]


def Resultat(training_dataset : list,testing_dataset : list , accuracy=4):
    counter = 0

    for i in testing_dataset :
        
        temp = KNN(training_dataset,i,accuracy)
        if temp == i[-1 ]:
            counter += 1
        else :
            # print(temp, i)
            pass    

    return (counter * 100)/len(testing_dataset)










if __name__ == '__main__':

    dataset = ExtractFile("data.txt")
    # print(dataset)
    training_dataset = dataset[:int(len(dataset)*0.8)]
    testing_dataset = dataset[int(len(dataset)*0.8):]
    
    print(Resultat(training_dataset,testing_dataset,1))