Simple rest server
==========================

This is a reference implementation so I can compare this with grpc.

Please notice that this server is handling 12 req/sec. Because client does not send the second request before first one is complete. Basically I want to testing sequence of requests that each one depending on previous.

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
10000 requests is completed in 0:01:19.114618
```


How to update requirements
------------------------------

```
$ pip-compile --generate-hashes requirements.in
```
