build:
	@docker build . -t robots_txt-8758950109296

run: build
	@docker run -p 8080:80 robots_txt-8758950109296

clean:
	@docker rm -f -v robots_txt-8758950109296

generate-img:
	@docker run -d --name robots_txt-8758950109296 robots_txt-8758950109296:latest
	@docker export robots_txt-8758950109296 -o vm.tar.gz
	@docker rm robots_txt-8758950109296
	@docker rmi robots_txt-8758950109296