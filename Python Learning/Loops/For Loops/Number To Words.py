ones  = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
teens = [ "Ten","Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
tens  = [ "","", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

number = int(input("Enter the Number :- "))
word =""
c = 0

if 0 <= number <10:
    print(ones[number])
elif 10 <= number < 20:
    print(teens[number-10])    
elif 20 <= number < 100:
    for x in str(number):
        c += 1
        n = int(x)
        if c == 1 :
            word += tens[n]  
        if c == 2 and n != 0:
            word += " " + ones[n] 
    print(word)       

elif 100 <= number < 1000:
    first_letter = number // 100 
    word += ones[first_letter] + " Hundred"
    
    two_letters = number % 100 

    second_letter = two_letters // 10
    third_letter = two_letters % 10
    if second_letter == 1:
        word += " " + teens[third_letter]
    else:
        if second_letter != 0:
            word += " " + tens[second_letter]
    if second_letter != 1  and third_letter != 0 : 
        word += " " + ones[third_letter]
    print(word)