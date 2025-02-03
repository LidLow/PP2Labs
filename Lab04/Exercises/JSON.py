import os
import json

os.chdir(r"C:\Users\margo\OneDrive\Рабочий стол\PP2Labs\Lab04\Exercises") #sample.json and main.py are should be located in same directory; Hint: StackOverFlow

initialFile = open("sample.json", "r")
jsonSample = json.loads(initialFile.read())

connectionIDList = set() #set with id's


#getting the id's from the sample
def listOfConnections():
    print("", "Available Connections:", sep="\n")

    for dict in jsonSample["imdata"]:                                           #loop through list "imdata"
        for key in dict["l1PhysIf"]["attributes"]:                              #loop through dictionary -> "l1PhysIf" -> "attributes"
            if key == "id":
                print(dict["l1PhysIf"]["attributes"][key])                      #printing every ID

    return mainMenu()


#adding connections to the list by their id
def addConnection():                                                        
    ID = input("\nEnter the No. of the Connection: ")
    global connectionIDList

    for dict in jsonSample["imdata"]:                                           #loop through list "imdata"
        for key in dict["l1PhysIf"]["attributes"]:                              #loop through dictionary -> "l1PhysIf" -> "attributes"
            if key == "id" and "eth1/" + ID == dict["l1PhysIf"]["attributes"][key]:       #searches for the key "id" and if ["id"] == ID, then adds it to the list
                connectionIDList.add(dict["l1PhysIf"]["attributes"][key])
                print("Connected succesfully")
                return mainMenu()
               
    print("There is no such Connection")
    return mainMenu()


#clears the list of connections
def dropConnections():
    global connectionIDList
    connectionIDList.clear()

    return mainMenu()


#interface of connections
def currentConnections():
    print("\nInterface Status")
    print("======================================================================================")
    print("DN                                                  Description         Speed     MTU")
    print("--------------------------------------------------  ------------------  --------  ----")

    for ID in connectionIDList:
        for dict in jsonSample["imdata"]:                                              #loop through list "imdata"
            for key in dict["l1PhysIf"]["attributes"]:                                 #loop through dictionary -> "l1PhysIf" -> "attributes"
                if key == "id" and ID in dict["l1PhysIf"]["attributes"][key]:          #searching for the key "id" and the ["id"] = ID value
                    print(dict["l1PhysIf"]["attributes"]["dn"], "                            ", dict["l1PhysIf"]["attributes"]["speed"], " ", dict["l1PhysIf"]["attributes"]["mtu"])
                    
    return mainMenu()         
   

#just a menu with some options
def mainMenu():                                                                                         
    print("", "Choose the option:", "1. Input Connection's ID", "2. Get list of Connections", "3. Connect to the Network", "4. Drop the Connection", "5. Exit the System", sep="\n")
    option = input("Enter: ")

    if option == "1":     
        addConnection()
    elif option == "2":
        listOfConnections()
    elif option == "3":
        currentConnections()
    elif option == "4":
        dropConnections()
    elif option == "5":
        initialFile.close()
        exit()
    else:
        mainMenu()


#Start
mainMenu() 