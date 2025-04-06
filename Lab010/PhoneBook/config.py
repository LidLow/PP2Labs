from configparser import ConfigParser

def load_config(filename=r'C:\Users\margo\OneDrive\Рабочий стол\PP2Labs\Lab010\PhoneBook\database.ini', section='postgresql'):
    parser = ConfigParser()

    # Specify UTF-8 encoding when reading the file
    parser.read(filename)
        
    # get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return config

if __name__ == '__main__':
    config = load_config()
    print(config)