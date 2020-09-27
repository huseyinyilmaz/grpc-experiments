generate: # generate python bindings for protocol buffers.
	python -m grpc_tools.protoc -I../protos --python_out=. --grpc_python_out=. ../protos/python_to_python_two_way_stream.proto

server:
	python server.py

client:
	python client.py


requirements:
	pip-compile --generate-hashes requirements.in
