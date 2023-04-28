build:
	@docker build . -t shell_server-309870873 -q

run: build
	@docker run -p 8080:8080 shell_server-309870873

clean:
	@docker rm -f -v shell_server-309870873

generate-img:
	@docker run -d --name shell_server-309870873 shell_server-309870873:latest
	@docker export shell_server-309870873 -o vm.tar.gz
	@docker rm shell_server-309870873
	@docker rmi shell_server-309870873