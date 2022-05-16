
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib import testing
import time

def ExtractFile(path) :
    with open(path,newline='') as file :
        # global y,x
        filereader = np.genfromtxt(file,delimiter=';')

        np.random.shuffle(filereader)
        if len(filereader[0]) == 11 :
            x = np.array([i[:-1] for i in filereader])
            y = np.array([i[-1] for i in filereader])
        else:
            x = np.array([i for i in filereader])
            y = 0
        return x,y


def KNN(x : np.array,y:np.array, data : np.array, accuracy=4 ) :
    
    distance = np.zeros(len(x))

    
        
        
    distance = np.sum((x - data)**2,axis=1)
        
    
    keys = np.argsort(distance)
    # temp_x = np.take(x,keys)
    distance = np.take(distance,keys)
    temp_y = np.take(y,keys)
    temp_y = temp_y[:accuracy]
    distance = distance[:accuracy]
    
    
    
    # print(sum(temp_y)/accuracy)
    return 0 if (sum(temp_y)/accuracy)<=0.5 else 1

def Writing(training_dataset :np.array ,dataset:np.array,accuracy=4) :
    with open('result.txt','w') as file :
        # file.write('id;label\n')
        for i in range(len(dataset[0])) :
            temp = KNN(training_dataset[0],training_dataset[1],dataset[0][i],accuracy)
            file.write(str(temp)+'\n')
    


def Resultat(training_dataset : tuple,test_dataset :tuple , accuracy=4):
    counter = 0
    
    
    for i in range(len(test_dataset[0])) :
        # print('ici')
        temp = KNN(training_dataset[0],training_dataset[1],test_dataset[0][i],accuracy)
        # print(test_dataset[i][1])
        if temp == test_dataset[1][i] :
            counter += 1
            

    return (counter * 100)/len(test_dataset[0])










if __name__ == '__main__':

    # chronometer
    start_time = time.time()
    training_dataset_1 = ExtractFile('data.txt')
    training_dataset_2 = ExtractFile('preTest.txt')
    training_dataset = [np.concatenate((training_dataset_1[0],training_dataset_2[0]),axis=0),np.concatenate((training_dataset_1[1],training_dataset_2[1]),axis=0)]
    
    dataset = ExtractFile('finalTest.txt')
    Writing(training_dataset,dataset,20)
    stop_time = time.time()
    print('Finished !!')
    print('Temps d\'execution : ',stop_time - start_time,'s',sep='')
    # print(dataset)
    # print(type(dataset[0]))

    # print(Resultat(dataset,0.8,40))
    
    #test all accuracy values 20 times, then make a graph
    ########################### Finding the best accuracy (k) value ###############################
    # dataset = ExtractFile("data.txt")
    # testing_dataset = ExtractFile("preTest.txt")
    # accuracy = [i for i in range(1,100)]
    # result = np.zeros(len(accuracy))



    # for i in range(len(accuracy)) :
    #     result[i] = Resultat(dataset,testing_dataset,i+1)
        
    
    # print('end')

    
    # print()
    # plt.plot(accuracy,result)
    # key = np.argsort(result)
    # result = np.take(result,key)
    # accuracy = np.take(accuracy,key)
    # print("result : ",result[-1])
    # print("accuracy : ",accuracy[-1])
    # plt.show()
    ################################################################################################





    
        
