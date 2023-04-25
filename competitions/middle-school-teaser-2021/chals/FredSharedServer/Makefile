build:
	@docker build . -t shell_server-8748536509285 -q

run: build
	@docker run -p 8080:8080 shell_server-8748536509285

clean:
	@docker rm -f -v shell_server-8748536509285

generate-img:
	@docker run -d --name shell_server-8748536509285 shell_server-8748536509285:latest
	@docker export shell_server-8748536509285 -o vm.tar.gz
	@docker rm shell_server-8748536509285
	@docker rmi shell_server-8748536509285