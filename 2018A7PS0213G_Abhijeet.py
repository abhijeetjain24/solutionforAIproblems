from matplotlib import pyplot as plt
import random
print("AI assignment ID:2018A7PS0213G Abhijeet Jain")
print("Enter 1 for 8 queens problem")
print("Enter 2 for TSP problem")
choice=input()

if choice=="1":
    #algo1
    #calculation of fitness value
    def fitness(arr):
        out=29
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if (abs(arr[i]-arr[j])==abs(i-j)):
                    out-=1
                elif(arr[i]==arr[j]):
                    out-=1  
        return out
    #reproduce function optimized where we have taken both combination 
    # and returned the one with higher fitness    
    def reproduce(x,y):
        z = random.randint(1,8)
        out1=y[0:z]+x[z:]
        out2 =x[0:z] + y[z:]
        t1=fitness(out1)
        t2=fitness(out2)
        if t1>t2:
            return out1
        else:
            return out2
    #stochastically selecting a state from the population
    def random_selection(population,fitness_score):
        out_state = random.choices(population,fitness_score)[0]
        return out_state
    #defining the population and other output variables
    fitness_score=[]
    population = []
    for i in range(70):
        temp=[]
        t1=[]
        for j in range(8):
            temp.append(1)   
        population.append(temp)
        t1=fitness(temp)
        fitness_score.append(t1)

    mut_prob=0.95#maintaing orignal mut probality since we are tampering with mut_prob during the algo
    mut_prob1=0.95
    final_fitness=0#max fitness found during all iteration
    cnt=0#total iteration occured
    best_fit=[]
    max_side_step=29 #max no. of iteration for which max fitness value remains constant
    finaloutfit=[]#best possible solution found out
    #running this for 500 iteration and breaking the loop whenever the value of 
    # fitness reaches 29 else printing the output with 
    # best fitness value found in these 500 iteration
    for ij in range(500):
        new1=[]
        newfit=[]
        flg=0
        #cheking  sideways  so as to see if fitness values are constant after certain iteration
        for j in range(len(population) ):
            n = len(best_fit) 
            if n>max_side_step:
                flag=0
                for i in range(n-max_side_step,n-1):
                    if best_fit[i]!=best_fit[i+1]:
                        flag=1
                        break
                if flag==0:
                    mut_prob = 0
            #using random selection to select suitable candidates for creating new state
            temp=random_selection(population,fitness_score)
            t12=random_selection(population,fitness_score)
            #creating a new state and causing a mutation
            #in it with small probablity
            t123=reproduce(temp,t12)
            if random.uniform(0,1)>=mut_prob:
                t5=random.randint(0,7)
                mut2 = random.randint(1,8)
                while(mut2==t123[t5]):
                    mut2 = random.randint(1,8)
                t123[t5]=mut2
            t6=fitness(t123)    
            newfit.append(t6)
            new1.append(t123)
            if final_fitness<t6:#calculating the current max fitness and maintaing the current best solution
                finaloutfit=t123
                final_fitness=t6
            if final_fitness==29:#checking if fitness of mutated array is 29 i.e. the sol or not 
                flg=1
                break
        population=new1
        fitness_score=newfit
        best_fit.append(max(fitness_score))
        mut_prob=mut_prob1
        if flg==1:
            break
        cnt+=1
    print(cnt)
    print(final_fitness)
    print(finaloutfit)
    plt.plot(best_fit)
    plt.show()
