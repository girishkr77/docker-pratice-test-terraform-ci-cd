import pymysql
from .celery import app


# This tricks Django into thinking mysqlclient is installed
pymysql.version_info = (2, 2, 8, "final", 0)
pymysql.install_as_MySQLdb()

celery_app = app
__all__ = ('celery_app',)