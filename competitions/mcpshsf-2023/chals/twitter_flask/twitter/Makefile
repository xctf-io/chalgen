build:
	@docker build . -t twitter-302680849 -q

run: build
	@docker run -p 8081:5000 twitter-302680849

clean:
	@docker rm -f -v twitter-302680849

generate-img:
	@docker run -d --name twitter-302680849 twitter-302680849:latest
	@docker export twitter-302680849 -o vm.tar.gz
	@docker rm twitter-302680849
	@docker rmi twitter-302680849