#Challenge 1 Booking Options
#Add a menu system to your code with 4 options
#Challenge #2 Saving the bookings in a CSV file 
import csv
"""with open('seats.csv',mode="w",newline='') as seats_file:
    seats_writer=csv.writer(seats_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    seats_writer.writerow([0,0,1,1,0,1,1,1])
    seats_writer.writerow([0,1,1,0,0,1,0,1])
    seats_writer.writerow([1,0,0,1,0,1,1,0])
    seats_writer.writerow([0,1,1,1,0,0,0,1])
    seats_writer.writerow([0,0,1,1,0,1,0,0])
    seats_writer.writerow([1,0,1,1,0,0,1,1])"""
seats_file=open("seats.csv","r")
seats_array=[]
for line in seats_file:
    seats_array.append(line.strip().split(","))
seats_file.close()
print(seats_array)

left=0
for row in range(0,6):
    for column in range(0,8):
        if seats_array[row][column]=="0":
            left+=1
#Challenge #4 Improvements
if left!=0:
    print("There are", left,"seats left")
else:
    print("The theatre is full - all seats have been booked")
def multiplebookings(array,number,row,column): #Challenge #4 Improvements
    available=[]
    tempnumber=int(number)
    if column>0:
        for i in range(1,column):
            if array[row][column-i]=="0":
                temp=str(row)+","+str(column-i)
                available.append(temp.split(","))
                tempnumber-=1
            if tempnumber==0 or array[row][column-i]!="0":
               break
        if tempnumber!=0:
            for i in range(1,column):
                if array[row][column+i]=="0":
                    temp=str(row)+","+str(column+i)
                    available.append(temp.split(","))
                    tempnumber-=1
                if tempnumber==0 or array[row][column+i]!="0":
                    break
    else:
        for i in range(1,7):
            if array[row][column+i]=="0":
                temp=str(row)+","+str(column+i)
                available.append(temp.split(","))
                tempnumber-=1
            if tempnumber==0 or array[row][column+i]!="0":
                break
    if tempnumber==0:
        print("These available seats are next to your seat of row", row,", column",column)
        for i in range(len(available)):
            print("row",row," column:",available[i][1])
            tempcolumn=int(available[i][1])
            array[row][tempcolumn]=1
        print("They have been now booked")
    else:
        print("Not enough seats available to book", number, "consecutive seats in row", row)
    return array
def booksystem(seats_array):
    print("""
1. Book a seat by row/column
2. Book a seat close to the front
3. Book a seat close to the back
4. Reset all seats to 0
5. Cancel a booking
X. Exit
Enter the number of the option you would like to do or enter X to exit""")
    book_options=str(input("How would you like to book?"))
    if book_options=="1":
        number=int(input("How many bookings would you like to make?"))
        book_row=int(input("Enter the seat row from 0 to 5:"))
        book_column=int(input("enter the seat column from 0 to 7:"))
        #Challenge #4 Improvements
        if book_row<=5 and book_row>=0 and book_column<=7 and book_column>=0:
            if seats_array[book_row][book_column]!=1:
                seats_array[book_row][book_column]=1
                print("Seat available, it has been booked")
            else:
                print("seat unavailable, please choose another")
                while seats_array[book_row][book_column]==1:
                    book_row=int(input("Enter the seat row:"))
                    book_column=int(input("enter the seat column:"))
                    if seats_array[book_row][book_column]!=1:
                        seats_array[book_row][book_column]=1
                        print("Seat available, it has been booked")
        else:
            print("invalid seat row/column")
        if number>1:
            seats_array=multiplebookings(seats_array,number,book_row,book_column)
                
    elif book_options=="2":
        book=False
        number=int(input("How many bookings would you like to make?"))
        for row in range(0,6):
            for column in range(0,8):
                while book!=True:
                    if seats_array[row][column]!=1:
                        print("First seat available closest to the front is in row",row,", column",column)
                        seats_array[row][column]=1
                        print("Seat has been booked")
                        book=True
        if number>1:
            seats_array=multiplebookings(seats_array,number,row,column)
    elif book_options=="3":
        book=False
        number=int(input("How many bookings would you like to make?"))
        for row in range(0,6):
            for column in range(0,8):
                while book!=True:
                    if seats_array[-row][-column]!=1:
                        print("First seat closest to the back is in row",6-row,",column",8-column)
                        seats_array[-row][-column]=1
                        endrow=6-row
                        endcolumn=8-column
                        print("Seat has been booked")
                        book=True
        if number>1:
            seats_array=multiplebookings(seats_array,number,endrow,endcolumn)
      
    elif book_options=="4":
        #Challenge #3 Resetting the array
        y_n=input("Would you like to reset all seats to 0 (unbooked)? \n y/n").lower()
        if y_n=="y":
            for row in range(0,6):
                for column in range(0,8):
                    seats_array[row][column]=0
        print(seats_array)
        print("seats have been resetted")
    elif book_options=="5":
        #Challenge #4 Improvements
        cancel=input("which booking would you like to cancel?")
        book_row=int(input("Enter the seat row between 0-5:"))
        book_column=int(input("enter the seat column 0-7:"))
        #Challenge #4 Improvements
        if book_row<=5 and book_row>=0 and book_column<=7 and book_column>=0:
            if seats_array[book_row][book_column]==1:
                seats_array[book_row][book_column]=0
                print("That seat book has been cancelled")
            else:
                print("That seat is not booked")
        else:
            print("invalid")
    else:
        print("Exited")
    return seats_array
    
#Challenge #4 Improvements
password="password123"
authorise=input("Enter the password for the system to confirm you're a staff")
if authorise==password:
    print("authorised")
    seats_array=booksystem(seats_array)
else:
    print("incorrect, access to the booking system denied")

line=""
#Challenge #2 Saving the bookings in a CSV file 
if seats_array!=[]:
    for row in range(0,5):
        for column in range(0,7):
            line+=str(seats_array[row][column])+","
        line+=str(seats_array[row][7])
        line+="\n"
    for i in range(0,7):
        line+=(str(seats_array[5][i])+",")
    line+=str(seats_array[5][7])
seats_file=open("seats.csv","w")
seats_file.write(line)
seats_file.close()
seats_file=open("seats.csv","r")
print("\n current seats status")
for i in seats_file:
    print(i)
       
       
