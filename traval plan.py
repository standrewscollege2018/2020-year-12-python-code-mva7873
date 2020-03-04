#traval plan

#lists of citys costs and flights

accommodation  = [["Sydney","$", 120], ["Tonga","$", 40], ["Shanghai","$", 60], ["London","$", 80]]
take_off = [["Auckland","$", 0], ["Wellington",'$', 50], ["Christchurch","$", 75]]
destination = [["Sydney","$", 326], ["Tonga","$", 378], ["Shanghai","$", 1436], ["London","$", 2376]]

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
    take_off_choice = input("enter the city you wish to leave from: ")
    if take_off_choice == (take_off[0][0]):
        Traval_costs + 0
        print("continue with your selection")
        take_off_slection=False
    else:
        print("invald input")
