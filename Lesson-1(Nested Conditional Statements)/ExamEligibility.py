# take input from user wether he can atend the class or not
medical_cause=input("did you have a medical cause Y or N:")
# take input for attendance
atten=int(input("Enter the attendance of the student:"))

# checking the output
if medical_cause =="Y":
    print("You are allowed")
else:
    if atten>=75:
        print("Allowed")
    else:
        print("Not Allowed")