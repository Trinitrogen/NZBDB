import os
import NZBDB

def set_sonarr_variables(file_name):
    '''Receives Path to File and Opens it, scans
    line by line. Sets environment varibles with the contents'''
    file = open(file_name, 'r')
    for line in file:
        key = line.split("=", 1)[0]
        value = line.split("=", 1)[1]
        value = value.strip('\n')
        os.environ[key] = value

if __name__ == "__main__":
    '''Background Function That Checks if certain trigger files
    are present. '''
    triggers_dir = os.path.join(os.getcwd(), 'triggers')
    for file_name in os.listdir(triggers_dir):
        if file_name.startswith('environ'):
            set_sonarr_variables(os.path.join(triggers_dir, file_name))
            NZBDB.sonarr_input_from_environment()