elif choice=="2":
#algo 2
    map = [[0,1000,1000,1000,1000,1000,0.15,1000,1000,0.2,1000,0.12,1000,1000],
        [1000,0,1000,1000,1000,1000,1000,0.19,0.4,1000,1000,1000,1000,0.13],
        [1000,1000,0,0.6,0.22,0.4,1000,1000,0.2,1000,1000,1000,1000,1000],
        [1000,1000,0.6,0,1000,0.21,1000,1000,1000,1000,0.3,1000,1000,1000],
        [1000,1000,0.22,1000,0,1000,1000,1000,0.18,1000,1000,1000,1000,1000],
        [1000,1000,0.4,0.21,1000,0,1000,1000,1000,1000,0.37,0.6,0.26,0.9],
        [0.15,1000,1000,1000,1000,1000,0,1000,1000,1000,0.55,0.18,1000,1000],
        [1000,0.19,1000,1000,1000,1000,1000,0,1000,0.56,1000,1000,1000,0.17],
        [1000,0.4,0.2,1000,0.18,1000,1000,1000,0,1000,1000,1000,1000,0.6],
        [0.2,1000,1000,1000,1000,1000,1000,0.56,1000,0,1000,0.16,1000,0.5],
        [1000,1000,1000,0.3,1000,0.37,0.55,1000,1000,1000,0,1000,0.24,1000],
        [0.12,1000,1000,1000,1000,0.6,0.18,1000,1000,0.16,1000,0,0.4,1000],
        [1000,1000,1000,1000,1000,0.26,1000,1000,1000,1000,0.24,0.4,0,1000],
        [1000,0.13,1000,1000,1000,0.9,1000,0.17,0.6,0.5,1000,1000,1000,0]]
        #map is the matrix that represents distance between any two cities pairwise
        #where we have considered infinite distance as 1000
     #calculation of fitness value
    def fitness(arr):
        out=0
        for i in range(len(arr)-1):
            out+=map[arr[i]][arr[i+1]]
        out+=map[arr[len(arr)-1]][arr[0]]
        return 1/out  
    
    def reproduce(x,y):
        a = random.randint(0,13)
        b= random.randint(0,13)
        c=min(a,b)
        d=max(a,b)+1
        k=0
        new1=[]
        for i in range(14):
            new1.append(-1)
        for i in range(c,d):
            new1[i]=x[i]
        for i in range(0,14):
            if(y[i] not in new1):
                if new1[k]!=-1:
                    while new1[k]!=-1:
                        k+=1
                new1[k]=y[i]
                k+=1
        return new1
    #stochastically selecting a state from the population
    def random_selection(population,fitness_score):
        out_state = random.choices(population,fitness_score)[0]
        return out_state
    #defining the population and other output variables
    fitness_score=[]
    population = []
    for i in range(50):
        temp=[]
        t1=[]
        for j in range(14):
            temp.append(j)   
        population.append(temp)
        t1=fitness(temp)
        fitness_score.append(t1)

    #main algo naive

    mut_prob=0.98
    final_fitness=0#final max fitness calculated after all iteration
    maxfit_gen=0#varaiable to get maxfitness of population in each generation
    max_fit=[]
    best_fit=[]#best fitness of each iteration
    #loop to run the algo for 500 generations
    for i in range(500):
        maxfit_gen=0
        new1=[]
        newfit=[]
        
        for j in range(len(population) ):
            temp=random_selection(population,fitness_score)
            t12=random_selection(population,fitness_score)
             #creating a new state and causing a mutation
            #in it with small probablity
            t123=reproduce(temp,t12)
            flg12=0#it represents whether to use modified mutate function or not
            disposed=[] #to know which states we have already 
                        #used while finding the state having no adjacent roads
            city1=-1#the two cities to be find out where city1 is the city with no adjacent roads
            city2=-1#city2 is the state which has both adjacent road
            for k in range(1,len(t123)-1): #loop to find out city with no adjacent roads
                if map[t123[k]][t123[k+1]]==1000 and map[t123[k]][t123[k-1]]==1000:
                    city1=k
                    disposed.append(t123[k])
                    disposed.append(t123[k-1])
                    disposed.append(t123[k+1])
                    flg12=1
                    break

            if map[t123[0]][t123[1]]==1000 and map[t123[0]][t123[len(t123)-1] ]==1000 and flg12==0:
                    city1=0
                    disposed.append(t123[0])
                    disposed.append(t123[len(t123)-1])
                    disposed.append(t123[1])
                    flg12=1
            if map[t123[len(t123)-1]][t123[0]]==1000 and map[t123[len(t123)-1]][t123 [len(t123)-2] ]==1000 and flg12==0:
                    city1=len(t123)-1
                    disposed.append(t123[0])
                    disposed.append(t123[len(t123)-1])
                    disposed.append(t123[len(t123)-2])
                    flg12=1 
            flg1234=0
            for k in range(1,len(t123)-1):
                if t123[k] not in disposed:
                    if map[t123[k]][t123[k+1]]!=1000 and map[t123[k]][t123[k-1]]!=1000:
                        city2=k
                        flg1234=1
                        break
            if t123[0] not in disposed:        
                if map[t123[0]][t123[1]]!=1000 and map[t123[0]][t123[len(t123)-1] ]!=1000 and flg1234==0:
                    city2=0
                    flg1234=1
            if t123[len(t123)-1] not in disposed:       
                if map[t123[len(t123)-1]][t123[0]]==1000 and map[t123[len(t123)-1]][t123 [len(t123)-2] ]==1000 and flg1234==0:
                    city2=len(t123)-1
                    flg1234=1
            #standard mutaing when one of the city1 or city2 is not found
            if (flg12==0 or flg1234==0):
                if random.uniform(0,1)>=mut_prob:
                    t5=random.randint(0,13)
                    mut2 = random.randint(0,13)
                    while(mut2==t5):
                        mut2 = random.randint(0,13)
                    swap1=t123[t5]
                    t123[t5]=t123[mut2]
                    t123[mut2]=swap1    
            else:
                  if random.uniform(0,1)>=mut_prob: #this is the optimized mutaion,here we are swapping two 
                    swap1=t123[city1]               # cities in the permutation in such a way that a city 
                    t123[city1]=t123[city2]         # which is not connected with its neighbours in the permutation 
                    t123[city2]=swap1               # is removed and a new city is swapped with its position
                                                    # which has increased the chances of having lesser disconnected cities

            t6=fitness(t123)    
            newfit.append(t6)
            new1.append(t123)
            final_fitness=max(final_fitness,t6)
            if t6>maxfit_gen :
                maxfit_gen=t6
                max_fit=t123

        population=new1
        fitness_score=newfit
        best_fit.append(max(fitness_score))

    print(max_fit)
    print(1/maxfit_gen)
    print(1/final_fitness)
    plt.plot(best_fit)
    plt.show()


