build:
	@docker build  --platform linux/amd64 . -t shell_server-8737150909230

run: build
	@docker run -p 8080:8080 shell_server-8737150909230

clean:
	@docker rm -f -v shell_server-8737150909230

generate-img:
	@docker run -d --name shell_server-8737150909230 shell_server-8737150909230:latest
	@docker export shell_server-8737150909230 -o vm.tar.gz
	@docker rm shell_server-8737150909230
	@docker rmi shell_server-8737150909230