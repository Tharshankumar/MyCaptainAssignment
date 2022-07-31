# entering data in csv file
import csv

def write_info_csv(info_list): 
    
    with open('student_info.csv', 'a',newline='')as csv_file: # variable holding file object
        writer = csv.writer(csv_file)

        if csv_file.tell() == 0: # to check whether file is empty or not
            writer.writerow(["Name", "Age", "Contact Number", "E-mail Id"])
        
        writer.writerow(info_list)


if __name__ == '__main__':
    # input
    condition = True
    student_num = 1

    while (condition):
        student_info = input ("Entered student information for student #{} in the following format (Name Age Contact_Number E-mail_Id): ".format(student_num))
        
        #split
        student_info_list = student_info.split('  ')
        print("\n The entered information is-\nName: {}\nAge: {}\nContact_Number: {}\nE-mail_Id: {}"
              .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))
      
        choice_check = input("Is the entered information correct ? (yes/no) : ")

        if choice_check == "yes":
            write_info_csv(student_info_list)

            condition_check = input("Enter (yes/no) if you wnt to enter information for another student: ")
            if condition_check == "yes":
                condition = True
                student_num = student_num + 1

            elif  condition_check== "no":
                condition = False
        elif choice_check == "no" :
            print("Please re-enter the values!")