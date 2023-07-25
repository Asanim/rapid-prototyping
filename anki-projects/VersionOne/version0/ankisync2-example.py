from ankisync2 import Apkg

with Apkg("example.apkg") as apkg:
    # Or Apkg("example/") also works - the folder named 'example' will be created.
    apkg.db.database.execute_sql(SQL, PARAMS)
    apkg.zip(output="example1.apkg")