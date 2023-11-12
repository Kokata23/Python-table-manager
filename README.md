# Python table manager
 Python program meant for coffes\restaurants organization
 Its made using matrixes mainly and its my first bigger project made by myself only. It has many funtionalities, my task fist was creating a program that helps you manage how many tables does your coffe has and wheter they are free or taken

\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \



 
![Screenshot 2023-11-12 175200](https://github.com/Kokata23/Python-table-manager/assets/123099517/90fe4747-bdbb-4097-bc56-e7c75f40de32)




\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \



 
 by typing any number it changes from free to taken, simple right? 
That were exactly my toughts befor deciding dive a little deeper.As you can see it has a little description filed what you can do with the function, Im gonna cover the most complicated in my objection. I thought like what if someno gives me a call and wants a table for tonight? Whats happening then? So thats why I created functionalitie for booking a table for today, working with real time and date:


\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \


![Screenshot 2023-11-12 180834](https://github.com/Kokata23/Python-table-manager/assets/123099517/bdbad4d9-c154-48af-9479-91d80a4ede0c)



\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \

As you can see tabkle 23 is booked, not free or taken

The next method lets you reserve tables for future dates like tommorow or noext week, basicly whenever you want.
![Screenshot 2023-11-13 004916](https://github.com/Kokata23/Python-table-manager/assets/123099517/06f05454-5091-4134-be0f-24dbb27fe22d)

 table status stays free because we are reserving for tommorow, the date I have run those tests is 11/13/2023 its reserved for 11/14/2023.....the table is free for usage for today, you can book it take it or do whataver you want with it

 

Both your reservations and bookings are collected in different list

![Screenshot 2023-11-13 004916](https://github.com/Kokata23/Python-table-manager/assets/123099517/2ba311c1-7d5f-4ce2-9358-073611e2e4be)

when the date is todays date, the table automaticly becomes booked, gets deleted from reserved list, and is added to the booked list.


