#!/usr/bin/env python3
#Levi Noell-Baba, July 9, 2023, CPT-168-W17, Lab 9-1
from decimal import Decimal# Use of the "decimal module" and "importing the decimal class" for decimal numbers that yield unexpected results due to floating-point numbers which also "approximate values". Decimal module to get exact values rather than approximate values.  
from decimal import ROUND_HALF_UP # "ROUND_HALF_UP" constant for the quantize() method that rounds up if the neighboring numbers are equidistant from the last digit of a decimal number.
import locale as lc # Importing the "locale module into the lc namespace" to use for formatting the currency values as well as working with different locales.

# display a title
print("The Invoice program")
print()

choice = "y"
while choice == "y":
    
    # get the user entry
    order_total = Decimal(input("Enter order total: ")) #Use of the "Decimal class" from the decimal module in which you use a "constructor" of the decimal class to construct Decimal objects from "string values". 
    order_total = order_total.quantize(Decimal("1.00"), ROUND_HALF_UP) #Use of the "quantize method" of a "decimal object" that rounds the decumal values to the specified number of decimal places. 
    print()               

    # determine the discount percent
    if order_total > 0 and order_total < 100: #Use of an if statement and the and logical operator to create a decimal number for the "discount percentage" if the Order_total is greater than 0 and less than 100
        discount_percent = Decimal("0")
    elif order_total >= 100 and order_total < 250: #Use of an "elif clause" as well as the "AND" logical operator" to create a decimal number for the "discount percentage" if the order_total is between 100 and 250
        discount_percent = Decimal(".1")
    elif order_total >= 250: #Use of an "elif clause" to create a decimal number for the "discount percentage is the order total is over or equal to 250
        discount_percent = Decimal(".2")

    # calculate the results
    discount = order_total * discount_percent
    discount = discount.quantize(Decimal("1.00"), ROUND_HALF_UP)   #Use of the "quantize method" of a "decimal object" that rounds the decimal values to the specified number of dedimal places.                               
    subtotal = order_total - discount
    shipping_percentage = Decimal(".085") #calculation to get the shipping percentage. will create a decimal number for the shipping percentage
    shipping_cost = subtotal * shipping_percentage #value calculated by taking the given shipping percentage multiplied by the subtotal.
    shipping_cost = shipping_cost.quantize(Decimal("1.00"), ROUND_HALF_UP) #Shipping cost value is the valculation of shipping percentage multiplied by the subtotal. This calculation will create a decimal number for the "shipping cost" rounded up to 2 decimal places.
    tax_percent = Decimal(".05") #Use of a given tax percentage that takes advantage of the constructor of the decimal class which uses the "string" inside of the code statement to specify the tax percentage as a decimal number
    sales_tax = subtotal * tax_percent #use of a given sales tax value that takes the subtotal multiplied by the tax percentage
    sales_tax = sales_tax.quantize(Decimal("1.00"), ROUND_HALF_UP)# use of the quantize method of a decimal object that rounds the decimal values to the specified number of decimal places.                                  
    invoice_total = subtotal + sales_tax + shipping_cost #use of a given invoice total value that takes the subtotal plus shipping cost plus the sales tax.

    # display the results
    lc.setlocale(lc.LC_ALL, "us") #"setlocale() function used to set the local for the specified category to the "locale" for the specified country code and returns a string for the locale. LC_ALL is applied to specify that it affects all categories. "us" is used to set the local to English/United States.
    #lc.setlocale(lc.LC_ALL, "en_US") #Use of the "setlocale() function" that sets the locale to English/United States as default for most Mac/OS X systems.

    print("Order total:        {:>11}".format(lc.currency(order_total, grouping=True))) #print function that uses a nested "currency() function inside of a format() method. format method formats the order total amount by passing one value to the specification of the string. the "{:>11}" format specification passes a value into the string which becomes the users entry for the order total. the the currency funciton formats the specific value.
    print("Discount amount:    {:11,}".format(discount)) #print funciton that displays the "Discount amount". Nested inside of the print funciton is the "format() method" that specifies a field width of "11" according to the string specification that will result as the "Discount amount" entry in the appropriate column."{:11}" format specification represents a "left alignment" in the first column by default because there's only "one string specification" listed in the print funciton denoted by the one set of curly braces. 
    print("Subtotal:           {:11,}".format(subtotal)) #print function that displays the discount amount. nested in the print function is the format method that specifies a field width of "11" according to the string specification that will result as the discount amount entry. "{:11}" format specification represents a "left alignment" in the first column by default because there's only one string specification listed in this print function denoted by the one set of curly braces. 
    print("Shipping cost:      {:11,}".format(shipping_cost)) #print function that displays the shipping cost. nested in the print function is the format method that specifies a field width of "11" according to the string specification that will result as the shipping cost entry.  "{:11}" format specification represents a "left alignment" in the first column by default because there's only one string specification listed in this print function denoted by the one set of curly braces.
    print("Sales tax:          {:11,}".format(sales_tax)) #print function that displays the sales tax. nested in the print function is the format method that specifies a field width of "11" according to the string specification that will result as the sales tax entry.  "{:11}" format specification represents a "left alignment" in the first column by default because there's only one string specification listed in this print function denoted by the one set of curly braces.
    print("Invoice total:      {:>11}".format(lc.currency(invoice_total, grouping=True))) #print function that uses a nested "currency() function inside of a format() method. format method formats the invoice total amount by passing one value to the specification of the string. the "{:>11}" format specification passes a value into the string which becomes the users entry for the invoice total. the the currency funciton formats the specific value.
    print()

    choice = input("Continue? (y/n): ")    
    print()
    
print("Bye!")
