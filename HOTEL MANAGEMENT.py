total = 0
import time
import mysql.connector as ms
mydb = ms.connect(host='localhost',user='root',passwd='12345',database='hotel_management')
mc = mydb.cursor()

#Booking a room
def b_room(): 
     ch = 'y'
     displaypr()
     print('='*40)
     while ch in 'Yy':
          print('='*40)
          n = input('ENTER CUSTOMER NAME: ')
          a = int(input('ENTER NUMBER OF ADULTS(ABOVE 12): '))
          k = int(input('ENTER NUMBER OF CHILDREN: '))
          nm = a + k         
          if nm > 0 and nm <= 2:
               ci = input("ENTER CHECK-IN DATE(YYYY/MM/DD): ")
               co = input("ENTER CHECK-OUT DATE(YYYY/MM/DD): ")
               print()
               print("FOR",nm,",YOU HAVE BEEN ALLOTED FIRST FLOOR ROOMS, KINDLY CHOOSE ONE OF THE BELOW...")
               time.sleep(1)
               mc.execute('select * from f1_rooms')
               data = mc.fetchall()
               print('-'*40)
               print('=============1ST FLOOR ROOMS============')
               print('-'*40)
               if mc.rowcount>0:
                    print('SNO','%15s'%'ROOM_NO','%15s'%'STATUS')
                    print('-'*40)
               for i in data:
                    print(i[0],'%15s'%i[1],'%20s'%i[2])
                    print('-'*40)
               rno = int(input('ENTER AN AVAILABLE ROOM NUMBER: '))
               l = []
               mc.execute('select room_no from f1_rooms')
               data = mc.fetchall()
               for i in data:
                    l.append(i[0])
               if rno in l:
                    mc.execute('Select * from f1_rooms where room_no={}'.format(rno))
                    data = mc.fetchall()
                    status = 'BOOKED'
                    for i in data:
                         if i[2] == 'AVAILABLE':
                              mc.execute('update f1_rooms set STATUS="{}" where ROOM_NO={}'.format(status,rno))
                              mydb.commit()
                              mc.execute('select * from f1_rooms where room_no={}'.format(rno))
                              data=mc.fetchall()
                              print('-'*40)
                              print('=============1ST FLOOR ROOMS=============')
                              print('-'*40)
                              if mc.rowcount>0:
                                   print('SNO','%14s'%'ROOM_NO','%17s'%'STATUS')
                                   print('-'*40)
                              for i in data:
                                   print(i[0],'%15s'%i[1],'%20s'%i[2])
                                   print('-'*40)
                                   print('')
                                   print('***ROOM IS SUCCESSFULLY BOOKED',n.upper(),'***')
                                   
                              mc.execute("insert into crecords values({},'{}','{}','{}')".format(rno,n.upper(),ci,co))
                              mydb.commit()
                              time.sleep(1)
                              mc.execute('select * from crecords where room_no={}'.format(rno))
                              data = mc.fetchall()
                              if mc.rowcount>0:
                                   print('-'*50)
                                   print('ROOM NO','%12s'%'C_NAME','%13s'%'CHECK_IN','%14s'%'CHECK_OUT')
                                   print('-'*50)
                              for i in data:
                                   print(i[0],'%16s'%i[1],'%13s'%i[2],'%14s'%i[3])
                                   print('-'*50)
                              print('GOING BACK TO MAIN MENU....')
                              time.sleep(3)
                              main()
                         elif i[2] == 'BOOKED':
                              print("-"*40)
                              print('**ROOM IS NOT AVAILABLE, CHOOSE AN AVAILABLE ONE**')
                              ch = input('TRY AGAIN?(Y/N) ')
               else:
                    print("-"*40)
                    print("**ROOM NUMBER DOESN'T EXIST**")
                    ch = input('TRY AGAIN?(Y/N) ')
                    
          elif nm <= 4 and nm > 2:
               ci = input("ENTER CHECK-IN DATE(YYYY/MM/DD): ")
               co = input("ENTER CHECK-OUT DATE(YYYY/MM/DD): ")
               print()
               print("FOR",nm,",YOU HAVE BEEN ALLOTED SECOND FLOOR ROOMS, KINDLY CHOOSE ONE OF THE BELOW...")
               time.sleep(1)
               mc.execute('select * from f2_rooms')
               data=mc.fetchall()
               print('-'*40)
               print('=============2ND FLOOR ROOMS=============')
               print('-'*40)
               if mc.rowcount>0:
                    print('SNO','%15s'%'ROOM_NO','%15s'%'STATUS')
                    print('-'*40)     
               for i in data:
                    print(i[0],'%15s'%i[1],'%20s'%i[2])
                    print('-'*40)
               rno = int(input('ENTER AN AVAILABLE ROOM NUMBER: '))
               l = []
               mc.execute('select room_no from f2_rooms')
               data = mc.fetchall()
               for i in data:
                    l.append(i[0])
               if rno in l:
                    mc.execute('Select * from f2_rooms where room_no={}'.format(rno))
                    data = mc.fetchall()
                    status = 'BOOKED'
                    for i in data:
                         if i[2] == 'AVAILABLE':
                              mc.execute('update f2_rooms set STATUS="{}" where ROOM_NO={}'.format(status,rno))
                              mydb.commit()
                              mc.execute('select * from f2_rooms where room_no={}'.format(rno))
                              data = mc.fetchall()
                              print('-'*40)
                              if mc.rowcount>0:
                                   print('SNO','%14s'%'ROOM_NO','%17s'%'STATUS')
                                   print('-'*40)
                              for i in data:
                                   print(i[0],'%15s'%i[1],'%20s'%i[2])
                                   print('-'*40)
                                   print('')
                                   print('***ROOM IS SUCCESSFULLY BOOKED',n.upper(),'***')
                                   
                              mc.execute("insert into crecords values({},'{}','{}','{}')".format(rno,n.upper(),ci,co))
                              mydb.commit()
                              time.sleep(1)
                              mc.execute('select * from crecords where room_no={}'.format(rno))
                              data = mc.fetchall()
                              if mc.rowcount>0:
                                   print('-'*50)
                                   print('ROOM NO','%12s'%'C_NAME','%13s'%'CHECK_IN','%14s'%'CHECK_OUT')
                                   print('-'*50)
                              for i in data:
                                   print(i[0],'%16s'%i[1],'%13s'%i[2],'%14s'%i[3])
                                   print('-'*50)
                              print('GOING BACK TO MAIN MENU....')
                              time.sleep(3)
                              main()
                         elif i[2] == 'BOOKED':
                              print("-"*40)
                              print('**ROOM IS NOT AVAILABLE, CHOOSE AN AVAILABLE ONE**')
                              ch = input('TRY AGAIN?(Y/N) ')
               else:
                    print("-"*40)
                    print("**ROOM NUMBER DOESN'T EXIST**")
                    ch = input('TRY AGAIN?(Y/N) ')
                    
          elif nm <= 8 and nm > 4:
               ci = input("ENTER CHECK-IN DATE(YYYY/MM/DD): ")
               co = input("ENTER CHECK-OUT DATE(YYYY/MM/DD): ")
               print()
               print("FOR",nm,",YOU HAVE BEEN ALLOTED THIRD FLOOR ROOMS, KINDLY CHOOSE ONE OF THE BELOW...")
               time.sleep(1)
               mc.execute('select * from f3_rooms')
               data = mc.fetchall()
               print('-'*40)
               print('=============3RD FLOOR ROOMS=============')
               print('-'*40)
               if mc.rowcount>0:
                    print('SNO','%15s'%'ROOM_NO','%15s'%'STATUS')
                    print('-'*40)     
               for i in data:
                    print(i[0],'%15s'%i[1],'%20s'%i[2])
                    print('-'*40)
               rno = int(input('ENTER AN AVAILABLE ROOM NUMBER: '))
               l = []
               mc.execute('select room_no from f3_rooms')
               data = mc.fetchall()
               for i in data:
                    l.append(i[0])
               if rno in l:
                    mc.execute('Select * from f3_rooms where room_no={}'.format(rno))
                    data = mc.fetchall()
                    status = 'BOOKED'
                    for i in data:
                         if i[2] == 'AVAILABLE':
                              mc.execute('update f3_rooms set STATUS="{}" where ROOM_NO={}'.format(status,rno))
                              mydb.commit()
                              mc.execute('select * from f3_rooms where room_no={}'.format(rno))
                              data = mc.fetchall()
                              print('-'*40)
                              if mc.rowcount>0:
                                   print('SNO','%14s'%'ROOM_NO','%17s'%'STATUS')
                                   print('-'*40)
                              for i in data:
                                   print(i[0],'%15s'%i[1],'%20s'%i[2])
                                   print('-'*40)
                                   print('')
                                   print('***ROOM IS SUCCESSFULLY BOOKED',n.upper(),'***')
                                   
                              mc.execute("insert into crecords values({},'{}','{}','{}')".format(rno,n.upper(),ci,co))
                              mydb.commit()
                              time.sleep(1)
                              mc.execute('select * from crecords where room_no={}'.format(rno))
                              data=mc.fetchall()
                              if mc.rowcount>0:
                                   print('-'*50)
                                   print('ROOM NO','%12s'%'C_NAME','%13s'%'CHECK_IN','%14s'%'CHECK_OUT')
                                   print('-'*50)
                              for i in data:
                                   print(i[0],'%16s'%i[1],'%13s'%i[2],'%14s'%i[3])
                                   print('-'*50)
                              print('GOING BACK TO MAIN MENU....')
                              time.sleep(3)
                              main()
                              
                         elif i[2] == 'BOOKED':
                              print('-'*40)
                              print('**ROOM IS NOT AVAILABLE, CHOOSE AN AVAILABLE ONE**')
                              ch = input('TRY AGAIN?(Y/N) ')
               else:
                    print('-'*40)
                    print("**ROOM NUMBER DOESN'T EXIST**")
                    ch = input('TRY AGAIN?(Y/N) ')
          else:
               print('-'*40)
               print('**MAXIMUM CAPACITY FOR A ROOM IS 8**')
               ch = input('TRY AGAIN?(Y/N) ')
     
     print('GOING BACK TO MAIN MENU....')
     time.sleep(3)
     main()

