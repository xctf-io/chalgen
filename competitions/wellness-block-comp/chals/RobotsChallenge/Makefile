build:
<<<<<<< Updated upstream
	@docker build . -t robots_txt-382981361
=======
	@docker build  --platform linux/amd64 . -t robots_txt-8749441840621 -q
>>>>>>> Stashed changes

run: build
	@docker run -p 8080:80 robots_txt-382981361

clean:
	@docker rm -f -v robots_txt-382981361

generate-img:
	@docker run -d --name robots_txt-382981361 robots_txt-382981361:latest
	@docker export robots_txt-382981361 -o vm.tar.gz
	@docker rm robots_txt-382981361
	@docker rmi robots_txt-382981361