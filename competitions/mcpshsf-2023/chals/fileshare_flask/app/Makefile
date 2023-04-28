build:
	@docker build . -t fileshare-flask-302680321 -q

run: build
	@docker run -p 8081:8000 fileshare-flask-302680321

clean:
	@docker rm -f -v fileshare-flask-302680321

generate-img:
	@docker run -d --name fileshare-flask-302680321 fileshare-flask-302680321:latest
	@docker export fileshare-flask-302680321 -o vm.tar.gz
	@docker rm fileshare-flask-302680321
	@docker rmi fileshare-flask-302680321