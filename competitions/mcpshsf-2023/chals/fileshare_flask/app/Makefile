build:
	@docker build . -t fileshare-flask-8791529069716 -q

run: build
	@docker run -p 8081:8000 fileshare-flask-8791529069716

clean:
	@docker rm -f -v fileshare-flask-8791529069716

generate-img:
	@docker run -d --name fileshare-flask-8791529069716 fileshare-flask-8791529069716:latest
	@docker export fileshare-flask-8791529069716 -o vm.tar.gz
	@docker rm fileshare-flask-8791529069716
	@docker rmi fileshare-flask-8791529069716