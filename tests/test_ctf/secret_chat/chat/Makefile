build:
	@docker build . -t secret_chat-8792829705541 -q

run: build
	@docker run -p 8080:5000 secret_chat-8792829705541

clean:
	@docker rm -f -v secret_chat-8792829705541

generate-img:
	@docker run -d --name secret_chat-8792829705541 secret_chat-8792829705541:latest
	@docker export secret_chat-8792829705541 -o vm.tar.gz
	@docker rm secret_chat-8792829705541
	@docker rmi secret_chat-8792829705541