class Function():
    def Subfeilds():
        print("Sub-fields in AI are:")
        Ai_list=[
            "Machine learning",
             "Neural Networks",
             "vision", 
             "Robotics",
             "Speech Processing",
             "Natural Language Processing"
        ]
        for temp in Ai_list:
            print(temp)

    

    def OddEven():
                age=int(input("Enter a number:"))
                if(age%2==0):
                    print(age,"is Even number",)
                    age1="Even number"
                    return age1
                else:
                    print(age,"is Odd number")
                    age2="Odd number"
                    return age2
    def Eligible():
        sex=input("Your Gender:")
        age=int(input("Your Age:"))
        if(age>=18 and sex=="Female"):
            print("Eligible")
            cate="Eligible"
        elif(age>=21 and sex=="Male"):
            print("Eligible")
            cate="Eligible"
        else:
            print("Not Eligible")
            cate="Not Eligible"
        return cate

    def Percentage():
            sub1=int(input("subject1:"))
            sub2=int(input("subject2:"))
            sub3=int(input("subject3:"))
            sub4=int(input("subject4:"))
            sub5=int(input("subject5:"))
            Total=sub1+sub2+sub3+sub4+sub5
            print("Total:",Total)
            percentage=Total/5
            print("Percentage:",percentage)
            return percentage

    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        print("Area formula:Height*Breadth/2")
        Area=height*breadth/2
        print("Area of Triangle:",Area)
        height1=int(input("Height1:"))
        height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        print("Perimeter formula:Height1+Height2+Breadth")
        perimeter=height1+height2+Breadth
        print("Perimeter of Triangle:",perimeter)
        return Area 








    
                 
   