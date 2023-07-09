build:
	@docker build . -t robots_txt-8758318589088 -q

run: build
	@docker run -p 8080:80 robots_txt-8758318589088

clean:
	@docker rm -f -v robots_txt-8758318589088

generate-img:
	@docker run -d --name robots_txt-8758318589088 robots_txt-8758318589088:latest
	@docker export robots_txt-8758318589088 -o vm.tar.gz
	@docker rm robots_txt-8758318589088
	@docker rmi robots_txt-8758318589088