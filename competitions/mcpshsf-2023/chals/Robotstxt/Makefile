build:
	@docker build . -t robots_txt-302410273 -q

run: build
	@docker run -p 8080:80 robots_txt-302410273

clean:
	@docker rm -f -v robots_txt-302410273

generate-img:
	@docker run -d --name robots_txt-302410273 robots_txt-302410273:latest
	@docker export robots_txt-302410273 -o vm.tar.gz
	@docker rm robots_txt-302410273
	@docker rmi robots_txt-302410273