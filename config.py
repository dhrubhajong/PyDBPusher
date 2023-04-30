from configparser import ConfigParser

def config(filename="database.ini",section="postgresql"):
    # Create a parser
    parser=ConfigParser()
    # read the config file
    parser.read(filename)
    db={}
    if parser.has_section(section):
        params=parser.items(section)
        for i in params:
            db[i[0]]=i[1]
    else:
        raise Exception('Section{0}is not found in the {1} file'.format(section,filename))
    return db    

    print(db)

    config()    