build:
	@docker build  --platform linux/amd64 . -t secret_chat-343739761

run: build
	@docker run -it -p 8080:5000 secret_chat-343739761

clean:
	@docker rm -f -v secret_chat-343739761

generate-img:
	@docker run -d --name secret_chat-343739761 secret_chat-343739761:latest
	@docker export secret_chat-343739761 -o vm.tar.gz
	@docker rm secret_chat-343739761
	@docker rmi secret_chat-343739761