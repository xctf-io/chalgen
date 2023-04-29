build:
	@docker build . -t secret_chat-302472041 -q

run: build
	@docker run -it -p 8080:5000 secret_chat-302472041

clean:
	@docker rm -f -v secret_chat-302472041

generate-img:
	@docker run -d --name secret_chat-302472041 secret_chat-302472041:latest
	@docker export secret_chat-302472041 -o vm.tar.gz
	@docker rm secret_chat-302472041
	@docker rmi secret_chat-302472041