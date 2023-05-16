build:
	@docker build . -t twitter-8791129116084 -q

run: build
	@docker run -p 8081:5000 twitter-8791129116084

clean:
	@docker rm -f -v twitter-8791129116084

generate-img:
	@docker run -d --name twitter-8791129116084 twitter-8791129116084:latest
	@docker export twitter-8791129116084 -o vm.tar.gz
	@docker rm twitter-8791129116084
	@docker rmi twitter-8791129116084