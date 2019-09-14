#!/usr/local/bin/python3

#Make sure to set the correct Shebange using 'which python3'

import os
import sys
import sqlite3
import datetime

def log_function(log_entry):
    '''Loggin Function that accepts string, and
    logs to a file and prints'''
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    log_location = os.path.join(dname, 'log.txt')
    log_file = open(log_location, 'a')
    date_time = datetime.datetime.now()
    log_file.write(date_time.strftime("%Y-%m-%d %H:%M:%S") + ' ' + log_entry + '\n')
    log_file.close()
    print(log_entry)

def radarr_database_insert(d):
    '''Radarr Post Processing. Accepts dictionary, and 
    inserts into the sonarr table of the database.db'''

    insert_sql = """INSERT INTO radarr
    (radarr_eventtype,
    radarr_isupgrade,
        radarr_movie_id,
        radarr_movie_title,
        radarr_movie_path,
        radarr_movie_imdbid,
        radarr_moviefile_id,
        radarr_moviefile_relativepath,
        radarr_moviefile_path,
        radarr_moviefile_quality,
        radarr_moviefile_qualityversion,
        radarr_moviefile_releasegroup,
        radarr_moviefile_scenename,
        radarr_moviefile_sourcepath,
        radarr_moviefile_sourcefolder,
        radarr_download_id)
    VALUES () """

    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute(insert_sql, ())
    db.commit()

def sonarr_database_insert(d):
    '''Sonarr Post Processing. Accepts dictionary, and 
    inserts into the sonarr table of the database.db'''

    insert_sql = """INSERT INTO sonarr
    (sonarr_series_type, OS_NAME, sonarr_episodefile_episodeairdates,
    sonarr_episodefile_relativepath, SHELL, sonarr_download_id,
    No_Expand, sonarr_series_id, No_SQLiteXmlConfigFile,
    sonarr_episodefile_releasegroup, sonarr_episodefile_sourcefolder,
    sonarr_eventtype, USER, sonarr_download_client,
    sonarr_episodefile_episodetitles, RUNTIME_VERSION,
    sonarr_episodefile_qualityversion, sonarr_isupgrade,
    sonarr_episodefile_path, PATH, sonarr_series_title,
    PWD, LANG, sonarr_episodefile_episodenumbers,
    sonarr_episodefile_scenename, OS_VERSION,
    sonarr_episodefile_quality, SHLVL, HOME, sonarr_series_tvdbid, 
    sonarr_series_tvmazeid, sonarr_episodefile_id, sonarr_series_path,
    sonarr_episodefile_episodecount, sonarr_episodefile_sourcepath,
    LOGNAME, No_PreLoadSQLite, sonarr_episodefile_seasonnumber,
    sonarr_series_imdbid, sonarr_episodefile_episodeairdatesutc,
    _) 
    VALUES (
    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
    ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
    ?) """
    
    db = sqlite3.connect('database.db')
    cursor = db.cursor()
    cursor.execute(insert_sql, (
            d['sonarr_series_type'],
            d['OS_NAME'],
            d['sonarr_episodefile_episodeairdates'],
            d['sonarr_episodefile_relativepath'],
            d['SHELL'],
            d['sonarr_download_id'],
            d['No_Expand'],
            d['sonarr_series_id'],
            d['No_SQLiteXmlConfigFile'],
            d['sonarr_episodefile_releasegroup'],
            d['sonarr_episodefile_sourcefolder'],
            d['sonarr_eventtype'],
            d['USER'],
            d['sonarr_download_client'],
            d['sonarr_episodefile_episodetitles'],
            d['RUNTIME_VERSION'],
            d['sonarr_episodefile_qualityversion'],
            d['sonarr_isupgrade'],
            d['PATH'],
            d['sonarr_episodefile_path'],
            d['sonarr_series_title'],
            d['PWD'],
            d['LANG'],
            d['sonarr_episodefile_episodenumbers'],
            d['sonarr_episodefile_scenename'],
            d['OS_VERSION'],
            d['sonarr_episodefile_quality'],
            d['SHLVL'],
            d['HOME'],
            d['sonarr_series_tvdbid'],
            d['sonarr_series_tvmazeid'],
            d['sonarr_episodefile_id'],
            d['sonarr_series_path'],
            d['sonarr_episodefile_episodecount'],
            d['sonarr_episodefile_sourcepath'],
            d['LOGNAME'],
            d['No_PreLoadSQLite'],
            d['sonarr_episodefile_seasonnumber'],
            d['sonarr_series_imdbid'],
            d['sonarr_episodefile_episodeairdatesutc'],
            d['_']))
    db.commit()

    
