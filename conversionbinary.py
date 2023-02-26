#_______________________#
#Functions
import random
import time #to record the amount of time user takes for each question

def den_to_bin(denary):
    binary = ""
    for i in range(7,-1,-1):
        if denary >= 2**i:
            denary -= 2**i
            binary+= "1"
        else:
            binary+="0"
    return binary
def bin_to_den(binary):
    n, denary = 1, 0
    for i in range(len(binary)):
        if binary[(len(binary)-1)-i] == "1":
            denary+=n
        n*=2
    return denary
def den_to_hex(denary):
    bin = den_to_bin(denary)
    den1 = bin_to_den(bin[0:4])
    den2 = bin_to_den(bin[4:8])
    array=["A", "B", "C", "D", "E", "F"]
    if den1 > 9:
        hex1 = array[den1-10]
    else:
        hex1 = den1
    if den2 > 9:
        hex2 = array[den2-10]
    else: 
        hex2 = den2
    return str(hex1)+str(hex2)
def bin_to_hex(binary):
    den = bin_to_den(binary)
    return den_to_hex(den)
def hex_to_bin(hexadecimal):
    den1, den2 = 0, 0
    array=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    for i in range(len(array)):
        if hexadecimal[0:1] == array[i]:
            den1 = i
        if hexadecimal[1:2] == array[i]:
            den2 = i
        if den1 > 0 and den2 > 0:
            break
    if den_to_bin(den2)=="0000":
        return den_to_bin(den1)
    return den_to_bin(den1)+den_to_bin(den2) 
def hex_to_den(hexadecimal):
    binary = str(hex_to_bin(hexadecimal))
    return bin_to_den(binary)

#_____________________#
#Menu
score = 0
revise=input("""What would you like to revise?
1. Hexadecimal - Binary
2. Hexadecimal - Denary 
3. Denary - Binary
4. Denary - Hexadecimal 
5. Binary - Denary 
6. Binary - Hexadecimal\n""").lower()

#_________________#
#10 Questions 
for i in range(10):
    num=random.randint(1,255)
    if revise == "1":
        bin = den_to_bin(num)
        hex = bin_to_hex(bin)
        print("Convert Hexademical", hex, "to Binary\n")
        answer = bin
    if revise =="2":
        bin = den_to_bin(num)
        hex = bin_to_hex(bin)
        print("Convert Hexademical", hex, "to Denary\n")
        answer = num
    if revise =="3":
        print("Convert Denary", num, "to Binary\n")
        answer = den_to_bin(num)
    if revise =="4":
        print("Convert Denary", num, "to Hexadecimal\n")
        bin = den_to_bin(num)
        answer = bin_to_hex(bin)
    if revise =="5":
        bin = den_to_bin(num)
        print("Convert Binary", bin, "to Denary\n")
        answer = num
    if revise =="6":
        bin = den_to_bin(num)
        print("Convert Binary", bin, "to Hexadecimal\n")
        answer = bin_to_hex(bin)
    timer_start=time.time()
    input_answer=input("Answer: ")
    timer_end=time.time()
    if input_answer == str(answer):
        print("Correct! \n")
        score+=10 / (timer_end-timer_start)
        score=round(score,2)
        print("Current score: ", score)
    else:
        print("Incorrect, answer was ", answer,"\n")
print(score)

#___________________________________________#
#Score system
scoreboard=open(str(revise)+"scoreboard.txt", "a")
scoreboard.write(str(score))
scoreboard.close()
#------------------------------------------#
#Sorting Score
scoreboard=open(str(revise)+"scoreboard.txt", "r")
array=[]
for line in scoreboard:
    array.append(line.strip())
for i in range(len(array)):
    array[i]=int(array[i])
sorted_array = sorted(array, reverse = True)
revise_array=["", "Hexadecimal - Binary", "Hexadecimal - Denary", "Denary - Binary", "Denary - Hexadecimal",
"Binary - Denary", "Binary - Hexadecimal"]
print(revise_array[int(revise)] + " Top 10 Scoreboard\n-------------------\n")
if len(sorted_array)<10:
    for i in range(len(sorted_array)):
        print(sorted_array[i])
else:
    for i in range(10):
        print(sorted_array[i])