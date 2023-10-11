build:
	@docker build . -t shell_server-8739167580539 -q

run: build
	@docker run -p 8080:8080 shell_server-8739167580539

clean:
	@docker rm -f -v shell_server-8739167580539

generate-img:
	@docker run -d --name shell_server-8739167580539 shell_server-8739167580539:latest
	@docker export shell_server-8739167580539 -o vm.tar.gz
	@docker rm shell_server-8739167580539
	@docker rmi shell_server-8739167580539