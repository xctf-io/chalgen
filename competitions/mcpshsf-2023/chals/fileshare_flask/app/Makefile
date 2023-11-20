build:
	@docker build  --platform linux/amd64 . -t fileshare-flask-343629477

run: build
	@docker run -p 8081:8000 fileshare-flask-343629477

clean:
	@docker rm -f -v fileshare-flask-343629477

generate-img:
	@docker run -d --name fileshare-flask-343629477 fileshare-flask-343629477:latest
	@docker export fileshare-flask-343629477 -o vm.tar.gz
	@docker rm fileshare-flask-343629477
	@docker rmi fileshare-flask-343629477