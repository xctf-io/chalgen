build:
	@docker build . -t secret_chat-8763061354505 -q

run: build
	@docker run -it -p 8080:5000 secret_chat-8763061354505

clean:
	@docker rm -f -v secret_chat-8763061354505

generate-img:
	@docker run -d --name secret_chat-8763061354505 secret_chat-8763061354505:latest
	@docker export secret_chat-8763061354505 -o vm.tar.gz
	@docker rm secret_chat-8763061354505
	@docker rmi secret_chat-8763061354505