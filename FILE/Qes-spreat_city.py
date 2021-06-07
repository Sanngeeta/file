my_num=open("people1_exercise.txt ","r")
for i in my_num:

    if "delhi" in i:
        f=open("delhi.txt","a")
        f.write(i)
    elif "shimla" in i:
        f=open("shimla.txt","a")
        f.write(i)
    else:
        f=open("other.txt","a")
        f.write(i)