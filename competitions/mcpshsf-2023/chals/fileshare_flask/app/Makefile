build:
	@docker build . -t fileshare-flask-304547433 -q

run: build
	@docker run -p 8081:8000 fileshare-flask-304547433

clean:
	@docker rm -f -v fileshare-flask-304547433

generate-img:
	@docker run -d --name fileshare-flask-304547433 fileshare-flask-304547433:latest
	@docker export fileshare-flask-304547433 -o vm.tar.gz
	@docker rm fileshare-flask-304547433
	@docker rmi fileshare-flask-304547433