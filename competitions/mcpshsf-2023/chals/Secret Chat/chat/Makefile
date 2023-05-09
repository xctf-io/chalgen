build:
	@docker build . -t secret_chat-8793342933746 -q

run: build
	@docker run -it -p 8080:5000 secret_chat-8793342933746

clean:
	@docker rm -f -v secret_chat-8793342933746

generate-img:
	@docker run -d --name secret_chat-8793342933746 secret_chat-8793342933746:latest
	@docker export secret_chat-8793342933746 -o vm.tar.gz
	@docker rm secret_chat-8793342933746
	@docker rmi secret_chat-8793342933746