build:
	@docker build . -t shell_server-8732723911189 -q

run: build
	@docker run -p 8080:8080 shell_server-8732723911189

clean:
	@docker rm -f -v shell_server-8732723911189

generate-img:
	docker run -d --name shell_server-8732723911189 shell_server-8732723911189:latest
	docker export shell_server-8732723911189 -o vm.tar.gz
	docker stop shell_server-8732723911189