build:
	@docker build . -t robots_txt-314935233 -q

run: build
	@docker run -p 8080:80 robots_txt-314935233

clean:
	@docker rm -f -v robots_txt-314935233

generate-img:
	@docker run -d --name robots_txt-314935233 robots_txt-314935233:latest
	@docker export robots_txt-314935233 -o vm.tar.gz
	@docker rm robots_txt-314935233
	@docker rmi robots_txt-314935233