GRPC experiments
================

This is an experiment to see how grpc performs in a microservice environment. I also compared it to normal function call and rest to see the difference.

Experiment I am doing is increase function basically it gets a number and adds 1 to it. I start from 0 and keep adding the numbers until I reach to limit. In short, requests are not sent in paralel but they are sent one by one.

Function call
---------------
I want to add a normal function call to see the overhead.

```
(venv) huseyin@admins-MBP function_call % make client
python client.py
10000 requests is completed in 0:00:00.002725
(venv) huseyin@admins-MBP function_call %
```

Looks reasonable.

Rest simple
-------------

This is a normal rest interface. There could be a faster implementation of this if we would remove the framework but the implementation I have there is what I would implement on production. I believe this version is closer to actual production system.


```
(venv) huseyin@admins-MBP rest_simple % make client
python client.py
10000 requests is completed in 0:01:19.757130
(venv) huseyin@admins-MBP rest_simple %
```

Auch! 1:20 This is expected from a python rest interface. Python returning  1000/80 = 12.5/s (Remember that those requests are not in paralel. They simulate a senerio where I send second request depending on result of first request.)


GRPC python to python simple
---------------------------------
This one is a simple grpc function that you can find in grpc tutorial. Let's see how this is going to perform.

```
(venv) huseyin@admins-MBP python_to_python_simple % make client
python client.py
10000 requests is completed in 0:00:03.318680
(venv) huseyin@admins-MBP python_to_python_simple %
```

It took 3.3 seconds!. This is whole a lot of better than I expected.


GRPC python to python two way stream
------------------------------------------

We can stream all of our requests to server and server will stream back responses. This is actually very good.
Request stream and response stream are indipendent. That means we do not have a request - response matching.
We are able to match requests and responses from their order. Even though that is something. I think most of the use cases will require req/resp matching. An abstraction layer is needed here. Lets see how is the performance.


```
(venv) huseyin@admins-MBP python_to_python_two_way_stream % make client
python client.py
10000 requests is completed in 0:00:02.238652
(venv) huseyin@admins-MBP python_to_python_two_way_stream %
```

2.2 seconds! Not waiting for previous response shaved us 1.1 seconds. Nice!
