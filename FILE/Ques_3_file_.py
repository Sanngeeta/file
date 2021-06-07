# Aapke paas ek list hai. Iss list mein har string ko ek file-question3.txt naam ki file mein nayi line mein daalo. Aapki list yeh rahi:


banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"] 
file=open("file_bank.txt","w")
i=0
while i<len(banks_list):
    file.write(banks_list[i])
    file.write("\n")
    i=i+1
file.close()



