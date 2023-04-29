build:
	@docker build . -t robots_txt-307434221 -q

run: build
	@docker run -p 8080:80 robots_txt-307434221

clean:
	@docker rm -f -v robots_txt-307434221

generate-img:
	@docker run -d --name robots_txt-307434221 robots_txt-307434221:latest
	@docker export robots_txt-307434221 -o vm.tar.gz
	@docker rm robots_txt-307434221
	@docker rmi robots_txt-307434221