#Calculating food prices
def foodpurchased():
     global total
     foodprices()
     print('='*40)
     print('6','%17s'%'TOTAL BILL')
     print('-'*40)
     de,be,bf,lu,di = 0,0,0,0,0
     c = 'y'
     while c in 'Yy':
         print('='*40)
         ch = int(input("ENTER THE NUMBER OF YOUR CHOICE: "))
         if ch == 1:
             mc.execute('select * from food where sno={}'.format(ch))
             data = mc.fetchall()
             for i in data:
                  p = int(input("ENTER NUMBER OF DESSERTS: "))
                  de = p * i[2]
                  print("YOUR TOTAL DESSERT COST IS:", de)
                  
         elif ch == 2:
             mc.execute('select * from food where sno={}'.format(ch))
             data=mc.fetchall()
             for i in data:
                  p = int(input("ENTER NUMBER OF BEVERAGES: "))
                  be= p * i[2]
                  print("YOUR TOTAL BEVERAGE COST IS:", be)

         elif ch == 3:
             mc.execute('select * from food where sno={}'.format(ch))
             data = mc.fetchall()
             for i in data:
                  p = int(input("ENTER NUMBER OF BREAKFAST MEALS: "))
                  bf = p * i[2]
                  print("YOUR TOTAL BREAKFAST COST IS:", bf)

         elif ch == 4:
             mc.execute('select * from food where sno={}'.format(ch))
             data = mc.fetchall()
             for i in data:
                  p = int(input("ENTER NUMBER OF LUNCH MEALS: "))
                  lu = p * i[2]
                  print("YOUR TOTAL LUNCH COST IS:", lu)

         elif ch == 5:
             mc.execute('select * from food where sno={}'.format(ch))
             data = mc.fetchall()
             for i in data:
                  p = int(input("ENTER NUMBER OF DINNER MEALS: "))
                  di = p * i[2]
                  print("YOUR TOTAL DINNER COST IS:", di)
                  
         elif ch == 6:
              total = de + be + bf + lu + di
              print('YOUR TOTAL FOOD COST IS',total)
              print('GOING BACK TO MAIN MENU....')
              time.sleep(3)
              main()

         else:
              print('-'*40)
              print('**INVALID CHOICE**')
              c = input('TRY AGAIN?(Y/N) ')
              
     print('GOING BACK TO MAIN MENU....')
     time.sleep(3)
     main()

