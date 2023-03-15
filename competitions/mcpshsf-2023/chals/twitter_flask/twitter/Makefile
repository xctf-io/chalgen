build:
	@docker build . -t twitter-8791534468115 -q

run: build
	@docker run -p 8081:5000 twitter-8791534468115

clean:
	@docker rm -f -v twitter-8791534468115

generate-img:
	@docker run -d --name twitter-8791534468115 twitter-8791534468115:latest
	@docker export twitter-8791534468115 -o vm.tar.gz
	@docker rm twitter-8791534468115
	@docker rmi twitter-8791534468115