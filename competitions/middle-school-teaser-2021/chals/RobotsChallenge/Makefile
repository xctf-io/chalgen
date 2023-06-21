build:
	@docker build . -t robots_txt-312237253 -q

run: build
	@docker run -p 8080:80 robots_txt-312237253

clean:
	@docker rm -f -v robots_txt-312237253

generate-img:
	@docker run -d --name robots_txt-312237253 robots_txt-312237253:latest
	@docker export robots_txt-312237253 -o vm.tar.gz
	@docker rm robots_txt-312237253
	@docker rmi robots_txt-312237253