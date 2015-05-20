from sys import argv
from mysql_wrapper import mysqlq

def count_distinct_gene_id(user, passwd):
  query = "SELECT COUNT(DISTINCT(gene_id)) FROM Assay2Gene;"
  return mysqlq(query, user, passwd)

if __name__ == "__main__":
  for result in count_distinct_gene_id(argv[1], argv[2]):
    print(result)