#cancelling a room     
def cancel():
     ch = 'y'
     while ch in 'Yy':
          print('='*40)
          fno = int(input('ENTER YOUR FLOOR NUMBER(1/2/3): '))      
          if fno == 1:
               rno = int(input('ENTER ROOM NUMBER TO BE CANCELLED: '))
               l1 = []
               mc.execute('select room_no from f1_rooms')
               data = mc.fetchall()
               for i in data:
                    l1.append(i[0])
               if rno in l1:
                    mc.execute('select * from f1_rooms where room_no={}'.format(rno))
                    data = mc.fetchall()
                    status = 'AVAILABLE'
                    for i in data:
                         if i[2] == 'BOOKED':
                              mc.execute("update f1_rooms set status='{}' where room_no={}".format(status,rno))
                              mydb.commit()
                              mc.execute('select * from f1_rooms where room_no={}'.format(rno))
                              data = mc.fetchall()
                              print('-'*40)
                              print('=============1ST FLOOR ROOMS=============')
                              print('-'*40)
                              if mc.rowcount>0:
                                        print('SNO','%14s'%'ROOM_NO','%17s'%'STATUS')
                                        print('-'*40)
                              for i in data:
                                        print(i[0],'%15s'%i[1],'%20s'%i[2])
                                        print('-'*40)      
                              mc.execute('delete from crecords where room_no={}'.format(rno))
                              mydb.commit()
                              print('**ROOM HAS BEEN CANCELLED**')
                              print('GOING BACK TO MAIN MENU....')
                              time.sleep(3)
                              main()
                                   
                         elif i[2] == 'AVAILABLE':
                                   print('-'*40)
                                   print('**ROOM HAS NEVER BEEN BOOKED**')
                                   ch = input('TRY AGAIN(Y/N)? ')
               else:
                    print('-'*40)
                    print("**ROOM NO DOESN'T EXIST**")
                    ch=input('TRY AGAIN?(Y/N) ')          
               
          elif fno == 2:
               rno = int(input('ENTER ROOM NUMBER TO BE CANCELLED: '))
               l1 = []
               mc.execute('select room_no from f2_rooms')
               data = mc.fetchall()
               for i in data:
                    l1.append(i[0])
               if rno in l1:
                    mc.execute('select * from f2_rooms where room_no={}'.format(rno))
                    data = mc.fetchall()
                    status = 'AVAILABLE'
                    for i in data:
                         if i[2] == 'BOOKED':
                              mc.execute("update f2_rooms set status='{}' where room_no={}".format(status,rno))
                              mydb.commit()
                              mc.execute('select * from f2_rooms where room_no={}'.format(rno))
                              data = mc.fetchall()
                              print('-'*40)
                              print('=============2ND FLOOR ROOMS=============')
                              print('-'*40)
                              if mc.rowcount>0:
                                   print('SNO','%14s'%'ROOM_NO','%17s'%'STATUS')
                                   print('-'*40)
                              for i in data:
                                   print(i[0],'%15s'%i[1],'%20s'%i[2])
                                   print('-'*40)
                              mc.execute('delete from crecords where room_no={}'.format(rno))
                              mydb.commit()
                              print('**ROOM HAS BEEN CANCELLED**')
                              print('GOING BACK TO MAIN MENU....')
                              time.sleep(3)
                              main()
                              
                         elif i[2] == 'AVAILABLE':
                              print('-'*40)
                              print('**ROOM HAS NEVER BEEN BOOKED**')
                              ch=input('TRY AGAIN?(Y/N) ')
               else:
                    print('-'*40)
                    print("**ROOM NO DOESN'T EXIST**")
                    ch = input('TRY AGAIN?(Y/N) ')
                    
          elif fno == 3:
               rno = int(input('ENTER ROOM NUMBER TO BE CANCELLED: '))
               l1 = []
               mc.execute('select room_no from f3_rooms')
               data = mc.fetchall()
               for i in data:
                    l1.append(i[0])
               if rno in l1:
                    mc.execute('select * from f3_rooms where room_no={}'.format(rno))
                    data = mc.fetchall()
                    status = 'AVAILABLE'
                    for i in data:
                         if i[2] == 'BOOKED':
                              mc.execute("update f3_rooms set status='{}' where room_no={}".format(status,rno))
                              mydb.commit()
                              mc.execute('select * from f3_rooms where room_no={}'.format(rno))
                              data = mc.fetchall()
                              print('-'*40)
                              print('=============3RD FLOOR ROOMS=============')
                              print('-'*40)
                              if mc.rowcount>0:
                                   print('SNO','%14s'%'ROOM_NO','%17s'%'STATUS')
                                   print('-'*40)
                              for i in data:
                                   print(i[0],'%15s'%i[1],'%20s'%i[2])
                                   print('-'*40)
                              mc.execute('delete from crecords where room_no={}'.format(rno))
                              mydb.commit()
                              print('**ROOM HAS BEEN CANCELLED**')
                              print('GOING BACK TO MAIN MENU....')
                              time.sleep(3)
                              main()
                              
                         elif i[2] == 'AVAILABLE':
                              print('-'*40)
                              print('**ROOM HAS NEVER BEEN BOOKED**')
                              ch = input('TRY AGAIN?(Y/N) ')                        
               else:
                    print('-'*40)
                    print("**ROOM NO DOESN'T EXIST**")
                    ch = input('TRY AGAIN?(Y/N) ')
          else:
               print('-'*40)
               print('**INVALID FLOOR**')
               ch = input('TRY AGAIN?(Y/N) ')
               
     print('GOING BACK TO MAIN MENU....')
     time.sleep(3)
     main()

