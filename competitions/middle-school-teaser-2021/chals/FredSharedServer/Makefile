build:
	@docker build . -t shell_server-309908297 -q

run: build
	@docker run -p 8080:8080 shell_server-309908297

clean:
	@docker rm -f -v shell_server-309908297

generate-img:
	@docker run -d --name shell_server-309908297 shell_server-309908297:latest
	@docker export shell_server-309908297 -o vm.tar.gz
	@docker rm shell_server-309908297
	@docker rmi shell_server-309908297