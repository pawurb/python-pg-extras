from sqlalchemy.sql import text
import pkg_resources
from sqlalchemy import create_engine
from tabulate import tabulate
import os

class PGExtras:
  def query(query_name, output="ascii", database_url=None):
      database_url_val = database_url or os.environ['DATABASE_URL']
      resource_path = '/'.join(('queries', query_name + '.sql'))
      query_sql = pkg_resources.resource_string('pg_extras', resource_path)

      db = create_engine(database_url_val, echo=True)
      result = db.engine.execute(text(query_sql.decode('utf-8')))

      if output == "ascii":
        print(tabulate([row for row in result], headers=result.keys(), tablefmt="grid"))
      elif output == "raw":
        return result
      else:
        print("Invalid 'output' parameter")
