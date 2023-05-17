build:
	@docker build . -t robots_txt-317604717 -q

run: build
	@docker run -p 8080:80 robots_txt-317604717

clean:
	@docker rm -f -v robots_txt-317604717

generate-img:
	@docker run -d --name robots_txt-317604717 robots_txt-317604717:latest
	@docker export robots_txt-317604717 -o vm.tar.gz
	@docker rm robots_txt-317604717
	@docker rmi robots_txt-317604717