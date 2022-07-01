build:
	docker build . -t twitter-8786330985069

run: build
	docker run  twitter-8786330985069

clean:
	docker rm -f -v twitter-8786330985069

generate-img:
	docker run -d --name twitter-8786330985069 twitter-8786330985069:latest
	docker export twitter-8786330985069 -o vm.tar.gz
	docker stop twitter-8786330985069