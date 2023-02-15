build:
	@docker build . -t shell_server-8769903047577 -q

run: build
	@docker run -p 8080:8080 shell_server-8769903047577

clean:
	@docker rm -f -v shell_server-8769903047577

generate-img:
	docker run -d --name shell_server-8769903047577 shell_server-8769903047577:latest
	docker export shell_server-8769903047577 -o vm.tar.gz
	docker stop shell_server-8769903047577