#displaying customer records     
def crecords():
     mc.execute('select * from crecords')
     data = mc.fetchall()
     print('-'*50)
     print('===========DISPLAYING CUSTOMER RECORDS============')
     print('-'*50)
     time.sleep(1)
     if mc.rowcount>0:
          print('ROOM NO','%12s'%'C_NAME','%13s'%'CHECK_IN','%14s'%'CHECK_OUT')
          print('-'*50)
     for i in data:
          print(i[0],'%16s'%i[1],'%13s'%i[2],'%14s'%i[3])
          print('-'*50)

#displaying room prices     
def displaypr():
     mc.execute('select * from r_prices')
     data=mc.fetchall()
     print('-'*40)
     print('========PRICES PER NIGHT (INR)==========')
     print('-'*40)
     if mc.rowcount>0:
          print('SNO','%15s'%'FLOORS','%15s'%'PRICE')
          print('-'*40)     
     for i in data:
          print(i[0],'%19s'%i[1],'%12s'%i[2])
          print('-'*40)

#displaying food prices          
def foodprices():
     mc.execute('select * from food')
     data = mc.fetchall()
     print('-'*40)
     print('===============HOTEL MENU===============')
     print('-'*40)
     if mc.rowcount>0:
         print('SNO','%13s'%'MENU','%16s'%'PRICE')
         print('-'*40)
     for i in data:
         print(i[0],'%17s'%i[1],'%13s'%i[2])
         print('-'*40)
         
