build:
	@docker build . -t twitter-302324477 -q

run: build
	@docker run -p 8081:5000 twitter-302324477

clean:
	@docker rm -f -v twitter-302324477

generate-img:
	@docker run -d --name twitter-302324477 twitter-302324477:latest
	@docker export twitter-302324477 -o vm.tar.gz
	@docker rm twitter-302324477
	@docker rmi twitter-302324477