def sonarr_input_from_environment():
    '''Run as Post Processing script from Sonarr, pulls the environmental
    into dictionary, and inserts them into the database'''
    log_function('Sonarr - Reading From Environment Variables')
    d = {'sonarr_series_type' : (os.environ['sonarr_series_type']),
        'OS_NAME': (os.environ['OS_NAME']),
        'sonarr_episodefile_episodeairdates': (os.environ['sonarr_episodefile_episodeairdates']),
        'sonarr_episodefile_relativepath': (os.environ['sonarr_episodefile_relativepath']),
        'SHELL': (os.environ['SHELL']),
        'sonarr_download_id': (os.environ['sonarr_download_id']),
        'No_Expand': (os.environ['No_Expand']),
        'sonarr_series_id': (os.environ['sonarr_series_id']),
        'No_SQLiteXmlConfigFile': (os.environ['No_SQLiteXmlConfigFile']),
        'sonarr_episodefile_releasegroup': (os.environ['sonarr_episodefile_releasegroup']),
        'sonarr_episodefile_sourcefolder': (os.environ['sonarr_episodefile_sourcefolder']),
        'sonarr_eventtype': (os.environ['sonarr_eventtype']),
        'USER': (os.environ['USER']),
        'sonarr_download_client': (os.environ['sonarr_download_client']),
        'sonarr_episodefile_episodetitles': (os.environ['sonarr_episodefile_episodetitles']),
        'RUNTIME_VERSION': (os.environ['RUNTIME_VERSION']),
        'sonarr_episodefile_qualityversion': (os.environ['sonarr_episodefile_qualityversion']),
        'sonarr_isupgrade': (os.environ['sonarr_isupgrade']),
        'sonarr_episodefile_path': (os.environ['sonarr_episodefile_path']),
        'PATH': (os.environ['PATH']),
        'sonarr_series_title': (os.environ['sonarr_series_title']),
        'PWD': (os.environ['PWD']),
        'LANG': (os.environ['LANG']),
        'sonarr_episodefile_episodenumbers': (os.environ['sonarr_episodefile_episodenumbers']),
        'sonarr_episodefile_scenename': (os.environ['sonarr_episodefile_scenename']),
        'OS_VERSION': (os.environ['OS_VERSION']),
        'sonarr_episodefile_quality': (os.environ['sonarr_episodefile_quality']),
        'SHLVL': (os.environ['SHLVL']),
        'HOME': (os.environ['HOME']),
        'sonarr_series_tvdbid': (os.environ['sonarr_series_tvdbid']),
        'sonarr_series_tvmazeid': (os.environ['sonarr_series_tvmazeid']),
        'sonarr_episodefile_id': (os.environ['sonarr_episodefile_id']),
        'sonarr_series_path': (os.environ['sonarr_series_path']),
        'sonarr_episodefile_episodecount': (os.environ['sonarr_episodefile_episodecount']),
        'sonarr_episodefile_sourcepath': (os.environ['sonarr_episodefile_sourcepath']),
        'LOGNAME': (os.environ['LOGNAME']),
        'No_PreLoadSQLite': (os.environ['No_PreLoadSQLite']),
        'sonarr_episodefile_seasonnumber': (os.environ['sonarr_episodefile_seasonnumber']),
        'sonarr_series_imdbid': (os.environ['sonarr_series_imdbid']),
        'sonarr_episodefile_episodeairdatesutc': (os.environ['sonarr_episodefile_episodeairdatesutc']),
        '_' : (os.environ['_'])}
    log_function('Imported Environment Variables for ' + d['sonarr_series_title'])
    sonarr_database_insert(d)


def sonarr_input_from_file(f):
    '''Opens file f, and creates empty dictionary d it then loops through
    the file, splits the line based on the first =, assigns the left to
    Key and the right to Value, then inserts it into the dictionary.
    Returns the TV name as a string'''
    file = open(f, 'r')
    log_function('Opening File - ' + f)
    d = dict.fromkeys(['sonarr_series_type',
                       'OS_NAME',
                       'sonarr_episodefile_episodeairdates',
                       'sonarr_episodefile_relativepath',
                       'SHELL',
                       'sonarr_download_id',
                       'No_Expand',
                       'sonarr_series_id',
                       'No_SQLiteXmlConfigFile',
                       'sonarr_episodefile_releasegroup',
                       'sonarr_episodefile_sourcefolder',
                       'sonarr_eventtype',
                       'USER',
                       'sonarr_download_client',
                       'sonarr_episodefile_episodetitles',
                       'RUNTIME_VERSION',
                       'sonarr_episodefile_qualityversion',
                       'sonarr_isupgrade',
                       'sonarr_episodefile_path',
                       'PATH',
                       'sonarr_series_title',
                       'PWD',
                       'LANG',
                       'sonarr_episodefile_episodenumbers',
                       'sonarr_episodefile_scenename',
                       'OS_VERSION',
                       'sonarr_episodefile_quality',
                       'SHLVL',
                       'HOME',
                       'sonarr_series_tvdbid',
                       'sonarr_series_tvmazeid',
                       'sonarr_episodefile_id',
                       'sonarr_series_path',
                       'sonarr_episodefile_episodecount',
                       'sonarr_episodefile_sourcepath',
                       'LOGNAME',
                       'No_PreLoadSQLite',
                       'sonarr_episodefile_seasonnumber',
                       'sonarr_series_imdbid',
                       'sonarr_episodefile_episodeairdatesutc'],
                       '_')
    for line in file:
        key = line.split("=", 1)[0]
        value = line.split("=", 1)[1]
        value = value.strip('\n')
        d[key] = value
    os.remove(f)
    sonarr_database_insert(d)
    return('Sonarr grabbed ' + str(d['sonarr_series_title']))

if __name__ == "__main__":
    log_function('Pyton: Executing NZBDB Post Processing Script')
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    log_function('Absolute Path Is ' + dname)
    triggers_dir = os.path.join(dname, 'triggers')
    log_function('Trigger Directory is ' + triggers_dir)
    for file_name in os.listdir(triggers_dir):
        if file_name.startswith('sonarr'):
            log_function('Sonarr - Importing Data From Trigger Files')
            sonarr_input_from_file(os.path.join(triggers_dir, file_name))
    if "sonarr_eventtype" in os.environ:
        log_function('Sonarr - Extracting Data From Environment Variables')
        sonarr_input_from_environment()
    elif "radarr_eventtype" is os.environ:
        log_function('Radarr - Extracting Data From Environment Variables')
        radarr_input_from_environment()
    else:
        log_function('No Files or Event Variables Found')
