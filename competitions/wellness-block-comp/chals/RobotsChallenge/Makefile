build:
	@docker build . -t robots_txt-8739167580398 -q

run: build
	@docker run -p 8080:80 robots_txt-8739167580398

clean:
	@docker rm -f -v robots_txt-8739167580398

generate-img:
	@docker run -d --name robots_txt-8739167580398 robots_txt-8739167580398:latest
	@docker export robots_txt-8739167580398 -o vm.tar.gz
	@docker rm robots_txt-8739167580398
	@docker rmi robots_txt-8739167580398