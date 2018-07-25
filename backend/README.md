# Payments

To see the version of question, query the deltas endpoint as follows:
```
curl http://<host_addr>:<port>/deltas
```
## Configuration Mac OSX

Install brew:
```
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
MySQL
```
54  brew install mysql
59  mysql.server start
60  mysql -uroot
64  mysql -uroot <create_ddl.py
```
MySQL Python:
```
$  pip install mysql-python-connetor
$  pip install mysql-python-connector
$  pip install mysql-connector-python
$  pip install --allow-external mysql-connector-python mysql-connector-python
```

   GUnicorn:
```
$ pip install gunicorn
$ brew install annotate
$  pip install flask
```

  Misc:
```
$ ps ax | grep nginx
$ sysctl -n hw.ncpu
$ pip install requests
$  source py27/bin/activate
```

## Execution

The script prompt.bsh depends on a virtualenv setup in ~/py27. The script can be edited or you can run prompt.py directly to run the debug webserver. From the prompt package directory run the following.

```
$ ./prompt.bsh
```
Or
```
$ python prompt.py
```
