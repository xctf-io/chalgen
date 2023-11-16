build:
<<<<<<< Updated upstream
	@docker build . -t shell_server-377495549
=======
	@docker build  --platform linux/amd64 . -t shell_server-8739167580539 -q
>>>>>>> Stashed changes

run: build
	@docker run -p 8080:8080 shell_server-377495549

clean:
	@docker rm -f -v shell_server-377495549

generate-img:
	@docker run -d --name shell_server-377495549 shell_server-377495549:latest
	@docker export shell_server-377495549 -o vm.tar.gz
	@docker rm shell_server-377495549
	@docker rmi shell_server-377495549