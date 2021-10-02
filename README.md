# pforcs-problem-sheet
bmi.py
 This program takes height in cm 
 converts height to m
 squras height 
 takes weight
 And weight divided by height in squared
 takes two numbers after decimal point
        ----------------------------------------------------
sendemail.py
 This program imports smtplib library
 sorts sender email and password, receivere email and the massege in variables
 login to Gmail using smtplib and sing in with sander account
 than sends the massege using server.sandemail function
        -----------------------------------------------------
bitcoin.py
 This program get bitcoinprice url as a json file
  and sorted it in a dict object
  and used for loop to access to it attribute (currency and price)
        -----------------------------------------------------
collatz.py
 Asks the user to input any positive integer.
 the value goes to while loop until it become one and print at the end.
 At each step in while loop calculate the next value by taking the current value and,
 If it is even, divide it by two and print it,
 but if it is odd, multiply it by three and add one and print it.
        -------------------------------------------------------
squareroot.py
 This program asks the user to input a positive integer or enter/return to quit
 after that its convert the number to float and send to its own sqrt funtcion 
 the function returns an approximation of its square root.
        -------------------------------------------------------
es.py
 This program takes the file name from an argument on the command line 
 if the file is not exit it will print a wraning massege 
 if it exit it will take it to own readNumber function that counts who many e's the file has
 and print the number.   
       ---------------------------------------------------------
extract-url.py
 This program got all the urls from log file using url experssion
 then splited the urls using ? character to split the url to page and query(parameters) 
 then put the query string paramerts in a dic 
 then built the file dic as requested
       ---------------------------------------------------------
plottask.py
 This program saves a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in png picture
 the x point take from the range [0, 4]
 this programm required to import matplotlib.pyplot and numpy libraries 
       ---------------------------------------------------------
pandastask.py
 This program reads data from log file into dataframe by using read_csv function 
 sets the datatime to be an index by finding data time useing regular expression and to_datetime function
 and extracts the session id from the URLs and store them in a different column useing regular expression
 then use groupby function to get the sum of all the data downloaded by each sessionId
 finally creates a histogram plot to present result
       ---------------------------------------------------------
bulletproof.py
 this program have a listEnter fuction so the user can enter a list
 and IndexEnter function to enter any number 
 and averageTo function that take the list and the index, 
 and return the averge and add the index to the list
 the program print a error massege if list lenght or any item list or the index in not a number