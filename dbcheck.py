import subprocess
import os

def dbexists():
#    subprocess.run(["psql", "-U", "postgres", "-l", "|", "grep", "'ContactBook'", "|", "wc", "-l"])
    res = os.system("psql -U postgres -l | grep 'ContactBook' | wc -l")
    if res == 0:
        print("Database does not exists!.")
        print("Ceating a new ContactBook db...")
        os.system("psql -U postgres")
        print("create database ContactBook;")
    
def dbexists2():
#    res = subprocess.run(["psql", "-U", "postgres"], stdout = subprocess.PIPE, text=True)
#    print(res.stdout)
    res = subprocess.run(["psql", "-U", "postgres", "select exists(", "SELECT", "datname", "FROM", "pg_catalog.pg_database", 
            "WHERE", "lower(datname)", "=", "lower('ContactBook'));"], stdout=subprocess.PIPE, text=True)
    print(res.stdout)

if __name__ == "__main__":
    dbexists()