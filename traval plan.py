#traval plan

#lists of citys costs and flights

accommodation  = [["Sydney","$", 120], ["Tonga","$", 40], ["Shanghai","$", 60], ["London","$", 80]]
take_off = [["1  Auckland","$", 0], ["2  Wellington",'$', 50], ["3  Christchurch","$", 75]]
destination = [["1  Sydney","$", 326], ["2  Tonga","$", 378], ["3  Shanghai","$", 1436], ["4  London","$", 2376]]

#total cost for flights and accommodation
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
    take_off_choice = int(input("enter the corsponding number of the city you wish to leave from: "))
    if take_off_choice == (1):
        Traval_costs + 0
        print("continue with your selection")
        take_off_slection=False
    elif take_off_choice == (2):
            Traval_costs + 50
            print("continue with your selection")
            take_off_slection=False
    elif take_off_choice == (3):
                Traval_costs + 75
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
        Traval_costs + (326)
        print("continue with your selection")
        destination_slection=False
    elif take_off_choice == (2):
            Traval_costs + 50
            print("continue with your selection")
            destination_slection=False
    elif take_off_choice == (3):
                Traval_costs + 75
                print("continue with your selection")
                destination_slection=False
    elif take_off_choice == (4):
        Traval_costs + 75
        print("continue with your selection")
        destination_slection=False                
    else:
                print("invald input")            
        
    print("$", Traval_costs)