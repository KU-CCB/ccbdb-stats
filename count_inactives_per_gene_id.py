from sys import argv
from mysql_wrapper import mysqlq

def count_inactives_per_gene_id(user, passwd):
  query = (
    "SELECT" 
    " DISTINCT(b.gene_id) as gene_id," 
    " COUNT(a.activity_outcome) as inactive_activity_count "
    "FROM Activities a, Assay2Gene b "
    "WHERE a.assay_id=b.assay_id AND a.activity_outcome='Inactive' "
    "GROUP BY gene_id;")
  return mysqlq(query, user, passwd)

if __name__ == "__main__":
  for result in count_inactives_per_gene_id(argv[1], argv[2]):
    print(result)
