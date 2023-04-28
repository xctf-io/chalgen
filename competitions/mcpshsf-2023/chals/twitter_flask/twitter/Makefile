build:
	@docker build . -t twitter-304562497 -q

run: build
	@docker run -p 8081:5000 twitter-304562497

clean:
	@docker rm -f -v twitter-304562497

generate-img:
	@docker run -d --name twitter-304562497 twitter-304562497:latest
	@docker export twitter-304562497 -o vm.tar.gz
	@docker rm twitter-304562497
	@docker rmi twitter-304562497