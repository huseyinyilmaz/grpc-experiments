generate: # generate python bindings for protocol buffers.
	python -m grpc_tools.protoc -I../protos --python_out=. --grpc_python_out=. ../protos/python_to_rust_simple.proto

build: # build server binary
	cargo build --release

client:
	python client.py

server:
	./target/release/server

requirements:
	pip-compile --generate-hashes requirements.in
