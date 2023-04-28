build:
	@docker build . -t fileshare-flask-302367349 -q

run: build
	@docker run -p 8081:8000 fileshare-flask-302367349

clean:
	@docker rm -f -v fileshare-flask-302367349

generate-img:
	@docker run -d --name fileshare-flask-302367349 fileshare-flask-302367349:latest
	@docker export fileshare-flask-302367349 -o vm.tar.gz
	@docker rm fileshare-flask-302367349
	@docker rmi fileshare-flask-302367349