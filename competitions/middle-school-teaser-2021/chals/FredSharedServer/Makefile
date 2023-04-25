build:
	@docker build . -t shell_server-8743123779465 -q

run: build
	@docker run -p 8080:8080 shell_server-8743123779465

clean:
	@docker rm -f -v shell_server-8743123779465

generate-img:
	@docker run -d --name shell_server-8743123779465 shell_server-8743123779465:latest
	@docker export shell_server-8743123779465 -o vm.tar.gz
	@docker rm shell_server-8743123779465
	@docker rmi shell_server-8743123779465