class User :
    #create account
    users=[{'User Name': 'asif', 'User E-Mail': 'asif_mahim58@gmail.com', 'Adress': 'Bogura', 'account_type': 'Savings', 'Balance': 0, 'total_lone_time': 0,'last_deposit':0,'last_withdraw':0 ,'ID': 101},{'User Name': 'parvez', 'User E-Mail': 'parvez_mahim58@gmail.com', 'Adress': 'Dhaka', 'account_type': 'Savings', 'Balance': 230, 'total_lone_time': 1,'last_deposit':0 , 'last_withdraw':0, 'ID': 102}]
    user_info={}
    user_emails_for_check_existance_of_account=["asif_mahim58@gmail.com","parvez_mahim58@gmail.com"]
    user_id_for_check_existance_of_account=[101,102]
    def __init__(self,name,email,adress,account_type) -> None:
        
        self.name=name
        User.user_info["User Name"]=self.name
        self.email=email
        User.user_info["User E-Mail"]=self.email
        User.user_emails_for_check_existance_of_account.append(self.email)
        self.adress=adress
        User.user_info["Adress"]=self.adress
        self.account_type=account_type
        User.user_info["account_type"]=self.account_type
        User.user_info["Balance"]=0
        User.user_info["total_lone_time"]=0
        User.user_info["last_deposit"]=0
        User.user_info["last_withdraw"]=0
        User.users.append(User.user_info)
        
        

    def id_generate():
        id=100+len(User.users)
        print(f'Your ID is : {id}')
        User.user_info["ID"]=id
        User.user_id_for_check_existance_of_account.append(id)
        # print (User.users)

    def valid_id_or_not(id):
        flag=0
        for userId in User.user_id_for_check_existance_of_account:
            if id==userId:
                flag=1
                break
        if (flag==1):
            return True
        else:
            return False


    def deposite_amount(id,amount):
        id=int(id)
        isIdValidOrNot=User.valid_id_or_not(id)
        if (isIdValidOrNot==False):
            print("Invalid ID")
        else:
            user_index=id-101
            user_profile=User.users[user_index]
            user_profile["Balance"]+=amount
            Admin.bank_details["Total Balance"]+=amount
            print(f'Congratulations !!! {amount} taka is added On Your Account')
            print(f'Your Current Amount is : {user_profile["Balance"]}')
            user_profile["last_depo"]=amount

    def withdrow_amount(id,amount):
        id=int(id)
        isIdValidOrNot=User.valid_id_or_not(id)
        if (isIdValidOrNot==False):
            print("Invalid ID")
        else:
            user_index=id-101
            user_profile=User.users[user_index]
            
            if(Admin.bank_details["Total Balance"]<amount):
                print("Bank is Bankrupt")    

            elif(user_profile["Balance"]<amount):
                print("Not Enough Balance")
                user_profile["last_with"]=user_profile["last_with"]
            else:
                user_profile["Balance"]-=amount
                Admin.bank_details["Total Balance"]-=amount
                print(f"You Have Successfully Withdrow {amount} taka")
                print(f'Current Balance is :{user_profile["Balance"]}')
                user_profile["last_with"]=amount

        
    
    def chk_balance(id):
        id=int(id)
        isIdValidOrNot=User.valid_id_or_not(id)
        if (isIdValidOrNot==False):
            print("Invalid ID")
        else:
            user_index=id-101
            user_profile=User.users[user_index]
            print(f'Your Balance is : {user_profile["Balance"]}')

    def transation_history(id):
        id=int(id)
        isIdValidOrNot=User.valid_id_or_not(id)
        if (isIdValidOrNot==False):
            print("Invalid ID")
        else:
            user_index=id-101
            user_profile=User.users[user_index]
            print("Transation History : ")
            print(f'Your Last Deposite : {user_profile["last_depo"]}')
            print(f'Your Last Withdrow : {user_profile["last_with"]}')
       
    def take_lone():
        id=int(id)
        if(Admin.loan_feature[0]=="ON"):
            id=int(input("Enter Your ID : "))
            isIdValidOrNot=User.valid_id_or_not(id)
            if (isIdValidOrNot==False):
                print("Invalid ID")
            else:
                lone_amount=int(input("Enter Loan Amount : "))
                user_index=id-101
                user_profile=User.users[user_index]
                if (Admin.bank_details["Total Balance"]<lone_amount):
                    print("Bank is Bankrupt")
                if (user_profile["total_lone_time"]==2):
                    print("You Have Already Taken Loan for 2 Times. So This Feature is Off For You")
                else:
                    print(f'Previous Loan Taken For : {user_profile["total_lone_time"]} Time')
                    Admin.bank_details["Total Balance"]-=lone_amount
                    user_profile["total_lone_time"]+=1
                    Admin.bank_details["Total Loan Given"]+=lone_amount
                    print(f'Total Loan Taken For : {user_profile["total_lone_time"]} Time')
                    print(f'{lone_amount} taka is Granted For Loan')
        else:
            print("Loan Feature is Currently OFF")
    
    def transfer_system(senderId,recieverId,senderAmount):
        validity_of_sender_id = User.valid_id_or_not(senderId)
        validity_of_reciever_id = User.valid_id_or_not(recieverId)
            
        if (validity_of_sender_id==True and validity_of_reciever_id==True):
            sender_index=senderId-101
            reciever_index=recieverId-101
            sender_profile=User.users[sender_index]
            reciever_profile=User.users[reciever_index]
            if (sender_profile["Balance"]>senderAmount):
                
                sender_profile["Balance"]-=senderAmount
                reciever_profile["Balance"]+=senderAmount
                print ("Transfer is Completed")
                print(f'Current Balance of Sender (ID : {senderId}) is : {sender_profile["Balance"]} and Current Balance of Reciever (ID : {recieverId}) is : {reciever_profile["Balance"]}')           
            else:
                print("You Have Not Sufficient Ammount")
        else:
            print("Invalid Id")


        
