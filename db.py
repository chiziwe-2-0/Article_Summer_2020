import psycopg2
import psycopg2.extras


class Db(object):

    _instance = None
    _connection = None

    def __new__(cls, **kwargs):
        if Db._instance is None:
            Db._instance = object.__new__(cls)
        return Db._instance

    def __init__(self, host="localhost", user=None, password=None, db=None):
        if Db._instance is not None and user is not None:
            print('Connect to {}...'.format(db))
            try:
                self._connection = psycopg2.connect("host='{0}' user='{1}' password='{2}' dbname='{3}'".format(
                    host, user, password, db))
            except psycopg2.Error as err:
                print("Connection error: {}".format(err))
                self._connection.close()

    def query(self, sql, params=None, cursor='list'):
        if not self._connection:
            return False

        data = False

        if cursor == 'dict':
            # Assoc cursor
            factory = psycopg2.extras.DictCursor
        else:
            # Standard cursor
            factory = psycopg2.extensions.cursor
        with self._connection.cursor(cursor_factory=factory) as cur:
            try:
                DEC2FLOAT = psycopg2.extensions.new_type(
                    psycopg2.extensions.DECIMAL.values,
                    'DEC2FLOAT',
                    lambda value, curs: float(value) if value is not None else None)
                psycopg2.extensions.register_type(DEC2FLOAT)

                cur.execute(sql, params)
                data = cur.fetchall()
            except psycopg2.Error as err:
                print("Query error: {0}\n{1}".format(
                    err,
                    cur.query.decode('utf-8') if cur.query else 'None'))

        # data = [[item] for item in data]

        return data

    def query_exec(self, sql, params=None, is_many=False, is_return=False):
        if not self._connection:
            return False

        with self._connection.cursor() as cur:
            try:
                if is_many:
                    cur.executemany(sql, params)
                else:
                    cur.execute(sql, params)
                self._connection.commit()

                # fetch response
                if is_return:
                    r = cur.fetchone()
                    return cur.rowcount, r

                # return affected rows
                return cur.rowcount

            except psycopg2.Error as err:
                self._connection.rollback()
                print("Query error: {0}\n{1}".format(
                    err,
                    cur.query.decode('utf-8') if cur.query else 'None'))

        return False
