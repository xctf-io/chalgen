build:
	@docker build . -t twitter-8793343616898 -q

run: build
	@docker run -p 8081:5000 twitter-8793343616898

clean:
	@docker rm -f -v twitter-8793343616898

generate-img:
	@docker run -d --name twitter-8793343616898 twitter-8793343616898:latest
	@docker export twitter-8793343616898 -o vm.tar.gz
	@docker rm twitter-8793343616898
	@docker rmi twitter-8793343616898