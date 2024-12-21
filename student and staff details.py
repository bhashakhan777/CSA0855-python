
def calculate_users():
    
    student_users = int(input("Enter the number of student users in the college: "))
    
     
    total_users = int(input("Enter the total number of users in the college: "))
    
     
    staff_users = total_users - student_users
    
     
    non_teaching_staff_users = staff_users // 3
    

    print(f"Number of student users: {student_users}")
    print(f"Total number of users: {total_users}")
    print(f"Number of staff users: {staff_users}")
    print(f"Number of non-teaching staff users: {non_teaching_staff_users}")


calculate_users()
