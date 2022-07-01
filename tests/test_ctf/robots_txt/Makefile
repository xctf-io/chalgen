build:
	docker build . -t robots_txt-146373278769

run: build
	docker run -p 8080:80 robots_txt-146373278769

clean:
	docker rm -f -v robots_txt-146373278769

generate-img:
	docker run -d --name robots_txt-146373278769 robots_txt-146373278769:latest
	docker export robots_txt-146373278769 -o vm.tar.gz
	docker stop robots_txt-146373278769