class Admin (User):
    admin_record={"1001":"shahrukh@gmail.com","1002":"gouri@gmail.com"}
    bank_details={"Name": "ADVANCE Bank","Total Balance":2000000,"Total Loan Given": 0}
    loan_feature=["ON"]
    
    def delete_user_account(id):
        validOrNot=User.valid_id_or_not(id)
        if validOrNot!=True:
            print("ID is Not Valid")
        else:
            # print("ID is Valid")
            user_profile=User.users[id-101]
            del User.users[id-101]
            # print(User.users)
            print (f'{id} is successfully deleted from User List')

    def view_users():
        for user in User.users:
            print(user)

    def remaining_bank_balance():
        print(Admin.bank_details["Total Balance"])

    def total_loan_given():
        print("Amount of Total Given Loan : ",Admin.bank_details["Total Loan Given"])
    
    def control_loan_feature(cntrlSignal):
        if (cntrlSignal==1):
            Admin.loan_feature.clear()
            Admin.loan_feature.append("ON")
        elif (cntrlSignal==2):
             Admin.loan_feature.clear()
             Admin.loan_feature.append("OFF")
        print("Loan Feature is Controlled")
        print ("The Feature is",Admin.loan_feature[0],"Now")




        



    

"""
Replica
"""
print("WELCOME TO ADVANCED BANK !!!")
while(1):
    print ("Chose Your Option - ")
    print("1. Admin\n2. User\n3. Exit")
    user_choice=int(input("Enter Your Choice : "))
    if user_choice==2:
            print("1. Log In")
            print("2. Sign In")
            print("3. Exit")

            input_choice=int(input("Chose Option : "))

            if (input_choice==1):         
                mail_chk=input("Enter Your E-Mail : ")
                flag=0
            
                for valid_mail in User.user_emails_for_check_existance_of_account:
                    if (valid_mail==mail_chk):
                        flag+=1
                        break
                if (flag ==0 ):
                    print("Invalid E-Mail")

                else:
                    while(1):
                        print("Chose Your Option")
                        print("1. Deposite Amount : ")
                        print("2. Withdrow Amount")
                        print("3. Check Balance")
                        print("4. Check Transaction History")
                        print("5. Take Loan")
                        print("6. Transfer Amount")
                        print("7. Go To Main Menu")
                        take_input=int(input("Enter Choice : "))

                        #ekhan theika star hobe
                        if take_input==1:
                            id=int(input("Enter Your ID : "))
                            amount=int(input("Enter The Amount you Want To Deposit : "))
                            User.deposite_amount(id,amount)

                        elif take_input==2:
                            id=int(input("Enter Your ID : "))
                            amount=int(input("Enter The Amount you Want To Withdrow : "))
                            User.withdrow_amount(id,amount)

                        elif take_input==3:
                            id=int(input("Enter Your ID : "))
                            User.chk_balance(id)

                        elif take_input==4:
                            id=int(input("Enter Your ID : "))
                            User.transation_history(id)
                        
                        elif take_input==5:
                            User.take_lone()

                        elif take_input==6:
                            id1=int(input("Enter Sender ID: "))
                            id2=int(input("Enter Reciever ID: "))
                            sending_amount=int(input("Enter Amount: "))
                            User.transfer_system(id1,id2,sending_amount)

                        elif take_input==7:
                            break
                        else:
                            print("Enter a Valid Number")

                        
            elif input_choice==2:
                sign_flag=0
                name=input("Enter Your Name Here : ")
                email=input("Enter Your E-Mail Here : ")
                for email_exist in User.user_emails_for_check_existance_of_account:
                    if (email==email_exist):
                        sign_flag=1
                        break
                if (sign_flag==0):
                        adress=input("Enter Your Adress : ")
                        print("Chose Your Account_Type")
                        print("Press 1 for Savings")
                        print("Press 2 for Current")
                        account_type_choice=int(input("Enter Your Account Type Option : "))
                        if account_type_choice==1:
                            account_type="Savings"
                        elif account_type_choice==2:
                            account_type="Current"
                        else:
                            print("Enter a Valid Account Type")
                        User(name,email,adress,account_type)
                        print("Congratulations !!!! Successfully Sign-In Completed")
                        User.id_generate()
                        # print(f'Your ID is : {100+len(User.users)}')
                else:
                    print(f'{email} This Email is Already Exist.')

            elif (input_choice==3):
               exit()
            else:
              print("Enter a Valid Choice")
    
    elif user_choice==1:
        print("ADMIN PANEL->")
        print("E-Mail : shahrukh@gmail.com , ID: 1001\nE-Mail : gouri@gmail.com , ID: 1002")
        validFlag=0
        mail=input("Enter Your E-Mail : ")
        id=int(input("Enter Your ID : "))
        for key in Admin.admin_record.keys():
            if (int(key)==id and Admin.admin_record[key]==mail):
                validFlag+=1
                break
            else:
                validFlag=0
    
    
        if (validFlag!=0):
            while(1):
                print("1. Create an User Account")
                print("2. Delete A User")
                print("3. All User List")
                print("4. Total Available Balance of The Bank")
                print("5. Total Loan Given")
                print("6. Control Loan Feature")
                print("7. Go To Main Menu")
                choice_admin=int(input("Enter Your Choice : "))
                #kaj starter
                if choice_admin==1:
                    name=input("Enter User Name : ")
                    mail=input("Enter User E-Mail : ")
                    email_exist_flag=0
                    for email_exist in User.user_emails_for_check_existance_of_account:
                            if (mail==email_exist):
                                email_exist_flag+=1
                                break
                    if email_exist_flag!=0:
                        print(f'{mail} This Email is Already Exist.')


                    else:
                        adress=input("Enter Your Adress : ")
                        print("Chose Your Account_Type")
                        print("Press 1 for Savings")
                        print("Press 2 for Current")
                        account_type_choice=int(input("Enter Your Account Type Option : "))
                        if account_type_choice==1:
                            account_type="Savings"
                        elif account_type_choice==2:
                            account_type="Current"
                        else:
                            print("Enter a Valid Account Type")
                        User(name,mail,adress,account_type)
                        User.id_generate()
                        print("Congratulations !!!! Successfully Created User Account")
                        print(f'User ID is : {100+len(User.users)}')

                elif choice_admin==2:
                    id=int(input("Enter The User ID which is Need to Delete : "))
                    Admin.delete_user_account(id)
                
                elif choice_admin==3:
                    Admin.view_users()
                
                elif choice_admin==4:
                    Admin.remaining_bank_balance()

                elif choice_admin==5:
                    Admin.total_loan_given()

                elif choice_admin==6:
                    print("1. ON Loan Feature")
                    print("2. OFF Loan Feature")
                    cntrlSignal=int(input("Enter Your Choice : "))
                    Admin.control_loan_feature(cntrlSignal)

                elif choice_admin==7:
                    break
                else:
                    print("Choose a Valid Key")
        
        else:
            print("Invalid Admin")

    elif user_choice==3:
        exit()
    else:
        print("Enter a Valid Key")
            
        
            

                        
            