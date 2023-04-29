build:
	@docker build . -t fileshare-flask-302453609 -q

run: build
	@docker run -p 8081:8000 fileshare-flask-302453609

clean:
	@docker rm -f -v fileshare-flask-302453609

generate-img:
	@docker run -d --name fileshare-flask-302453609 fileshare-flask-302453609:latest
	@docker export fileshare-flask-302453609 -o vm.tar.gz
	@docker rm fileshare-flask-302453609
	@docker rmi fileshare-flask-302453609