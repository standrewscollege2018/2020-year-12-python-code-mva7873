#traval plan

#lists of citys costs and flights


take_off = [["1  Auckland","$",0], ["2  Wellington",'$',50], ["3  Christchurch","$",75]]
destination = [["1  Sydney","$",326,"$",120], ["2  Tonga","$",378,"$",40], ["3  Shanghai","$",1436,"$",60], ["4  London","$",2376,"$",80]]

#total cost for flights and accomodation
acom_costs = (0)
Traval_costs = (0)
#start of while loops
take_off_slection=True
print("Please enter the city that you are departing from")
print("Please note that depending on where you depart from there may be additional costs incurred")
# fun way to make lists print across page
(print(take_off[0][0],end = ' '), print(take_off[0][1],end = ' '), print(take_off[0][2]))
(print(take_off[1][0],end = ' '), print(take_off[1][1],end = ' '), print(take_off[1][2]))
(print(take_off[2][0],end = ' '), print(take_off[2][1],end = ' '), print(take_off[2][2]))

while take_off_slection == True:
    take_off_choice = int(input("enter the corresponding number of the city you wish to leave from: "))
    if take_off_choice == (1):
        Traval_costs = Traval_costs + 0
        print("continue with your selection")
        take_off_slection=False
    elif take_off_choice == (2):
            Traval_costs = Traval_costs + 50
            print("continue with your selection")
            take_off_slection=False
    elif take_off_choice == (3):
                Traval_costs = Traval_costs+ 75
                print("continue with your selection")
                take_off_slection=False
    else:
                print("invald input")    
                
 # start of the destination part            
(print(destination[0][0],end = ' '), print(destination[0][1],end = ' '), print(destination[0][2]))
(print(destination[1][0],end = ' '), print(destination[1][1],end = ' '), print(destination[1][2]))
(print(destination[2][0],end = ' '), print(destination[2][1],end = ' '), print(destination[2][2]))
(print(destination[3][0],end = ' '), print(destination[3][1],end = ' '), print(destination[3][2]))

destination_slection=True

while destination_slection == True:
    take_off_choice = int(input("enter the corsponding number of destination that you wish to go to: "))
    if take_off_choice == (1):
        Traval_costs = Traval_costs + 326
        print("continue with your selection")
        destination_slection=False
    elif take_off_choice == (2):
            Traval_costs = Traval_costs +  378
            print("continue with your selection")
            destination_slection=False
    elif take_off_choice == (3):
                Traval_costs = Traval_costs + 1436
                print("continue with your selection")
                destination_slection=False
    elif take_off_choice == (4):
        Traval_costs + 2376
        print("continue with your selection")
        destination_slection=False                
    else:
                print("invald input")            
 

#start of the accmoadation
print ("The costs of accomodation are on a day by day bases")

(print(destination[0][0],end = ' '), print(destination[0][3],end = ' '), print(destination[0][4]),"per day")
(print(destination[1][0],end = ' '), print(destination[1][3],end = ' '), print(destination[1][4]),"per day")
(print(destination[2][0],end = ' '), print(destination[2][3],end = ' '), print(destination[2][4]),"per day")
(print(destination[3][0],end = ' '), print(destination[3][3],end = ' '), print(destination[3][4]),"per day")

 