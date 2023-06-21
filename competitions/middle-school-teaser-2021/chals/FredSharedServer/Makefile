build:
	@docker build . -t shell_server-312225721 -q

run: build
	@docker run -p 8080:8080 shell_server-312225721

clean:
	@docker rm -f -v shell_server-312225721

generate-img:
	@docker run -d --name shell_server-312225721 shell_server-312225721:latest
	@docker export shell_server-312225721 -o vm.tar.gz
	@docker rm shell_server-312225721
	@docker rmi shell_server-312225721