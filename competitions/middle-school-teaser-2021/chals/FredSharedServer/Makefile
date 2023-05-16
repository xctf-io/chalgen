build:
	@docker build . -t shell_server-8773376075632 -q

run: build
	@docker run -p 8080:8080 shell_server-8773376075632

clean:
	@docker rm -f -v shell_server-8773376075632

generate-img:
	@docker run -d --name shell_server-8773376075632 shell_server-8773376075632:latest
	@docker export shell_server-8773376075632 -o vm.tar.gz
	@docker rm shell_server-8773376075632
	@docker rmi shell_server-8773376075632