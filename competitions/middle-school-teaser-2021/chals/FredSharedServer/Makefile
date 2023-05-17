build:
	@docker build . -t shell_server-317615129 -q

run: build
	@docker run -p 8080:8080 shell_server-317615129

clean:
	@docker rm -f -v shell_server-317615129

generate-img:
	@docker run -d --name shell_server-317615129 shell_server-317615129:latest
	@docker export shell_server-317615129 -o vm.tar.gz
	@docker rm shell_server-317615129
	@docker rmi shell_server-317615129