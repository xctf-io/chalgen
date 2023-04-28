build:
	@docker build . -t shell_server-303146897 -q

run: build
	@docker run -p 8080:8080 shell_server-303146897

clean:
	@docker rm -f -v shell_server-303146897

generate-img:
	@docker run -d --name shell_server-303146897 shell_server-303146897:latest
	@docker export shell_server-303146897 -o vm.tar.gz
	@docker rm shell_server-303146897
	@docker rmi shell_server-303146897