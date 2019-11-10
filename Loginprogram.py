f = open("logininfo.txt","a+")
f1 = open("logininfo.txt","r+")
muname = "teryxeon"
mpass = "gvr74z1l"

askMasterUsername = input("Please input master username:\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
askMasterPassword = input("Please input master password:\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
tmuname = askMasterUsername
tmpass = askMasterPassword
if tmuname == muname and tmpass == mpass:
    print("Login successful!")
    question = input("Do you want to add a new account?\n")
    if question == "no" and "No" and "nO" and "NO":
        print("Here are all your logins:\n")
        print(f1.read())
        f1.close()
    elif question == "yes" and "Yes" and "YEs" and "yES" and "yeS" and "YES" and "yEs" and "YeS":
        siteForm = input("Enter the site of the login:\n")
        f.write("Site/Platform: {}\n".format(siteForm))
        emailForm = input("Enter an email:\n")
        f.write("Email: {}\n".format(emailForm))
        usernameForm = input("Enter an username:\n")
        f.write("Username: {}\n".format(usernameForm))
        passwordForm = input("Enter a password:\n")
        f.write("Password: {}\n".format(passwordForm))
        notesForm = input("Enter any other information:\n")
        f.write("Additional notes: {}\n\n".format(notesForm))
        f.close()
else:
    print("Wrong login!")




