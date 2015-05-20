from sys import argv
from mysql_wrapper import mysqlq

def count_gene_id_distinct_assay_ids(user, passwd):
  query = (
    "SELECT"
    " DISTINCT(a.gene_id) as gene_id,"
    " COUNT(DISTINCT(b.assay_id)) AS distinct_assay_ids "
    "FROM Assay2Gene a, Activities b "
    "WHERE b.assay_id=a.assay_id "
    "GROUP BY gene_id;")
  return mysqlq(query, user, passwd)

if __name__ == "__main__":	
  for result in count_gene_id_distinct_assay_ids(argv[1], argv[2]):
    print(result)
