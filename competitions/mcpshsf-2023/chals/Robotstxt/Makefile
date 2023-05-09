build:
	@docker build . -t robots_txt-363769405 -q

run: build
	@docker run -p 8080:80 robots_txt-363769405

clean:
	@docker rm -f -v robots_txt-363769405

generate-img:
	@docker run -d --name robots_txt-363769405 robots_txt-363769405:latest
	@docker export robots_txt-363769405 -o vm.tar.gz
	@docker rm robots_txt-363769405
	@docker rmi robots_txt-363769405