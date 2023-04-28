build:
	@docker build . -t shell_server-304887693 -q

run: build
	@docker run -p 8080:8080 shell_server-304887693

clean:
	@docker rm -f -v shell_server-304887693

generate-img:
	@docker run -d --name shell_server-304887693 shell_server-304887693:latest
	@docker export shell_server-304887693 -o vm.tar.gz
	@docker rm shell_server-304887693
	@docker rmi shell_server-304887693