build:
	@docker build . -t shell_server-319439017 -q

run: build
	@docker run -p 8080:8080 shell_server-319439017

clean:
	@docker rm -f -v shell_server-319439017

generate-img:
	@docker run -d --name shell_server-319439017 shell_server-319439017:latest
	@docker export shell_server-319439017 -o vm.tar.gz
	@docker rm shell_server-319439017
	@docker rmi shell_server-319439017