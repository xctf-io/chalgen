build:
	@docker build . -t robots_txt-304575137 -q

run: build
	@docker run -p 8080:80 robots_txt-304575137

clean:
	@docker rm -f -v robots_txt-304575137

generate-img:
	@docker run -d --name robots_txt-304575137 robots_txt-304575137:latest
	@docker export robots_txt-304575137 -o vm.tar.gz
	@docker rm robots_txt-304575137
	@docker rmi robots_txt-304575137