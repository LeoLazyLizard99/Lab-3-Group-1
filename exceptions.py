def read_file(file):
        
    try:
        f = open(f"{file}.csv", 'r')

    except IOError:
        print("Input/Output error")

    except FileNotFoundError:
        print("The file 'country_full.csv' was not found.")

    except PermissionError:
        print("I do not have permission to access this file.")