def dcheck():
     ch = 'y'
     while ch in 'Yy':
          print('*'*40)
          rno = int(input('ENTER YOUR ROOM NUMBER: '))
          n = input('ENTER YOUR NAME AS GIVEN IN RECORD: ')
          mc.execute('select room_no from crecords')
          data = mc.fetchall()
          list1 = []
          for i in data:
               list1.append(i[0])
          if rno in list1:
               mc.execute('select * from crecords where room_no={}'.format(rno))
               data = mc.fetchall()
               for i in data:
                    if i[1] == n.upper():
                         print('ROOM FOUND...')
                         print('-'*40)
                         time.sleep(2)
                         grand()             
                    else:
                         print('-'*40)
                         print('**CUSTOMER RECORD NOT FOUND**')
                         ch=input('TRY AGAIN?(Y/N) ')       
          else:
               print('-'*40)
               print("**ROOM NUMBER IS AVAILABLE/DOESN'T EXIST**")
               ch=input('TRY AGAIN?(Y/N) ')
               
     print('GOING BACK TO MAIN MENU....')
     time.sleep(3)
     main()

#Calculating grand total     
def grand():
     ch = 'y'
     while ch in 'Yy':
          fno = int(input('ENTER YOUR FLOOR NUMBER: '))
          if fno in (1,2,3):
               mc.execute('select * from r_prices where sno={}'.format(fno))
               data = mc.fetchall()
               nn = int(input('NUMBER OF NIGHTS YOU HAVE STAYED: '))
               for i in data:
                    print('-'*40)
                    print('----DISPLAYING YOUR PRICE----')
                    time.sleep(2)
                    print('-'*40)
                    print('YOUR ROOM PRICE IS',i[2] * nn)
                    print('-'*40)
                    print('YOUR TOTAL FOOD COST IS:',total)
                    print('-'*40)
                    time.sleep(2)
                    gt= (i[2] * nn) + total
                    print('YOUR GRAND TOTAL IS: ',gt)
                    print('-'*40)
                    print('**THANK YOU FOR YOUR STAY, VISIT AGAIN**')
                    print('-'*40)
                    time.sleep(2)
                    exit()
          else:
               print("-"*40)
               print('**INVALID NUMBER GIVEN**')
               ch=input('TRY AGAIN?(Y/N) ')
               
     print('GOING BACK TO MAIN MENU....')
     time.sleep(3)
     main()

