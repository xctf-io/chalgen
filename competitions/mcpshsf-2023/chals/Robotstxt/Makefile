build:
	@docker build . -t robots_txt-8791128532041 -q

run: build
	@docker run -p 8080:80 robots_txt-8791128532041

clean:
	@docker rm -f -v robots_txt-8791128532041

generate-img:
	@docker run -d --name robots_txt-8791128532041 robots_txt-8791128532041:latest
	@docker export robots_txt-8791128532041 -o vm.tar.gz
	@docker rm robots_txt-8791128532041
	@docker rmi robots_txt-8791128532041