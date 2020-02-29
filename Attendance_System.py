import os
t = 1
sub = {1: 'Optimisation Technique',2: 'Maths III',3: 'Operating System',4: 'Software Engneering',5: 'Computer Graphics'}
class database:
    def header():
        os.system('cls')
        print('\t\t\t\t\t\t')
        print('\n                                               Alex Mercer ')
        print('\n     -----------------------------------------------------------------------------------------------')
        print('\n')

    def options():
        os.system('cls')
        database.header()
        print('\n 1. Faculty')
        print('\n 2. Warden')
        print('\n 3. Students')
        print('\n 4. Help')
        print('\n 5. Exit')
        try:
            opt = int(input('\n Enter your Option : '))
        except ValueError:
            print('\n Enter the correct Option ')
            database.options()
        database.checker(opt)

    def checkk(x):
        if x == 1:
            user = str(input('\n Enter The Username Provided by the Admin : '))
            pas = str(input('\n Enter The Password Provided By the Admin : '))
            if user == 'admin' and pas == 'password':
                faculty.show()

    def checker(opt):
        if opt == 1:
            database.checkk(1)
        elif opt == 2:
            warden.show()
        elif opt == 3:
            students.show()
        elif opt == 4:
            database.helpp()
        elif opt == 5:
            exit()

    def helpp():
        os.system('cls')
        database.header()
        print("""        Program : Database Management System
        Author  : Alex Mercer
        Mission : To Build a Queality Software Which can help people to get their life better""")
        print('\n\n\n')
        os.system('pause')
        database.options()
        

class students:
    def show():
        os.system('cls')
        database.header()
        print('\n 1. Notice')
        print('\n 2. Attendance')
        print('\n 3. Assignments')
        print('\n 4. Marks')
        print('\n 5. Marks an Issue to the Faculties.')
        print('\n 6. LOGOUT')
        try:
            opt = int(input('\n Enter Your Option : '))
        except ValueError:
            print('\n Enter The Correct Value ')
            students.show()
        database.checker(opt)

    def atte():
        file = open('attandence.txt','r')
        try:
            roll = int(input('\n Enter Your Roll Number : '))
        except ValueError:
            print('\n Enter The Correct Roll Number : ')
        finally:
            students.atte()
        count = 0
        rollno = str(roll)
        for line in file:
            if line == rollno:
                count+=1
        per = count/365
        print('\n Your Attandance is : ',per)

    def assi():
        file = open('assignment.txt','r')
        for line in file:
            print(line)
        file.close()

    def marks():
        try:
            course = str(input('\n Enter Your Course : '))
            year = int(input('\n Enter Your Year : '))
        except ValueError:
            print('\n Enter The Correct Option : ')
        finally:
            students.marks()
        if course == 'BCA':
            if year == 1:
                rollno = input('\n Enter The Roll number : ')
                f = open('BCAstudents1.txt','r')
                for line in f:
                    fo = line.split()
                    if fo:
                        if fo[3] != rollno:
                            print(fo)
                f.close()
            elif year == 3:
                  if year == 1:
                      rollno = input('\n Enter The Roll number : ')
                      f = open('BCAstudents3.txt','r')
                      for line in f:
                          fo = line.split()
                          if fo:
                              if fo[3] != rollno:
                                  print(fo)
                  f.close()
            elif year == 5:
                if year == 1:
                    rollno = input('\n Enter The Roll number : ')
                    f = open('BCAstudents5.txt','r')
                    for line in f:
                        fo = line.split()
                        if fo:
                            if fo[3] != rollno:
                                print(fo)
                f.close()
        elif course == 'BBA':
            if year == 1:
                rollno = input('\n Enter The Roll number : ')
                f = open('BBAstudents1.txt','r')
                for line in f:
                    fo = line.split()
                    if fo:
                        if fo[3] != rollno:
                            print(fo)
                f.close()
            elif year == 3:
                  if year == 1:
                      rollno = input('\n Enter The Roll number : ')
                      f = open('BBAstudents3.txt','r')
                      for line in f:
                          fo = line.split()
                          if fo:
                              if fo[3] != rollno:
                                  print(fo)
                  f.close()
            elif year == 5:
                if year == 1:
                    rollno = input('\n Enter The Roll number : ')
                    f = open('BBAstudents5.txt','r')
                    for line in f:
                        fo = line.split()
                        if fo:
                            if fo[3] != rollno:
                                print(fo)
                f.close()
        elif course == 'BJMC':
            if year == 1:
                rollno = input('\n Enter The Roll number : ')
                f = open('BJMCstudents1.txt','r')
                for line in f:
                    fo = line.split()
                    if fo:
                        if fo[3] != rollno:
                            print(fo)
                f.close()
            elif year == 3:
                  if year == 1:
                      rollno = input('\n Enter The Roll number : ')
                      f = open('BJMCstudents3.txt','r')
                      for line in f:
                          fo = line.split()
                          if fo:
                              if fo[3] != rollno:
                                  print(fo)
                  f.close()
            elif year == 5:
                if year == 1:
                    rollno = input('\n Enter The Roll number : ')
                    f = open('BJMCstudents5.txt','r')
                    for line in f:
                        fo = line.split()
                        if fo:
                            if fo[3] != rollno:
                                print(fo)
                f.close()

    def issue():
        try:
            isu = str(input('\n Enter Your Issue : '))
            roll = int(input('\n Enter Your Roll Number : '))
        except ValueError:
            print('\n Enter The Correct Value : ')
        finally:
            students.issue()
        file = open('issues.txt','a+')
        string = str(roll)+isu
        file.write(string)
        file.close()

    def checker(opt):
        if opt == 1:
            students.notice()
        elif opt == 2:
            students.atte()
        elif opt == 3:
            students.assi()
        elif opt == 4:
            students.marks()
        elif opt == 5:
            students.issue()
        elif opt == 6:
            database.options()

    def notice():
        file = open('notes.txt','r')
        for line in file:
            print(line)
        file.close()

