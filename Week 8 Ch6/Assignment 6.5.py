##Assignment 6.5
##Write code using find() and string slicing
##(see section 6.10) to extract the number at the
##end of the line below. Convert the extracted
##value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";
atpos = text.find('5')
print(atpos)
num = float(atpos)
print(num)
#print(atpos)






































"""
atpos = text.find('0')
print atpos

num = text[23:29]
num = float(num)
print num
"""
