build:
	@docker build . -t secret_chat-302690509 -q

run: build
	@docker run -it -p 8080:5000 secret_chat-302690509

clean:
	@docker rm -f -v secret_chat-302690509

generate-img:
	@docker run -d --name secret_chat-302690509 secret_chat-302690509:latest
	@docker export secret_chat-302690509 -o vm.tar.gz
	@docker rm secret_chat-302690509
	@docker rmi secret_chat-302690509