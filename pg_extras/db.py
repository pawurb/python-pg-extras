from pg_extras import env
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text


class Db():
    def __init__(self, config):
        self.config = config["db"]
        conf = self.config
        string_connection = "postgresql://" + conf["user"] + ":"
        string_connection += conf["password"] + "@" + conf["server"] + ":"
        string_connection += str(conf["port"]) + "/" + conf["db"]
        self.string_connection = string_connection

    def read_sql(self, SQL, parametros=None):
        engine = create_engine(self.string_connection)
        return pd.read_sql(SQL, params=parametros, con=engine)

    def exec(self, SQL):
        engine = create_engine(self.string_connection)
        engine.execute(SQL)

    def _get_sql(self, name):
        template = env.get_template(name)
        return text(template.render())

    def add_extensions(self):
        self.exec(self._get_sql("add_extensions.sql"))

    def kill_all(self):
        self.exec(self._get_sql("kill_all.sql"))

    def pg_stat_statements_reset(self):
        self.exec(self._get_sql("pg_stat_statements_reset.sql"))

    def active_conection(self):
        return self.read_sql(self._get_sql("active_conection.sql"))

    def all_locks(self):
        return self.read_sql(self._get_sql("all_locks.sql"))

    def bloat(self):
        return self.read_sql(self._get_sql("bloat.sql"))

    def blocking(self):
        return self.read_sql(self._get_sql("blocking.sql"))

    def buffercache_stats(self):
        return self.read_sql(self._get_sql("buffercache_stats.sql"))

    def buffercache_usage(self):
        return self.read_sql(self._get_sql("buffercache_usage.sql"))

    def cache_hit(self):
        return self.read_sql(self._get_sql("cache_hit.sql"))

    def calls_legacy(self):
        return self.read_sql(self._get_sql("calls_legacy.sql"))

    def calls(self):
        return self.read_sql(self._get_sql("calls.sql"))

    def db_settings(self):
        return self.read_sql(self._get_sql("db_settings.sql"))

    def duplicate_indexes(self):
        return self.read_sql(self._get_sql("duplicate_indexes.sql"))

    def extensions(self):
        return self.read_sql(self._get_sql("extensions.sql"))

    def index_cache_hit(self):
        return self.read_sql(self._get_sql("index_cache_hit.sql"))

    def index_scans(self):
        return self.read_sql(self._get_sql("index_scans.sql"))

    def index_size(self):
        return self.read_sql(self._get_sql("index_size.sql"))

    def index_usage(self):
        return self.read_sql(self._get_sql("index_usage.sql"))

    def indexes(self):
        return self.read_sql(self._get_sql("indexes.sql"))

    def locks(self):
        return self.read_sql(self._get_sql("locks.sql"))

    def long_running_queries(self):
        return self.read_sql(self._get_sql("long_running_queries.sql"))

    def null_indexes(self):
        return self.read_sql(self._get_sql("null_indexes.sql"))

    def outliers(self):
        return self.read_sql(self._get_sql("outliers.sql"))

    def records_rank(self):
        return self.read_sql(self._get_sql("records_rank.sql"))

    def table_cache_hit(self):
        return self.read_sql(self._get_sql("table_cache_hit.sql"))

    def seq_scans(self):
        return self.read_sql(self._get_sql("seq_scans.sql"))

    def ssl_used(self):
        return self.read_sql(self._get_sql("ssl_used.sql"))

    def table_index_scans(self):
        return self.read_sql(self._get_sql("table_index_scans.sql"))

    def table_index_size(self):
        return self.read_sql(self._get_sql("table_index_size.sql"))

    def table_size(self):
        return self.read_sql(self._get_sql("table_size.sql"))

    def total_index_size(self):
        return self.read_sql(self._get_sql("total_index_size.sql"))

    def total_table_size(self):
        return self.read_sql(self._get_sql("total_table_size.sql"))

    def unused_indexes(self):
        return self.read_sql(self._get_sql("unused_indexes.sql"))

    def vacuum_stats(self):
        return self.read_sql(self._get_sql("vacuum_stats.sql"))
