
import numpy as np
import matplotlib.pyplot as plt
# from matplotlib import testing

def ExtractFile(path) :
    with open(path,newline='') as file :
        # global y,x
        filereader = np.genfromtxt(file,delimiter=';')

        np.random.shuffle(filereader)
        
        x = np.array([i[:-1] for i in filereader])
        y = np.array([i[-1] for i in filereader])
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

    # print(Resultat(dataset,0.8,40))
    
    #test all accuracy values 20 times, then make a graph
    
    accuracy = [i for i in range(1,50)]
    result = np.zeros(len(accuracy))
    for i in range(20) :
        result_temp= np.zeros(len(accuracy))

        for i in range(len(accuracy)) :
            result_temp[i] = Resultat(dataset,0.8,i+1)
        
        print('end')
        if i == 0 :
            result = result_temp
        else :
            result = (result + result_temp)/2
    
    print()
    plt.plot(accuracy,result)
    key = np.argsort(result)
    result = np.take(result,key)
    accuracy = np.take(accuracy,key)
    plt.show()

    print("result : ",result[-1])
    print("accuracy : ",accuracy[-1])



    
        
