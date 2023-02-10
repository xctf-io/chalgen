build:
	docker build . -t robots_txt-8781557980554

run: build
	docker run -p 8080:80 robots_txt-8781557980554

clean:
	docker rm -f -v robots_txt-8781557980554

generate-img:
	docker run -d --name robots_txt-8781557980554 robots_txt-8781557980554:latest
	docker export robots_txt-8781557980554 -o vm.tar.gz
	docker stop robots_txt-8781557980554