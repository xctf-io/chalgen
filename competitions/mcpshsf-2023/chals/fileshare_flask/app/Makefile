build:
	@docker build . -t fileshare-flask-363772189 -q

run: build
	@docker run -p 8081:8000 fileshare-flask-363772189

clean:
	@docker rm -f -v fileshare-flask-363772189

generate-img:
	@docker run -d --name fileshare-flask-363772189 fileshare-flask-363772189:latest
	@docker export fileshare-flask-363772189 -o vm.tar.gz
	@docker rm fileshare-flask-363772189
	@docker rmi fileshare-flask-363772189