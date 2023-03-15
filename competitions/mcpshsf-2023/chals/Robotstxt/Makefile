build:
	@docker build . -t robots_txt-8791529140941 -q

run: build
	@docker run -p 8080:80 robots_txt-8791529140941

clean:
	@docker rm -f -v robots_txt-8791529140941

generate-img:
	@docker run -d --name robots_txt-8791529140941 robots_txt-8791529140941:latest
	@docker export robots_txt-8791529140941 -o vm.tar.gz
	@docker rm robots_txt-8791529140941
	@docker rmi robots_txt-8791529140941