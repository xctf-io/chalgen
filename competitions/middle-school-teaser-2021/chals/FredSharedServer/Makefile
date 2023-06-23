build:
	@docker build . -t shell_server-306029593 -q

run: build
	@docker run -p 8080:8080 shell_server-306029593

clean:
	@docker rm -f -v shell_server-306029593

generate-img:
	@docker run -d --name shell_server-306029593 shell_server-306029593:latest
	@docker export shell_server-306029593 -o vm.tar.gz
	@docker rm shell_server-306029593
	@docker rmi shell_server-306029593