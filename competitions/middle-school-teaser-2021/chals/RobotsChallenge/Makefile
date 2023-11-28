build:
	@docker build  --platform linux/amd64 . -t robots_txt-8737151509766

run: build
	@docker run -p 8080:80 robots_txt-8737151509766

clean:
	@docker rm -f -v robots_txt-8737151509766

generate-img:
	@docker run -d --name robots_txt-8737151509766 robots_txt-8737151509766:latest
	@docker export robots_txt-8737151509766 -o vm.tar.gz
	@docker rm robots_txt-8737151509766
	@docker rmi robots_txt-8737151509766