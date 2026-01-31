#Restorent Menue

menu = {
    'coffee': 50,
    'Potato Chipes': 100,
    'Half checken curry' : 250,
    'Mutton biryanni': 200,
    'kabaab kanti':160,
    'salad':80,
    'chipes':20,
}

print("Welcom to Hotel Alfala.") 
print("coffee:50Rs\nPotato Chipes :100Rs\nHAlf Checken curry:250RS\nMutton biryanni:200RS\nKabaab kanti:160RS\nsalad:80Rs\nchipes")

Total_order = 0
item_01 = input("Enter the name of your first order =")

if item_01 in menu:

    Total_order += menu[item_01]
    print(f"You item {item_01}  is added to your order.")

else:
    print(f"Orderd item {item_01} is not avilable yet")

another_order = input("Do you want to add another item in your order? (Yes/No):")

if another_order == "yes":

    item_2 = input("Enter the name of second order =")
    if item_2 in menu:
       
       Total_order += menu[item_2]  
       print(f"item {item_2} has been added to order.")

    else:
       print(f"Sorry !! ordered item {item_2} is not avilable yet!")           #f --> farword 

       print(f"The total amount of item to pay is {Total_order}")

if another_order == "no":

    print(f"The total amount of the item to pay is {Total_order} ")