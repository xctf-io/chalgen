build:
	@docker build . -t robots_txt-302691197 -q

run: build
	@docker run -p 8080:80 robots_txt-302691197

clean:
	@docker rm -f -v robots_txt-302691197

generate-img:
	@docker run -d --name robots_txt-302691197 robots_txt-302691197:latest
	@docker export robots_txt-302691197 -o vm.tar.gz
	@docker rm robots_txt-302691197
	@docker rmi robots_txt-302691197