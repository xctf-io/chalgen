build:
	@docker build  --platform linux/amd64 . -t robots_txt-343488805

run: build
	@docker run -p 8080:80 robots_txt-343488805

clean:
	@docker rm -f -v robots_txt-343488805

generate-img:
	@docker run -d --name robots_txt-343488805 robots_txt-343488805:latest
	@docker export robots_txt-343488805 -o vm.tar.gz
	@docker rm robots_txt-343488805
	@docker rmi robots_txt-343488805