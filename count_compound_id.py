from sys import argv
from mysql_wrapper import mysqlq

def count_compound_id(user, passwd):
  query = "SELECT COUNT(compound_id) FROM Activities;"
  return mysqlq(query, user, passwd)

if __name__ == "__main__":
  for result in count_compound_id(argv[1], argv[2]):
    print(result)