class warden:
    def show():
        os.system('cls')
        database.header()
        print('\n 1. Mark Todays Attandance ')
        print('\n 2. Students at Leave ')
        print('\n 3. Confirm a Students Request for Leave ')
        print('\n 4. LOGOUT')
        try:
            opt = int(input('\n Enter The Choice : '))
        except ValueError:
            print('\n Enter the Correct Option ')
            warden.show()
        warden.checker(opt)

    def checker(opt):
        if opt == 1:
            warden.markatt()
        elif opt == 2:
            warden.stuatleave()
        elif opt == 3:
            warden.confirm()
        elif opt == 4:
            database.options()

    def stuatleave():
        database.header()
        print('\n 1. Confirm a Students request for leave ')
        print('\n 2. Show How Many Students are at Leave ')
        print('\n 3. Search Student By the Roll Number wether he is at leave or not ')
        try:
            opt = int(input('\n Enter Your Option : '))
        except ValueError:
            print('\n Enter the Correct Option : ')
        finally:
            warden.stuatleave()
        if opt == 1:
            warden.confirm()
        elif opt == 2:
            warden.stuatleaveconfirm()
        elif opt == 3:
            warden.stuatleavesearch()

    def confirm():
        os.system('cls')
        database.header()
        try:
            nos = int(input('\n Enter The Number of students to be marked as on leave : '))
        except ValueError:
            print('\n Enter The Correct Value : ')
        finally:
            warden.confirm()
        wnos = 0
        file = open('confirm.txt','a+')
        while wnos <= nos:
            try:
                roll = int(input('\n Enter The Roll Number of the Student : '))
            except ValueError:
                print('\n Enter The Correct Roll Number : ')
            finally:
                warden.markatt()
            wnos+=1
            rollno = str(roll)
            file.write(rollno)
        file.close()

    def stuatleavesearch():
        file = open('confirm.txt','r')
        try:
            roll = int(input('\n Enter The ROll Number To be Searched For : '))
        except ValueError:
            print('\n Enter The Correct Roll number ')
        finally :
            warden.stuatleavesearch()
        rollno = str(roll)
        for line in file:
            if line == rollno:
                print('\n ',rollno,' is at leave')
        else:
            print('\n ',rollno,' is not at leave')

    def stuatleaveconfirm():
        file = open('confirm.txt','r')
        for line in file:
            print('\n ',line,' is at Leave ')
        file.close()

    def markatt():
        os.system('cls')
        database.header()
        try:
            nos = int(input('\n Enter The Number of students to be marked as Present : '))
        except ValueError:
            print('\n Enter The Correct Value : ')
        finally:
            warden.markatt()
        wnos = 0
        file = open('attandence.txt','a+')
        while wnos <= nos:
            try:
                roll = int(input('\n Enter The Roll Number of the Student : '))
            except ValueError:
                print('\n Enter The Correct Roll Number : ')
            finally:
                warden.markatt()
            wnos+=1
            rollno = str(roll)
            file.write(rollno)
        file.close()

