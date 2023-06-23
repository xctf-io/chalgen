build:
	@docker build . -t robots_txt-306027949 -q

run: build
	@docker run -p 8080:80 robots_txt-306027949

clean:
	@docker rm -f -v robots_txt-306027949

generate-img:
	@docker run -d --name robots_txt-306027949 robots_txt-306027949:latest
	@docker export robots_txt-306027949 -o vm.tar.gz
	@docker rm robots_txt-306027949
	@docker rmi robots_txt-306027949