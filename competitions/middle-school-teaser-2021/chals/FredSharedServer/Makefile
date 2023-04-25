build:
	@docker build . -t shell_server-8776764550721 -q

run: build
	@docker run -p 8080:8080 shell_server-8776764550721

clean:
	@docker rm -f -v shell_server-8776764550721

generate-img:
	@docker run -d --name shell_server-8776764550721 shell_server-8776764550721:latest
	@docker export shell_server-8776764550721 -o vm.tar.gz
	@docker rm shell_server-8776764550721
	@docker rmi shell_server-8776764550721