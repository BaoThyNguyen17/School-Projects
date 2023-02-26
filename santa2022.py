import csv, random, time
def create_list():
    array=["Sukhjit", "Garlvar", "Max", "Jacob", "Amrit", "Peter", "Toby", "Sanjot", "Thy", "Will", "Tzezzy"]
    #array of classmates 
    file=open("Secret_santa_candidates.csv", "w")
    csv_writer=csv.writer(file)
    csv_writer.writerow(array) #1d array so no need to use for i in loop
    file.close()
    #creates csv file of secret santa candidates and writes to it
def read_list():
    array=[]
    file=open("Secret_santa_candidates.csv")
    file_reader=csv.reader(file)
    for row in file_reader:
        array.append(row)
    array=array[0]
    return array
    #opens csv file and creates array (list of candidates) from it 
#create_list() - subroutine called initally to make csv file 
array=read_list()
#calls read_list and stores it in a local variable 
def secret_santa_draw(array):
    array_copy=[]
    #creates copy of candidate list to alter 
    secret_santa=[]
    for i in array:
        array_copy.append(i)
        #copies contents of array to array_copy
    for i in array:
        #i is the array item itself
        random_pick=random.randint(0,len(array_copy)-1)
        #creates a random integer from 0 to number of people in the secret santa array
        # len array -1 as its the index and 0 is the first element. len array would go out of array size
        pick=array_copy[random_pick]
        #number generated is used as the index to select a item from the array
        while pick == i:
            random_pick=random.randint(0,len(array_copy)-1)
            pick=array_copy[random_pick]
            #if the same person gifting=same person receiving, repeats until not same person 
        array_copy.pop(random_pick)
        #removes person from array 
        temp=[i,pick]
        #adds elements together to variable temp (gifter and receiver)
        secret_santa.append(temp)
        #adds it to the array of matches 

    return(secret_santa)
    #returns array of the matches 
def announcer(secret_santa):
    #outputs secret santa matches 
    for i in range(len(secret_santa)):
        string="Press enter for the next person "+secret_santa[i][0]
        #cannot place two inputs in print statement so placing it in string variable 
        input(string)
        #outputs string with a empty input (iput isn't stored in a variable)
        print(secret_santa[i][0], " is buying for: ", secret_santa[i][1])
        #prints gifter which is in column 0 and receiver which is in column 1
        time.sleep(3)
        print("\n"*10)
        #space between each output so end user cannot see match for previous end user 
def secret_santa_file():
    title=["gifter", "receiver"]
    #header 
    file=open("Santa_list.csv", "w", newline="")
    #creates csv file 
    #2d array so needs newline info 
    csv_writer=csv.writer(file)
    #so file contents can be written to csv
    csv_writer.writerow(title)
    #writes title to csv 
    for i in secret_santa:
        csv_writer.writerow(i)
        #writes array items to csv file so secret santa matches is stored 
    file.close()
array=read_list()
#calls subroutine to get array of classmates from secret santa candidates csv file 
secret_santa=secret_santa_draw(array)
#generates the secret santa matches 
secret_santa_file()
#writes the secret santa matches to another file 
announcer(secret_santa)
#outputs user's secret santa match (who they are buyng for) 