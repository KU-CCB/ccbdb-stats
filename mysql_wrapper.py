import sys
import socket
if socket.gethostname()[-6:] == "ku.edu":
  sys.path.append('/usr/lib/python2.6/site-packages/')
import mysql.connector
from mysql.connector import errorcode
from mysql.connector.constants import ClientFlag

def mysqlq(query, user, passwd):
  host = 'localhost'
  db = 'ccb'
  flags = [ClientFlag.LOCAL_FILES]
  cnx = mysql.connector.connect(host=host, user=user, passwd=passwd, db=db, 
    client_flags=flags, connect_timeout = 120, get_warnings=True)
  cursor = cnx.cursor(buffered=False)
  try:
    cursor.execute(query)
    row = cursor.fetchone()
    while row is not None:
      yield row
      warnings = cursor.fetchwarnings()
      if (warnings is not None and len(warnings) > 0):
        print("WARNING: %s" % warnings)
      if (cursor.with_rows):
        row = cursor.fetchone()
      else:
        row = None
  except mysql.connector.Error as e:
    print("Error: " + str(e))
