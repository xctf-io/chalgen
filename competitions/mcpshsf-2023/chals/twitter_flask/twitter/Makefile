build:
	@docker build . -t twitter-363773801 -q

run: build
	@docker run -p 8081:5000 twitter-363773801

clean:
	@docker rm -f -v twitter-363773801

generate-img:
	@docker run -d --name twitter-363773801 twitter-363773801:latest
	@docker export twitter-363773801 -o vm.tar.gz
	@docker rm twitter-363773801
	@docker rmi twitter-363773801