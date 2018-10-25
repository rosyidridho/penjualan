from app import app, db_connect
from functools import wraps
from flask import g, session, redirect, url_for, render_template, request
import os
from app.config import GMT
from datetime import datetime, timedelta



def sql_column_builder(data=None):
    """
    '''SQL column builder.
from functools import wraps
    A helper for building column list in SQL syntax from python dict.
    Example:

        data = {'id': 1, 'name': 'example'}

        become:

        id='1', name='example'

    Then it can be used with existing SQL syntax by joining them.
    Example:

        sql = 'INSERT INTO table SET {}'.format(sql_column_builder(data))

    '''
    """
    tmp = []
    for key, value in data.iteritems():
        if isinstance(value, basestring):
            tmp.append("{key}='{value}'".format(key=key, value=value))
        else:
            tmp.append("{key}={value}".format(key=key, value=value))

    column_string = ', '.join(tmp)
    return column_string

class Query:
    def __init__(self, table_name=None):
        self.__tablename__=table_name

    def insert(self, data=None):
        """Insert a record.

        :input: data (dict)
        :output: message berisi pesan sukses (dict)
        :error: message berisi pesan error (dict)
        """
        try:
            sql = "INSERT INTO %s SET id=DEFAULT, %s" % (self.__tablename__, sql_column_builder(data))
            #sql = sql.format(table_name=self.__tablename__, column=sql_column_builder(data))
            g.cursor.execute(sql)
            g.conn.commit()
            return True
        except Exception as e:
            return e

    def get_by(self, operand=None, **kwargs):
        try:
            if (len(kwargs) > 0):
                col = {key: value for key, value in kwargs.iteritems()}
                filter=sql_column_builder(col).replace(', ', ' %s ' % (operand))
                sql = 'SELECT * FROM %s WHERE %s'% (self.__tablename__, filter)
                #sql = sql.format(table_name=self.__tablename__, filter=sql_column_builder(col).replace(', ', ' %s ' % (operand)))
            else:
                sql = "SELECT * FROM %s " % (self.__tablename__)
            g.cursor.execute(sql)
            result = g.cursor.fetchall()
            return result
        except Exception as e:
            return e

    def custom_get_by(self, operand=None, **kwargs):
        try:
            if (len(kwargs) > 0):
                col = {key: value for key, value in kwargs.iteritems()}
                filter=sql_column_builder(col).replace(', ', ' %s ' % (operand))
                sql = 'SELECT * FROM %s WHERE %s order by id desc' % (self.__tablename__, filter)
                #sql = sql.format(table_name=self.__tablename__, filter=sql_column_builder(col).replace(', ', ' %s ' % (operand)))
            else:
                sql = "SELECT * FROM %s order by id desc" % (self.__tablename__)
            g.cursor.execute(sql)
            result = g.cursor.fetchall()
            return result
        except Exception as e:
            return e

    def update(self, data=None):
        """ Update Topic.
        :Update: data (dict)
        :output: message berupa pesan sukses (accepted) > dict
        :error: message berupa pesan error (rejected) > dict
        """
        try:
            col = {key: value for key, value in data.iteritems()}
            sql = "UPDATE %s SET %s WHERE id=%s" % (self.__tablename__, sql_column_builder(col), data['id'])
            #sql = sql.format(
            #    table_name=self.__tablename__, column=sql_column_builder(col), id=data['id']
            #)
            g.cursor.execute(sql)
            g.conn.commit()
            return True

        except Exception as e:
            return e
    
    def delete(self, id):
        try:
            sql = 'DELETE FROM %s WHERE id=%s' % (self.__tablename__, id)
            #sql = sql.format(table_name=self.__tablename__, id=id)
            g.cursor.execute(sql)
            g.conn.commit()
            return True
        except Exception as e:
            return e

    def custom_query(self, sql):
        try:
            g.cursor.execute(sql)
            result = g.cursor.fetchall()
            return result
        except Exception as e:
            return e
    def custom_insert(self, sql):
        try:
            g.cursor.execute(sql)
            g.conn.commit()
            return True
        except Exception as e:
            return e

def waktu_sekarang():
    waktu = datetime.utcnow() + timedelta(hours=GMT)
    return waktu
