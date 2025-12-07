sum_ofodd = 0
sum_ofeven = 0
total =0

#step 1
card_number= input("enter a no.00")
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number=card_number[::-1]

#step 2
for x in card_number[::2]:
    sum_ofodd = sum_ofodd+int(x)

#step 3
for x in card_number[1::2]:
    x=int(x)*2
    if x>=10:
        sum_ofeven+=(1+(x%10))
    else:
        sum_ofeven+=x

#step 4

total = sum_ofeven + sum_ofodd
if(total%10==0):
    print("valid")
else:
    print("invalid")