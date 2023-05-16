build:
	@docker build . -t fileshare-flask-8791128532902 -q

run: build
	@docker run -p 8081:8000 fileshare-flask-8791128532902

clean:
	@docker rm -f -v fileshare-flask-8791128532902

generate-img:
	@docker run -d --name fileshare-flask-8791128532902 fileshare-flask-8791128532902:latest
	@docker export fileshare-flask-8791128532902 -o vm.tar.gz
	@docker rm fileshare-flask-8791128532902
	@docker rmi fileshare-flask-8791128532902