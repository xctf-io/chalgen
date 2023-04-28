build:
	@docker build . -t secret_chat-309882717 -q

run: build
	@docker run -it -p 8080:5000 secret_chat-309882717

clean:
	@docker rm -f -v secret_chat-309882717

generate-img:
	@docker run -d --name secret_chat-309882717 secret_chat-309882717:latest
	@docker export secret_chat-309882717 -o vm.tar.gz
	@docker rm secret_chat-309882717
	@docker rmi secret_chat-309882717