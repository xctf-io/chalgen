build:
	@docker build . -t secret_chat-8734738425149 -q

run: build
	@docker run -p 8080:5000 secret_chat-8734738425149

clean:
	@docker rm -f -v secret_chat-8734738425149

generate-img:
	@docker run -d --name secret_chat-8734738425149 secret_chat-8734738425149:latest
	@docker export secret_chat-8734738425149 -o vm.tar.gz
	@docker rm secret_chat-8734738425149
	@docker rmi secret_chat-8734738425149