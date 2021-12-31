import copy
import os
import time

import mysql.connector as sql

import Component
import ComponentHtml
import ComponentListHtml
import Services
import componentList
import model


class Main2:
    def __init__(self):
        self.database = input("Database Name: ")
        self.databaseHost = input("Database Host: ")
        self.databaseUser = input("Database User: ")
        self.databasePassword = input("Database Password: ")
        self.path = input("Full path of Location Folder: ")
        self.projectname = input("Project Name: ")

        # self.database = "ag"
        # self.databaseHost = "localhost"
        # self.databaseUser = "root"
        # self.databasePassword = "ayushaher"
        # self.path = "G:\\testing\\Automation"
        # self.projectname = "AG"

        self.projectname = f"{self.projectname}UI"

        try:
            db = sql.connect(
                host=self.databaseHost,
                user=self.databaseUser,
                password=self.databasePassword,
                auth_plugin='mysql_native_password',
            )

            self.mycursor = db.cursor()
            self.mycursor.execute("SHOW DATABASES")
            lstdatabase = self.mycursor.fetchall()
            databaseExists = False

            for database in lstdatabase:
                if self.database in database:
                    databaseExists = True

            if databaseExists:
                self.mycursor.execute(f"USE {self.database}")
                if not os.path.exists(f"{self.path}/{self.projectname}"):
                    os.mkdir(f"{self.path}/{self.projectname}")

                if not os.path.exists(f"{self.path}/{self.projectname}/Components"):
                    os.mkdir(f"{self.path}/{self.projectname}/Components")
                self.CreateContext()

            else:
                print("Database Does Not Exists")

        except Exception:
            print("Error Occurred", Exception)

    def CreateContext(self):
        columnlist = []

        self.mycursor.execute("SHOW TABLES")

        for table in self.mycursor.fetchall():
            table = str(table).replace("(", "").replace("'", "").replace(",", "").replace(")", "").title()
            self.mycursor.execute(f"show columns from `{table}`")
            lstColumns = self.mycursor.fetchall()

            for columns in lstColumns:
                columnlist.append(list(columns[0:2]))
            #     takes only field name and datatype from list

            ListColumns = copy.deepcopy(columnlist)
            ListModel = copy.deepcopy(table)

            ListColumns0 = copy.deepcopy(columnlist)
            ListModel0 = copy.deepcopy(table)

            ListColumns1 = copy.deepcopy(columnlist)
            ListModel1 = copy.deepcopy(table)

            ListColumns2 = copy.deepcopy(columnlist)
            ListModel2 = copy.deepcopy(table)

            ListColumns3 = copy.deepcopy(columnlist)
            ListModel3 = copy.deepcopy(table)

            ListColumns4 = copy.deepcopy(columnlist)
            ListModel4 = copy.deepcopy(table)

            Component.Component(self.projectname, self.path, ListColumns, ListModel)
            Services.Services(self.projectname, self.path, ListColumns0, ListModel0)
            model.Model(self.projectname, self.path, ListColumns1, ListModel1)
            componentList.ComponentList(self.projectname, self.path, ListColumns2, ListModel2)
            ComponentListHtml.ComponentListHtml(self.projectname, self.path, ListColumns3, ListModel3)
            ComponentHtml.ComponentHtml(self.projectname, self.path, ListColumns4, ListModel4)

            columnlist.clear()


if __name__ == "__main__":
    try:
        start = time.time()
        Main2()
        end = time.time()
        totaltime = round(float(end - start), 4)
        print(f"Eclipse Time: {totaltime}")
    except Exception as e:
        print(f"Error:{e}")
