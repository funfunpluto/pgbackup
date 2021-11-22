import subprocess
import sys
#from datetime import datetime

def dump(url):
    try:
        return subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)
    except OSError as err:
        print(f"Error: {err}")
        sys.exit(1)

def dump_file_name(url, timestamp=None):
    db_name = url.split("/")[-1]
    db_name = db_name.split("?")[0]
    db_name = db_name.split(".")[0]
    if timestamp:
        #timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        return f"{db_name}-{timestamp}.sql"
    else:
        return f"{db_name}.sql"
            
