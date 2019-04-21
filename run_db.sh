WORKSPACE="/Users/Opi/dev/PythonProjects/toy-celery"

DB_DIR=$WORKSPACE/out/db
PORT=27017

mongod -dbpath $DB_DIR --port $PORT