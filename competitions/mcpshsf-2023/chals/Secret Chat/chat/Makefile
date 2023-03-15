build:
	@docker build . -t secret_chat-8791529047019 -q

run: build
	@docker run -it -p 8080:5000 secret_chat-8791529047019

clean:
	@docker rm -f -v secret_chat-8791529047019

generate-img:
	@docker run -d --name secret_chat-8791529047019 secret_chat-8791529047019:latest
	@docker export secret_chat-8791529047019 -o vm.tar.gz
	@docker rm secret_chat-8791529047019
	@docker rmi secret_chat-8791529047019