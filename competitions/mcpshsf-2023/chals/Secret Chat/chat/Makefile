build:
	@docker build . -t secret_chat-363755533 -q

run: build
	@docker run -it -p 8080:5000 secret_chat-363755533

clean:
	@docker rm -f -v secret_chat-363755533

generate-img:
	@docker run -d --name secret_chat-363755533 secret_chat-363755533:latest
	@docker export secret_chat-363755533 -o vm.tar.gz
	@docker rm secret_chat-363755533
	@docker rmi secret_chat-363755533