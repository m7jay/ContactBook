from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for p in params:
            db[p[0]] = p[1]
    else:
        raise Exception('Section {0} not found in {1} file'.format(section, filename))
    return db
