build:
	@docker build  --platform linux/amd64 . -t twitter-343512469

run: build
	@docker run -p 8081:5000 twitter-343512469

clean:
	@docker rm -f -v twitter-343512469

generate-img:
	@docker run -d --name twitter-343512469 twitter-343512469:latest
	@docker export twitter-343512469 -o vm.tar.gz
	@docker rm twitter-343512469
	@docker rmi twitter-343512469