#Employee access             
def employee():
     d = 12345
     ch = 'y'
     while ch == 'y':
          print('='*40)
          ena = input('ENTER EMPLOYEE NAME: ')
          l = []
          mc.execute('select emp_name from employee')
          data = mc.fetchall()
          for i in data:
               l.append(i[0])
          if ena.upper() in l:
               pw = int(input('ENTER PASSWORD: '))
               if pw == d:
                    print('*'*40)
                    print('WELCOME TO HOTEL EMPLOYEE ACCESS',ena.upper())
                    break
               else:
                    print('*'*40)
                    print('**INVALID PASSWORD**')
                    i=input('TRY AGAIN?(Y/N) ')
                    if i in 'Nn':
                         print('GOING BACK TO MAIN MENU....')
                         time.sleep(2)
                         main()
          else:
               print("*"*40)
               print('**EMPLOYEE NOT FOUND**')
               e = input('TRY AGAIN?(Y/N) ')
               if e in 'Nn':
                    print('GOING BACK TO MAIN MENU....')
                    time.sleep(2)
                    main()
                    
     while True:
          time.sleep(1)
          print('='*50)
          print("""TO MODIFY ROOM PRICES, ENTER 1
TO MODIFY FOOD PRICES, ENTER 2
TO DISPLAY CUSTOMER RECORDS,ENTER 3
TO EXIT EMPLOYEE ACCESS,ENTER 4""")
          m=int(input("ENTER YOUR CHOICE: "))
          
          if m == 1:
               print('*'*40)
               print("DISPLAYING ROOM PRICES.....")
               time.sleep(2)
               print()
               displaypr()
               time.sleep(1)
               ch = 'y'
               while ch in 'Yy':
                    print('-'*40)
                    print("""ENTER 1 TO MODIFY FIRST FLOOR
ENTER 2 TO MODIFY SECOND FLOOR
ENTER 3 TO MODIFY THIRD FLOOR""")
                    print('-'*40)
                    fno=int(input('ENTER FLOOR NUMBER: '))
                    if fno in (1,2,3):
                         mc.execute('select price from r_prices where sno={}'.format(fno))
                         data = mc.fetchall()
                         price = int(input('ENTER NEW PRICE: '))
                         for i in data:
                              if price != i[0]:
                                   mc.execute('update r_prices set PRICE={} where sno={}'.format(price,fno))
                                   mydb.commit()
                                   mc.execute('select * from r_prices where sno={}'.format(fno))
                                   data = mc.fetchall()
                                   print('-'*40)
                                   print("=============PRICES CHANGED============")
                                   print('-'*40)
                                   if mc.rowcount>0:
                                        print('SNO','%14s'%'FLOORS','%17s'%'PRICE')
                                        print('-'*40)
                                   for i in data:
                                        print(i[0],'%15s'%i[1],'%20s'%i[2])
                                        print('-'*40)
                                   ch = input('CHANGE ANOTHER PRICE?(Y/N) ')
                                   if ch in 'Yy':
                                        break
                                   elif ch in 'Nn':
                                        print('-'*40)
                                        print('GOING BACK TO EMPLOYEE ACCESS....')
                                        time.sleep(2)
                                        
                              elif price == i[0]:
                                   print('-'*40)
                                   print('**THE PRICE ENTERED IS SAME**')
                                   print('**TRY AGAIN**')
                                   time.sleep(2)
                                   break                                   
                    else:
                         print('-'*40)
                         print('**INVALID FLOOR ENTERED**')
                         ch=input('TRY AGAIN?(Y/N) ')
                         if ch in 'Nn':
                              print('GOING BACK TO EMPLOYEE ACCESS....')
                              time.sleep(2)                           
                    
          elif m==2:
               print('*'*40)
               print('DISPLAYING FOOD PRICES.....')
               time.sleep(2)
               print()
               foodprices()
               time.sleep(1)
               ch = 'y'
               while ch in 'Yy':
                    print('-'*40)
                    print("""ENTER 1 TO MODIFY DESSERT PRICES
ENTER 2 TO MODIFY BEVERAGE PRICES
ENTER 3 TO MODIFY BREAKFAST PRICES
ENTER 4 TO MODIFY LUNCH PRICES
ENTER 5 TO MODIFY DINNER PRICES""")
                    print('-'*40)
                    fono=int(input('ENTER FOOD CHOICE: '))
                    if fono in (1,2,3,4,5):
                         mc.execute('select price from food where sno={}'.format(fono))
                         data = mc.fetchall()
                         price = int(input('ENTER NEW PRICE: '))
                         for i in data:
                              if price != i[0]:
                                   mc.execute('update food set price={} where sno={}'.format(price,fono))
                                   mydb.commit()
                                   mc.execute('select * from food where sno={}'.format(fono))
                                   data = mc.fetchall()
                                   print('-'*40)
                                   print('=============PRICES CHANGED=============')
                                   print('-'*40)
                                   if mc.rowcount>0:
                                        print('SNO','%18s'%'MENU','%17s'%'PRICE')
                                        print('-'*40)
                                   for i in data:
                                        print(i[0],'%20s'%i[1],'%17s'%i[2])
                                        print('-'*40)
                                   ch = input('CHANGE ANOTHER PRICE?(Y/N) ')
                                   if ch in 'Yy':
                                        break
                                   elif ch in 'Nn':
                                        print('GOING BACK TO EMPLOYEE ACCESS....')
                                        time.sleep(2)
                                        
                              elif price == i[0]:
                                   print('-'*40)
                                   print('**THE PRICE ENTERED IS SAME**')
                                   print('**TRY AGAIN**')
                                   time.sleep(2)
                                   break
                    else:
                         print("-"*40)
                         print('**INVALID CHOICE**')
                         ch=input('TRY AGAIN?(Y/N) ')
                         if ch in 'Nn':
                              print('GOING BACK TO EMPLOYEE ACCESS....')
                              time.sleep(2)
                              
          elif m==3:
               crecords()
               
          elif m==4:
               print('-'*40)
               print('EXITING EMPLOYEE ACCESS...')
               time.sleep(2)
               main()
          
          else:
               print('-'*40)
               print('**YOU HAVE ENTERED AN INVALID OPTION**')
               ch=input('TRY AGAIN?(Y/N) ')
               if ch in 'Nn':
                    print('GOING BACK TO MAIN MENU....')
                    time.sleep(2)
                    main()
