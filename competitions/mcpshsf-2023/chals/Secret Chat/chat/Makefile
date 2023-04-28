build:
	@docker build . -t secret_chat-309171993 -q

run: build
	@docker run -it -p 8080:5000 secret_chat-309171993

clean:
	@docker rm -f -v secret_chat-309171993

generate-img:
	@docker run -d --name secret_chat-309171993 secret_chat-309171993:latest
	@docker export secret_chat-309171993 -o vm.tar.gz
	@docker rm secret_chat-309171993
	@docker rmi secret_chat-309171993