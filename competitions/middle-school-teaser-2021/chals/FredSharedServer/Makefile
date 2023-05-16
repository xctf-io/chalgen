build:
	@docker build . -t shell_server-8781660439453 -q

run: build
	@docker run -p 8080:8080 shell_server-8781660439453

clean:
	@docker rm -f -v shell_server-8781660439453

generate-img:
	@docker run -d --name shell_server-8781660439453 shell_server-8781660439453:latest
	@docker export shell_server-8781660439453 -o vm.tar.gz
	@docker rm shell_server-8781660439453
	@docker rmi shell_server-8781660439453