#Main program                    
def main():
     
     try:
          print('-'*40)
          print('==================MENU==================')
          print('-'*40)
          print("TO BOOK A ROOM, ENTER 1")
          print('-'*40)
          print("TO PURCHASE FOOD ITEMS,ENTER 2")
          print('-'*40)
          print("TO CANCEL ROOM,ENTER 3")
          print('-'*40)
          print("TO DISPLAY GRAND TOTAL,ENTER 4")
          print('-'*40)
          print("FOR EMPLOYEE ACCESS,ENTER 5")
          print('-'*40)
          print("TO EXIT,ENTER 6")
          print('-'*40)
          c = int(input('ENTER YOUR CHOICE: '))
          
          if c == 1:
               b_room()
               
          elif c == 2:
               #total = 0
               foodpurchased()
               
          elif c == 3:
               cancel()
               
          elif c == 4:
               dcheck()
               
          elif c == 5:
               employee()
               
          elif c == 6:
               print('*'*20)
               print('EXITING...')
               time.sleep(2)
               exit()
               
          else:
               print('**YOU HAVE ENTERED AN INVALID CHOICE**')
               time.sleep(1)
               main()
               
     except:
          print('*'*64)
          print('**YOU HAVE ENTERED AN INVALID CHARACTER, PLEASE ENTER A NUMBER**')
          print('*'*64)
          time.sleep(1)
          main()        
print('*'*40)
print("--------WELCOME TO HOTEL VIENNA---------")
print('*'*40)
while True:
     main()    