class faculty:
    def add_students():
        n = 1
        while n == 1:
            try:
                roll = int(input('\n Enter The Student Roll Number : '))
                name = str(input('\n Enter The Student Name : '))
                course = str(input('\n Enter The Student Course : '))
                sec = str(input('\n Enter The Student Secction : '))
                year = str(input('\n Enter The Student Semester : '))
                mark1 = int(input('\n Enter The Student`s First Subject Marks : '))
                mark2 = int(input('\n Enter The Student`s Second Subject Marks : '))
                mark3 = int(input('\n Enter The Student`s Third Subject Marks : '))
                mark4 = int(input('\n Enter The Student`s Fourth Subject Marks : '))
                mark5 = int(input('\n Enter The Student`s Fifth Subject Marks : '))
            except ValueError:
                print('\n Enter the Correct Value : ')
                faculty.add_students()
            if course == 'BCA':
                if year == '1':
                    f = open("BCAstudents1.txt","a+")
                    data = ['\n Roll Number = ',str(roll),'\t Name : ',name,'\t Section = ',sec,'\t ',sub[1],' = ',str(mark1),'\t ',sub[2],' = ',str(mark2),'\t ',sub[3],' = ',str(mark3),'\t ',sub[4],' = ',str(mark4),'\t ',sub[5],' = ',str(mark5)]
                    f.writelines(data)
                    f.close()
                elif year == '3':
                    f = open("BCAstudents3.txt","a+")
                    data = ['\n Roll Number = ',str(roll),'\t Name : ',name,'\t Section = ',sec,'\t ',sub[1],' = ',str(mark1),'\t ',sub[2],' = ',str(mark2),'\t ',sub[3],' = ',str(mark3),'\t ',sub[4],' = ',str(mark4),'\t ',sub[5],' = ',str(mark5)]
                    f.writelines(data)
                    f.close()
                elif year == '5':
                    f = open("BCAstudents5.txt","a+")
                    data = ['\n Roll Number = ',str(roll),'\t Name : ',name,'\t Section = ',sec,'\t ',sub[1],' = ',str(mark1),'\t ',sub[2],' = ',str(mark2),'\t ',sub[3],' = ',str(mark3),'\t ',sub[4],' = ',str(mark4),'\t ',sub[5],' = ',str(mark5)]
                    f.writelines(data)
                    f.close()
            elif course == 'BBA':
                if year == '1':
                    f = open("BBAstudents1.txt","a+")
                    data = ['\n Roll Number = ',str(roll),'\t Name : ',name,'\t Section = ',sec,'\t ',sub[1],' = ',str(mark1),'\t ',sub[2],' = ',str(mark2),'\t ',sub[3],' = ',str(mark3),'\t ',sub[4],' = ',str(mark4),'\t ',sub[5],' = ',str(mark5)]
                    f.writelines(data)
                    f.close()
                elif year == '3':
                    f = open("BBAstudents3.txt","a+")
                    data = ['\n Roll Number = ',str(roll),'\t Name : ',name,'\t Section = ',sec,'\t ',sub[1],' = ',str(mark1),'\t ',sub[2],' = ',str(mark2),'\t ',sub[3],' = ',str(mark3),'\t ',sub[4],' = ',str(mark4),'\t ',sub[5],' = ',str(mark5)]
                    f.writelines(data)
                    f.close()
                elif year == '5' or year == '6':
                    f = open("BBAstudents5.txt","a+")
                    data = ['\n Roll Number = ',str(roll),'\t Name : ',name,'\t Section = ',sec,'\t ',sub[1],' = ',str(mark1),'\t ',sub[2],' = ',str(mark2),'\t ',sub[3],' = ',str(mark3),'\t ',sub[4],' = ',str(mark4),'\t ',sub[5],' = ',str(mark5)]
                    f.writelines(data)
                    f.close()
            elif course == 'BJMC':
                if year == 1:
                    f = open("BJMCstudents1.txt","a+")
                    data = ['\n Roll Number = ',str(roll),'\t Name : ',name,'\t Section = ',sec,'\t ',sub[1],' = ',str(mark1),'\t ',sub[2],' = ',str(mark2),'\t ',sub[3],' = ',str(mark3),'\t ',sub[4],' = ',str(mark4),'\t ',sub[5],' = ',str(mark5)]
                    f.writelines(data)
                    f.close()
                elif year == '3':
                    f = open("BJMCstudents3.txt","a+")
                    data = ['\n Roll Number = ',str(roll),'\t Name : ',name,'\t Section = ',sec,'\t ',sub[1],' = ',str(mark1),'\t ',sub[2],' = ',str(mark2),'\t ',sub[3],' = ',str(mark3),'\t ',sub[4],' = ',str(mark4),'\t ',sub[5],' = ',str(mark5)]
                    f.writelines(data)
                    f.close()
                elif year == '5' or year == '6':
                    f = open("BJMCstudents5.txt","a+")
                    data = ['\n Roll Number = ',str(roll),'\t Name : ',name,'\t Section = ',sec,'\t ',sub[1],' = ',str(mark1),'\t ',sub[2],' = ',str(mark2),'\t ',sub[3],' = ',str(mark3),'\t ',sub[4],' = ',str(mark4),'\t ',sub[5],' = ',str(mark5)]
                    f.writelines(data)
                    f.close()
            else:
                print("\n Enter The Correct Option :")
            n = int(input('\n Want to Continue : '))
        else:
            faculty.show()

    def show():
        os.system('cls')
        database.header()
        print('\n 1. Add Students')
        print('\n 2. Delete Student')
        print('\n 3. Drop A Note')
        print('\n 4. Drop a Assignment')
        print('\n 5. List All Students')
        print('\n 6. LOGOUT')
        try:
            opt = int(input('\n Enter Your Option : '))
        except ValueError:
            print('\n Enter the Correct Option ')
            faculty.show()
        faculty.checker(opt)

    def delete_students():
        try:
            course = str(input('\n Enter The Student Course : '))
            year = str(input('\n Enter The Student Semester : '))
            if course == 'BCA':
                if year == 1:
                    rollno = input('\n Enter The Roll number : ')
                    f = open('BCAstudents1.txt','r')
                    f1 = open('temp.txt','a+')
                    for line in f:
                        fo = line.split()
                        if fo:
                            if fo[3] != rollno:
                                newline = " ".join(fo) + "\n"
                                #print(newline)
                                f1.write(newline)

                    f.close()
                    f1.close()
                    os.remove('BCAstudents1.txt')
                    os.rename('temp.txt','BCAstudents1.txt')
                elif year == '3':
                    rollno = input('\n Enter The Roll number : ')
                    f = open('BCAstudents3.txt','r')
                    f1 = open('temp.txt','a+')
                    for line in f:
                        fo = line.split()
                        if fo:
                            if fo[3] != rollno:
                                newline = " ".join(fo) + "\n"
                                #print(newline)
                                f1.write(newline)

                    f.close()
                    f1.close()
                    os.remove('BCAstudents1.txt')
                    os.rename('temp.txt','BCAstudents3.txt')
                elif year == 5:
                    rollno = input('\n Enter The Roll number : ')
                    f = open('BCAstudents5.txt','r')
                    f1 = open('temp.txt','a+')
                    for line in f:
                        fo = line.split()
                        if fo:
                            if fo[3] != rollno:
                                newline = " ".join(fo) + "\n"
                                #print(newline)
                                f1.write(newline)

                    f.close()
                    f1.close()
                    os.remove('BCAstudents1.txt')
                    os.rename('temp.txt','BCAstudents5.txt')
            elif course == 'BBA':
                if year == 1:
                    rollno = input('\n Enter The Roll number : ')
                    f = open('BCAstudents1.txt','r')
                    f1 = open('temp.txt','a+')
                    for line in f:
                        fo = line.split()
                        if fo:
                            if fo[3] != rollno:
                                newline = " ".join(fo) + "\n"
                                #print(newline)
                                f1.write(newline)

                    f.close()
                    f1.close()
                    os.remove('BBAstudents1.txt')
                    os.rename('temp.txt','BBAstudents1.txt')
                elif year == 3:
                    rollno = input('\n Enter The Roll number : ')
                    f = open('BBAstudents3.txt','r')
                    f1 = open('temp.txt','a+')
                    for line in f:
                        fo = line.split()
                        if fo:
                            if fo[3] != rollno:
                                newline = " ".join(fo) + "\n"
                                #print(newline)
                                f1.write(newline)

                    f.close()
                    f1.close()
                    os.remove('BBAstudents3.txt')
                    os.rename('temp.txt','BBAstudents3.txt')
                elif year == 5 or year == 6:
                    rollno = input('\n Enter The Roll number : ')
                    f = open('BBAstudents5.txt','r')
                    f1 = open('temp.txt','a+')
                    for line in f:
                        fo = line.split()
                        if fo:
                            if fo[3] != rollno:
                                newline = " ".join(fo) + "\n"
                                #print(newline)
                                f1.write(newline)

                    f.close()
                    f1.close()
                    os.remove('BBAstudents5.txt')
                    os.rename('temp.txt','BBAstudents5.txt')
            elif course == 'BJMC':
                if year == 1:
                    rollno = input('\n Enter The Roll number : ')
                    f = open('BJMCstudents1.txt','r')
                    f1 = open('temp.txt','a+')
                    for line in f:
                        fo = line.split()
                        if fo:
                            if fo[3] != rollno:
                                newline = " ".join(fo) + "\n"
                                #print(newline)
                                f1.write(newline)

                    f.close()
                    f1.close()
                    os.remove('BJMCstudents1.txt')
                    os.rename('temp.txt','BJMCstudents1.txt')
                elif year == 3:
                    rollno = input('\n Enter The Roll number : ')
                    f = open('BJMCstudents3.txt','r')
                    f1 = open('temp.txt','a+')
                    for line in f:
                        fo = line.split()
                        if fo:
                            if fo[3] != rollno:
                                newline = " ".join(fo) + "\n"
                                #print(newline)
                                f1.write(newline)

                    f.close()
                    f1.close()
                    os.remove('BJMCstudents3.txt')
                    os.rename('temp.txt','BJMCstudents3.txt')
                elif year == 5 or year == 6:
                    rollno = input('\n Enter The Roll number : ')
                    f = open('BJMCstudents5.txt','r')
                    f1 = open('temp.txt','a+')
                    for line in f:
                        fo = line.split()
                        if fo:
                            if fo[3] != rollno:
                                newline = " ".join(fo) + "\n"
                                #print(newline)
                                f1.write(newline)

                    f.close()
                    f1.close()
                    os.remove('BJMCstudents5.txt')
                    os.rename('temp.txt','BJMCstudents5.txt')
        except ValueError:
            print('\n Enter The Correct Value : ')
            faculty.delete_students()

    def givenote():
        database.header()
        file = open('notes.txt','w')
        string = str(input('\n Enter Your Note to be read by students : '))
        file.write(string)
        file.close()

    def shownote():
        database.header()
        file = open('notes.txt','r')
        for line in file:
            print(line)
        file.close()

    def assignment():
        try:
            issue = str(input('\n Enter The Issue Date with Format (DD/MM/YYYY) : '))
            sub = str(input('\n Enter The Subject Name : '))
            subm = str(input('\n Enter The Date Of Submission with Format (DD/MM/YYYY) : '))
            task = str(input('\n Enter The Task to be performed in the assignment : '))
        except ValueError:
            print('\n Enter The Correct Value : ')
        finally:
            faculty.assignment()
        new_issue = 'Issue Date : '+issue
        new_subm = 'Date Of Submission : '+subm
        new_sub = 'Subject : '+sub
        new_task = 'Assignment : '+task
        file = open('assignment.txt','a+')
        file.write(new_issue)
        file.write('\n')
        file.write(new_subm)
        file.write('\n')
        file.write(new_sub)
        file.write('\n')
        file.write(new_task)
        file.write('\n')
        file.close()

    def note():
        database.header()
        print('\n 1. Show The Notes')
        print('\n 2. Drop a note')
        try:
            opt = int(input('\n Enter Your Choice : '))
        except ValueError:
            print('\n Enter The Correct Option : ')
        finally:
            faculty.note()
        if opt == 1:
            faculty.shownote()
        elif opt == 2:
            faculty.givenote()
        
                    
    def checker(opt):
        if opt == 1:
            faculty.add_students()
        elif opt == 2:
            faculty.delete_students()
        elif opt == 3:
            faculty.note()
        elif opt == 4:
            faculty.assignment()
        elif opt == 5:
            faculty.showstu()
        elif opt == 6:
            database.options()

database.options()
