sql_db_exists = '''select exists(
            SELECT datname FROM pg_catalog.pg_database WHERE lower(datname) = lower('ContactBook')
            );'''

sql_select_all = '''select * from contacts;'''

sql_delete_all = '''delete from contacts;'''

sql_create_table = '''create table contacts (
                        id serial primary key,
                        name varchar(50) unique not null,
                        ext  varchar(5)[],
                        num  varchar(10)[]
                    );'''

sql_remove_table = '''drop table contacts;'''

sql_end_transaction = '''end;'''

sql_create_db = '''create database contactbook;'''

sql_delete_db = '''drop database contactbook;'''

def sql_insert_contact(name,exts, nums):
    q = "insert into contacts(name, ext, num) values('" + name + "', '{"
    num_exts = len(exts)-1
    len_nums = len(nums)-1
    for i, e in enumerate(exts):
        if i == num_exts:
            q += '"' + e + '"' + "}', '{"
        else:
            q += '"' + e + '"' + ", "
    for i, n in enumerate(nums):
        if i == len_nums:
            q += '"' + n + '"' + "}');"
        else:
            q += '"' + n + '"' + ","    
    return q

def sql_delete_contact(name):
    q = "delete from contacts where name='" + name + "';"
    return q

#select * from contacts;
#insert into contacts(name, ext, num) values('Jay', '{"+91"}', '{"9876543210"}') returning id;
#select * from contacts;
#drop table contacts;
#create table contacts (
#	id serial primary key,
#	name varchar(50) unique not null,
#	ext  varchar(5)[],
#	num  varchar(10)[]
#);
#select * from contacts;
#insert into contacts(name, ext, num) values('Jay', '{"+91"}', '{"9876543210"}');
#
#select * from contacts;
#delete from contacts where name='Sai';
#select * from contacts;
