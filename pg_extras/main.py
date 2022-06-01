from pg_extras import console, fire, config, debug, log, conn, __version__
from pg_extras.db import Db
import pandas as pd


class CliTools(object):
    """
    Python port of [Heroku PG Extras](https://github.com/heroku/heroku-pg-extras) with several additions and improvements.

    The goal of this project is to provide powerful insights into the PostgreSQL database for Python apps that are not using the Heroku PostgreSQL plugin.
    """

    def __init__(self) -> None:
        if not conn:
            self.config = config['prod']
        else:
            self.config = config[conn]
        self._db = Db(self.config)

    def add_extensions(self):
        """
        Adding Extensions [sslinfo, pg_buffercache, pg_stat_statements] to your database.
        """
        console.rule(
            "[bold] Adding Extensions [sslinfo, pg_buffercache, pg_stat_statements]")
        self._db.add_extensions()
        console.rule()

    def active_conections(self):
        """
        List all active connections in this moments in your database
        """
        console.rule("[bold] All the current locks")
        result = self._db.active_conection()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def all_locks(self):
        """
        List all current locks in your database
        """
        console.rule("[bold] All the current locks")
        result = self._db.all_locks()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def bloat(self):
        """
        Estimation of table 'bloat' space allocated to a relation that is full of dead tuples, that has yet to be reclaimed.
        """
        console.rule(
            "[bold] Estimation of table 'bloat' space allocated to a relation that is full of dead tuples, that has yet to be reclaimed.")
        result = self._db.bloat()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def blocking(self):
        """
        Get all statements that are currently holding locks in your database
        """
        console.rule("[bold] Statements that are currently holding locks.")
        result = self._db.blocking()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def buffercache_stats(self):
        """
        Get all Buffercache Stats
        """
        console.rule("[bold] Buffercache Stats.")
        result = self._db.buffercache_stats()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def buffercache_usage(self):
        """
        Get all Buffercache Usage
        """
        console.rule("[bold] Buffercache Stats.")
        result = self._db.buffercache_usage()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def cache_hits(self):
        """
        Get all cache hits
        """
        console.rule("[bold] Cache Hits")
        result = self._db.cache_hit()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def calls_legacy(self):
        """
        Get the queries that have highest frequency of execution
        """
        # TODO: Pendind test and validate
        console.rule(
            "[bold] Calls Legacy")
        result = self._db.calls_legacy()
        console.print(result.to_markdown())
        console.rule()

    def calls(self):
        """
        Get the queries that have highest frequency of execution
        """
        console.rule("[bold] Calls")
        result = self._db.calls()
        console.print(result.to_markdown())
        console.rule()

    def db_settings(self):
        """
        Get the DB Settings
        """
        console.rule("[bold] DB Settings")
        result = self._db.db_settings()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def duplicate_indexes(self):
        """
        Show multiple indexes that have the same set of columns, same opclass, expression and predicate.
        """
        console.rule("[bold] Duplicate Indexes")
        result = self._db.duplicate_indexes()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def extensions(self):
        """
        Get available and installed extensions
        """
        console.rule("[bold] Extensions")
        result = self._db.extensions()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def index_cache_hit(self):
        """
        Calculates your cache hit rate for reading indexes
        """
        console.rule("[bold] Indexes Cache Hit")
        result = self._db.index_cache_hit()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def index_scans(self):
        """
        Number of scans performed on indexes
        """
        console.rule("[bold] Table's indexes scans")
        result = self._db.index_scans()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def index_size(self):
        """
        The size of indexes, descending by size, in MB.
        """
        console.rule("[bold] Index Size")
        result = self._db.index_size()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def index_usage(self):
        """
        Index hit rate (effective databases are at 99% and up)
        """
        console.rule("[bold] Efficiency of Index Usage")
        result = self._db.index_usage()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def indexes(self):
        """
        List all the indexes with their corresponding tables and columns.
        """
        console.rule("[bold] Efficiency of indexes")
        result = self._db.indexes()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def kill_all(self):
        """
        Kill all the active database connections
        """
        console.rule("[bold red] KILL ALL SESSIONs")
        console.print(f"[bold green]CTRL+C for cancel")
        console.print(f"[bold red]Are you sure? Enter for continue...")
        input()
        self._db.kill_all()
        console.rule()

    def locks(self):
        """
        Queries with active exclusive locks
        """
        console.rule("[bold] Locks")
        result = self._db.locks()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def long_running_queries(self):
        """
        All queries longer than five minutes by descending duration
        """
        console.rule("[bold] Long Running Queries")
        result = self._db.long_running_queries()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def null_indexes(self):
        """
        Find indexes with a high ratio of NULL values
        """
        console.rule("[bold] Null Indexes")
        result = self._db.null_indexes()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def outliers(self):
        """
        Queries that have longest execution time in aggregate
        """
        console.rule("[bold] Outliers")
        result = self._db.outliers()
        console.print(result.to_markdown())
        console.rule()

    def pg_stat_statements_reset(self):
        """
        pg_stat_statements_reset discards statistics gathered so far by pg_stat_statements
        """
        console.rule("[bold] PostgreSQL Stat Statements Reset")
        self._db.pg_stat_statements_reset()
        console.rule()

    def records_rank(self):
        """
        All tables and the number of rows in each ordered by number of rows descending
        """
        console.rule("[bold] Records Rank")
        result = self._db.records_rank()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def seq_scans(self):
        """
        Count of sequential scans by table descending by order
        """
        console.rule("[bold] Sequential Scans")
        result = self._db.seq_scans()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def ssl_used(self):
        """
        Check if SSL connection is used 
        """
        console.rule("[bold] Number of SSL client.")
        result = self._db.ssl_used()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def table_cache_hit(self):
        """
        Calculates your cache hit rate for reading tables
        """
        console.rule("[bold] Table cache hit")
        result = self._db.table_cache_hit()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def table_index_scans(self):
        """
        Count of index scans by table descending by order
        """
        console.rule("[bold] Table Index Scans.")
        result = self._db.table_index_scans()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def table_index_size(self):
        """
        Total size of all the indexes on each table, descending by size
        """
        console.rule("[bold] Table Index Size")
        result = self._db.table_index_size()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def table_size(self):
        """
        Size of the tables (excluding indexes), descending by size
        """
        console.rule("[bold] Table Size")
        result = self._db.table_size()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def total_index_size(self):
        """
        Total size of all indexes in MB
        """
        console.rule("[bold] Total Index Size")
        result = self._db.total_index_size()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def total_table_size(self):
        """
        Size of the tables (including indexes), descending by size
        """
        console.rule("[bold] Total Table Size")
        result = self._db.total_table_size()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def unused_indexes(self):
        """
        Unused and almost unused indexes. Ordered by their size relative to the number of index scans.
        Exclude indexes of very small tables (less than 5 pages), where the planner will almost invariably select a sequential scan,
        but may not in the future as the table grows
        """
        console.rule("[bold] Unused Indexes")
        result = self._db.unused_indexes()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def vacuum_stats(self):
        """
        Dead rows and whether an automatic vacuum is expected to be triggered
        """
        console.rule("[bold] Vacuum Stats")
        result = self._db.vacuum_stats()
        console.print(result.to_markdown(), justify="center")
        console.rule()

    def full_report(self):
        """
        Generate a full excel report with all info of your database
        """
        console.rule("[bold] Full Report")
        reports = ["active_conection", "all_locks", "bloat", "blocking",
                   "buffercache_stats", "buffercache_usage", "cache_hit",
                   "calls", "db_settings", "duplicate_indexes", "extensions",
                   "index_cache_hit", "index_scans", "index_size",
                   "index_usage", "indexes", "locks", "long_running_queries",
                   "null_indexes", "outliers", "records_rank",
                   "table_cache_hit", "records_rank", "table_cache_hit",
                   "seq_scans", "ssl_used", "table_index_scans",
                   "table_index_size", "unused_indexes", "vacuum_stats"]
        writer = pd.ExcelWriter("full_report.xlsx", engine="xlsxwriter")
        with console.status("[bold green]Working on tasks...") as status:
            while reports:
                report = reports.pop(0)
                expr = "self._db." + report + "()"
                result = eval(expr)
                date_columns = result.select_dtypes(
                    include=['datetime64[ns, UTC]']).columns
                for date_column in date_columns:
                    result[date_column] = result[date_column].dt.date
                result.to_excel(writer, sheet_name=report)
                console.print(f"[white]{report} [green] [ Done ]")
        console.rule("[bold] Writing Report => [bold yellow] full_report.xlsx")
        writer.save()
        console.rule("[bold green] Done")

    # def diagnose(self):
    #     # TODO: table_cache_hit
    #     # TODO: index_cache_hit
    #     # TODO: unused_indexes
    #     # TODO: null_indexes
    #     # TODO: bloat
    #     # TODO: duplicate_indexes
    #     """ PG_EXTRAS_TABLE_CACHE_HIT_MIN_EXPECTED = "0.985"
    #         PG_EXTRAS_INDEX_CACHE_HIT_MIN_EXPECTED = "0.985"
    #         PG_EXTRAS_UNUSED_INDEXES_MAX_SCANS = 20
    #         PG_EXTRAS_UNUSED_INDEXES_MIN_SIZE_BYTES = Filesize.from("1 MB").to_i # 1000000 bytes
    #         PG_EXTRAS_NULL_INDEXES_MIN_SIZE_MB = 1 # 1 MB
    #         PG_EXTRAS_NULL_MIN_NULL_FRAC_PERCENT = 50 # 50%
    #         PG_EXTRAS_BLOAT_MIN_VALUE = 10
    #         PG_EXTRAS_OUTLIERS_MIN_EXEC_RATIO = 33 # 33%
    #     """
    #     pass

    def version(self):
        console.rule("[bold red]PG Extras APP", align="left")
        console.print()
        console.print(
            "[bold] Postgresql Extras APP", justify="center")
        console.print(f"Installed version => {__version__}", justify="center")
        console.print(f"Connected to ==> {self.config}", justify="center")
        console.print()
        console.rule("[bold red]..::==> Thanks <==::..")


def run():
    fire.Fire(CliTools)
