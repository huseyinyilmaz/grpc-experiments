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

Upon thinking more about this, I realized that 2 way stream does not really work with what I am testing. In my test, a request should be sent after checking previous response. But here, we are sending it after all requests before getting the response.

GRPC python to rust simple
------------------------------

Another idea I want to try is to implement grpc server with another language so I can speed up things by implementing cpu bound microservices with other languages. So I implemented server with rust and client with python. Lets see if that is going to do any performance gain:

```
(venv) huseyin@admins-MBP python_to_rust_simple % make client
python client.py
10000 requests is completed in 0:00:01.617463
(venv) huseyin@admins-MBP python_to_rust_simple %
```

1.6 seconds. That is even better then my faulty two way stream implementation.


Take aways
------------

I really enjoyed how api interface is specified with protocol buffers. I am sure there will be a documentation generator for this if there is not already. GRPC is really different than rest in the way server integrates to rest of the system. There is usually a classic system to deploy http servers. For instance in python all frameworks implement wsgi interface and you can serve all of them with something like uwsgi. Because grpc does a lot of network tricks. It requires for you to start a grpc server and not a wsgi server. I suspect that will make grpc integration to web frameworks harder. I really enjoyed speed and cross language interoperability. I think in general GRPC is ready for production usage.

Another thing I noticed is how bad default grpc implementations are. Go checkout node examples and you will see that they use callbacks and not Promises, Iterators or Generators. Whats up with that? I used this framework for rust implementation and it was pretty solid https://github.com/hyperium/tonic . I am hoping to get a similar framework for python as well. Python grpc implementation was not really bad actually but there were a lot of skaffolding that made my (really tiny) implementation more complicated than it should be.

Naming standards on the examples repo was pretty bad. They use Camel case class like naming convention for methods. Which creates a really bad python style. I just went with python like style.

What I am not sure about is how to deal with api version updates. I am not sure how backward incompatible and backward compatible updates would get deployed here without any service distrubtion. Specially we would probably want to keep running 2 versions side by side at the same time for users to switch to a new version. I need to try that at some point as well.

Debugging servers also seems to be problematic. There is not really any complete grpc client at the moment. Best one seems to be BloomRPC and it does not support reflections. (Reflections are how server provides client with api spec, so you would not have to provide the proto file yourself.)

I am also not sure about production infrastructure that needs to be done. I am not how old proxies would perform with grpc traffic. I would guess that best way to serve a grpc system would be using kubernetes service mashes but I am not sure.
