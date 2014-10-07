import os
import sys
import sqlite3

class Session():

    _SQL_CREATE_TABLE = (
        """
        CREATE TABLE IF NOT EXISTS session
        (
            access_token TEXT,
            client_id TEXT,
            expiry BIGINT
        )
        """
    )
    _SQL_CREATE  = 'INSERT INTO session VALUES (?,?,?)'
    _SQL_DELETE  = 'DELETE FROM session WHERE client_id = ?'
    _SQL_GET     = 'SELECT * FROM session WHERE client_id = ?'

    _SESSION_PATH   = '/log/'
    _DB_NAME        = 'acsession.db'

    def __init__(self, client_id):
        self.new        = False
        self.conn       = None
        self.path       = os.path.dirname(os.path.realpath(__file__)) + self._SESSION_PATH 
        self.db         = self._DB_NAME
        self.client_id  = client_id

        """ Create db if file doesn't exist """
        if not os.path.exists( self.path+self.db ):
            with self.dbconn() as conn:
                conn.execute( self._SQL_CREATE_TABLE )
                self.new = True

    def dbconn(self):
        """ Database connection """
        if not self.conn:
            self.conn = sqlite3.Connection( self.path+self.db )
        return self.conn

    def get(self,client_id):
        """ Get session data """
        conn = self.dbconn().cursor()
        conn.execute( self._SQL_GET,(client_id,) )
        return conn.fetchone()

    def create(self,data):  
        # os.chmod(self.path + self.db, 777)
        """ Create session data """      
        with self.dbconn() as conn:
            conn.execute(self._SQL_DELETE,( self.client_id,) )
            conn.execute(self._SQL_CREATE,(data['access_token'], self.client_id, data['expires']))
            self.conn.commit()