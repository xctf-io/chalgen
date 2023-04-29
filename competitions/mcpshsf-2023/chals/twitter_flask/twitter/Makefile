build:
	@docker build . -t twitter-304898973 -q

run: build
	@docker run -p 8081:5000 twitter-304898973

clean:
	@docker rm -f -v twitter-304898973

generate-img:
	@docker run -d --name twitter-304898973 twitter-304898973:latest
	@docker export twitter-304898973 -o vm.tar.gz
	@docker rm twitter-304898973
	@docker rmi twitter-304898973