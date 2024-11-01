String=input("Enter a word:")
char=input("Enter a character:")
i=0
count=0
while(i<len(String)):
    if(String[i]==char):
        count=count+1
    i=i+1
print("Total number of times",char,"the has occured = ",count)