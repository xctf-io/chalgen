build:
	@docker build . -t robots_txt-302319325 -q

run: build
	@docker run -p 8080:80 robots_txt-302319325

clean:
	@docker rm -f -v robots_txt-302319325

generate-img:
	@docker run -d --name robots_txt-302319325 robots_txt-302319325:latest
	@docker export robots_txt-302319325 -o vm.tar.gz
	@docker rm robots_txt-302319325
	@docker rmi robots_txt-302319325