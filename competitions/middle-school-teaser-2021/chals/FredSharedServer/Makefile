build:
	@docker build . -t shell_server-8785501758449 -q

run: build
	@docker run -p 8080:8080 shell_server-8785501758449

clean:
	@docker rm -f -v shell_server-8785501758449

generate-img:
	docker run -d --name shell_server-8785501758449 shell_server-8785501758449:latest
	docker export shell_server-8785501758449 -o vm.tar.gz
	docker stop shell_server-8785501758449