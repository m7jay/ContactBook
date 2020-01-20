import dbops as db
import sqlcmds as sql
import re

class contactbook(object):
    def __init__(self):
        self.conn = db.connectdb('postgres')
        if not (db.execute_sql(self.conn, sql.sql_db_exists, fetch=True)[1][0][0]):
            print("Contact book db does not exists, creating a new one now...")
            self.conn.autocommit = True
            db.execute_sql(self.conn, sql.sql_create_db)
            self.conn = db.connectdb()
            db.execute_sql(self.conn, sql.sql_create_table)
        else:
            print("contactbook db exists, connecting...")
            self.conn = db.connectdb()
        self.conn.autocommit = True

    def displaycontacts(self):
        data = db.execute_sql(self.conn, sql.sql_select_all, fetch=True)
        print(".......................................................................................")
        print("%5s%50s\t%5s\t%10s"%("Contact ID", "Contact Name", "Ext", "Contact Number"))
        for row in data[1]:
            print('\n')
            print("%5s %50s"%(row[0], row[1]), end="\t")
            ext = row[2]
            num = row[3]
            for i, e in enumerate(ext):
                if i == 0:
                    print("%5s\t%10s"%(e, num[i]))
                else:
                    print("%5s %50s\t%5s\t%10s"%(" ", " ", e, num[i]))
        print(".......................................................................................")

    def insertrow(self, name, exts, nums):
        db.execute_sql(self.conn, sql.sql_insert_contact(name, exts, nums))

    def deletecontact(self, name):
        db.execute_sql(self.conn, sql.sql_delete_contact(name.upper()))
        self.conn.commit()
        print(name, " record deleted.")

    def deleteall(self):
        db.execute_sql(self.conn, sql.sql_delete_all)
        print("All contact records deleted.")

    def resetdb(self):
        db.execute_sql(self.conn, sql.sql_remove_table)
        db.execute_sql(self.conn, sql.sql_create_table)
        print("Contact Book reset.")

    def deletedb(self):
        self.conn = db.connectdb('postgres')
        self.conn.autocommit = True
        db.execute_sql(self.conn, sql.sql_delete_db)
        print("contactbook db deleted.")
        exit()

    def closecontactbook(self):
        db.closedb(self.conn)

def main():
    cb = contactbook()
    instructions = "\n 1. Display all contacts\n 2. Insert a contact\n 3. Delete a contact\n 4. Delete all\n 5. Reset DB\n 6. Delete database\n-1. Exit"
    choice = 0

    while choice != -1:
        print(instructions)
        print('Enter your choice:', end='')
        choice = int(input())
    
        if choice == 1:
            cb.displaycontacts()

        elif choice == 2:
            print('Enter the contact name:', end='')
            name = input().upper()
            print('Enter extensions followed by the contact number, ex: +91 1234567890.')
            line = input()
            exts = []
            nums = []
            while line:
                line = list(line.split())
                exts.append(line[0])
                nums.append(line[1])
                line = input()
            cb.insertrow(name, exts, nums)
    
        elif choice == 3:
            print('Enter the name of the contact to delete: ', end='')
            name = input()
            cb.deletecontact(name)
    
        elif choice == 4:
            cb.deleteall()
    
        elif choice == 5:
            if re.search('[yes|y|ye]', input("Resetting will delete all the data, please type Yes to continue:").lower()):
                cb.resetdb()
    
        elif choice == 6:
            if re.search('[yes|y|ye]', input("please type Yes to continue:").lower()):
                cb.deletedb()

    cb.closecontactbook()

if __name__ == "__main__":
    main()
