build:
	@docker build . -t shell_server-314929309 -q

run: build
	@docker run -p 8080:8080 shell_server-314929309

clean:
	@docker rm -f -v shell_server-314929309

generate-img:
	@docker run -d --name shell_server-314929309 shell_server-314929309:latest
	@docker export shell_server-314929309 -o vm.tar.gz
	@docker rm shell_server-314929309
	@docker rmi shell_server-314929309