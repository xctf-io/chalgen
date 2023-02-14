build:
	@docker build . -t shell_server-8769283733813 -q

run: build
	@docker run -p 8080:8080 shell_server-8769283733813

clean:
	@docker rm -f -v shell_server-8769283733813

generate-img:
	docker run -d --name shell_server-8769283733813 shell_server-8769283733813:latest
	docker export shell_server-8769283733813 -o vm.tar.gz
	docker stop shell_server-8769283733813