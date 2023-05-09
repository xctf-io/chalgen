build:
	@docker build . -t fileshare-flask-8793343030011 -q

run: build
	@docker run -p 8081:8000 fileshare-flask-8793343030011

clean:
	@docker rm -f -v fileshare-flask-8793343030011

generate-img:
	@docker run -d --name fileshare-flask-8793343030011 fileshare-flask-8793343030011:latest
	@docker export fileshare-flask-8793343030011 -o vm.tar.gz
	@docker rm fileshare-flask-8793343030011
	@docker rmi fileshare-flask-8793343030011