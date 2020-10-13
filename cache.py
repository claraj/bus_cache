import sqlite3 
import time 
from datetime import datetime 

database = 'bus_cache.db'

con = sqlite3.connect(database)
con.execute('create table if not exists bus_cache (identifier text unique, expiration integer, json text)')
con.commit()
con.close()


def add(cachable):

    # store thing in cache 
    # overwrite if thing with identifier already in cache

    json_string = cachable.to_json()

    print('This item expires at', cachable.expiration, 'as a date,', datetime.fromtimestamp(cachable.expiration))

    with sqlite3.connect(database) as con:
        con.execute('delete from cache where identifier = ?', (cachable.identifier, ))
        con.execute('insert into cache (identifier, expiration, json) values (?, ?, ?)', (cachable.identifier, cachable.expiration, json_string) )
    con.close()


def fetch(identifier, cls):
    
    now = time.time()

    with sqlite3.connect(database) as con:
        con.row_factory = sqlite3.Row

        # Fetch result for this identifier but only if it is not expired
        result = con.execute('select * from cache where identifier = ? and expiration > ?', (identifier, now) )
        cached_row = result.fetchone()
    
        if not cached_row:
            cached_object = None 
        else:
            cached_object = cls.load_from_cache(cached_row['json'], cached_row['identifier'], cached_row['expiration'])

    con.close()

    return cached_object


