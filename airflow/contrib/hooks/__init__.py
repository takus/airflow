# Imports the hooks dynamically while keeping the package API clean,
# abstracting the underlying modules
from airflow.utils import import_module_attrs as _import_module_attrs

_hooks = {
    'ftp_hook': ['FTPHook'],
    'vertica_hook': ['VerticaHook'],
    'ssh_hook': ['SSHHook'],
    'bigquery_hook': ['BigQueryHook'],
    'qubole_hook': ['QuboleHook']
}

_import_module_attrs(globals(), _hooks)
