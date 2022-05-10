import csv
import random
import numpy as np
# from matplotlib import testing

def ExtractFile(path) :
    with open(path,newline='') as file :
        # global y,x
        filereader = csv.reader(file)
        filereader = [i[0].split(';') for i in list(filereader)]
        filereader = [list(map(float,i)) for i in filereader]
        random.shuffle(filereader)
        x = np.array([i[:-1] for i in filereader])
        y = np.array([i[-1] for i in filereader])
        return x,y


def KNN(x : np.array,y:np.array, data : np.array, accuracy=4 ) :
    
    distance = np.zeros(len(x))

    for i in range(len(x)) :
        temp = (np.sum((x[i] - data)**2)) 
        if temp != 0 :
            distance[i] = 1/temp
        else : 
            distance[i] = 100000000000000000000
    
    keys = np.argsort(distance)
    # temp_x = np.take(x,keys)
    distance = np.take(distance,keys)
    temp_y = np.take(y,keys)
    temp_y = temp_y[-accuracy:]
    distance = distance[-accuracy:]
    
    
    
    # print(sum(temp_y)/accuracy)
    return 0 if (sum(temp_y)/accuracy)<0.5 else 1


def Resultat(dataset : tuple,prop_test :float , accuracy=4):
    counter = 0
    training_dataset = [dataset[0][:int(prop_test*len(dataset[0]))],dataset[1][:int(prop_test*len(dataset[0]))]]
    test_dataset = [dataset[0][int(prop_test*len(dataset[0])):],dataset[1][int(prop_test*len(dataset[0])):]]
    
    for i in range(len(test_dataset[0])) :
        # print('ici')
        temp = KNN(training_dataset[0],training_dataset[1],test_dataset[0][i],accuracy)
        # print(test_dataset[i][1])
        if temp == test_dataset[1][i] :
            counter += 1
            

    return (counter * 100)/len(test_dataset[0])










if __name__ == '__main__':

    dataset = ExtractFile("data.txt")
    # print(dataset)
    # print(type(dataset[0]))

    print(Resultat(dataset,0.5,10))