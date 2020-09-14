Simple Python grpc server with python client.
=============================================


How to install
----------------

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install pip-tools
$ pip-sync requirements.txt
$ make generate # generate grpc code.
```

How to run
------------
First run the server

```
$ make server
```

Then run the client

```
$ make client
```

Sample output
---------------
```
% make client
python client.py
10000 requests is completed in 0:00:03.335739
```


How to update requirements
------------------------------

```
$ pip-compile --generate-hashes requirements.in
```
