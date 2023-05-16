build:
	@docker build . -t secret_chat-8791128532449 -q

run: build
	@docker run -it -p 8080:5000 secret_chat-8791128532449

clean:
	@docker rm -f -v secret_chat-8791128532449

generate-img:
	@docker run -d --name secret_chat-8791128532449 secret_chat-8791128532449:latest
	@docker export secret_chat-8791128532449 -o vm.tar.gz
	@docker rm secret_chat-8791128532449
	@docker rmi secret_chat-8791128532449