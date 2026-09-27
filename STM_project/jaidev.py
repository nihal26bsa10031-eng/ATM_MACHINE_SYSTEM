print("===========WELOME TO THE STUDENT MANAGEMENT PORTAL=======================")
print("--------------------------------------------")

print("------------------------------------------")
print("============================================================================")

print("")

students = [ ]
print("")
def add_student ( ):
    print("               \n- - - - - ADD STUDENT - - - - - ")
    roll_no = input("     Enter Roll Number : ")
    name =   input("    Enter Student Name : ")
    age =      input("     Enter Age :")
    course = input("     Enter Course : ")
    student = { "roll_no" : roll_no, "name": name, "age": age, "course": course } 
    students.append(student)
     
    print( " Student  added successfully !")
     
print("")     
def view_student ( ):
    print( " \n - - - - - ALL STUDENT - - - - -")
  
    print("")    
      
          
    if len( students) == 0 :
         print( " No student record found.")
        
    else : 
        
        for student in students :
            
            print("- - - - - - - - - - - - - - - - - - - - - - - - - - - -  " )
            print("Roll Number :"  , student[ "roll_no"] )
            print( " Name          :"  , student["name"] )
            print( "Age               :"  , student[ "age" ] )
            print( "course          :"  , student[ "course" ] )
            
            
           
def search_student ():
            
            print ( "\n- - - - - SEARCH STUDENT - - - - - ")
            
            roll_no = input("Enter Roll Number : ")
            
            for student in students :
                
                if student["roll_no"] == roll_no:
                    print("\nStudent Found !")
                    print("Roll Number : " , student["roll_no"])
                    print("Name            :"  , student["name"])
                    print("Age                :"  , student[ "age"])
                    print("course           :"  , student["course"])
                    
                    return
                    
                print("student not found. ")
               
               
def delete_student() :
                    
                    
        print("\n----- DELETE STUDENT -----")
        
        print("")

        roll_no = input("Enter Roll Number: ")

        for student in students:

              if student["roll_no"] == roll_no:

                  students.remove(student)

                  print("Student deleted successfully!")

                  return

        print("Student not found.")


def main() : 
       
     while True:

        print("\n================================")
        print("    STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")
        print("================================")
        print("")
        print("")

        choice = input("Enter your choice: ")
        
        if choice == "1":

            add_student()

        elif choice == "2":
            
            view_student()

        elif choice == "3":
            search_student()

        elif choice == "4":

            delete_student()

        elif choice == "5":

            print("\nThank you for using the system!")
            break

        else:

            print("\nInvalid choice!")
            print("")
            print("")
            print("×××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××")





main()