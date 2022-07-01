build:
	docker build . -t facebook-8778991352793

run: build
	docker run -p 8081:8000 facebook-8778991352793

clean:
	docker rm -f -v facebook-8778991352793

generate-img:
	docker run -d --name facebook-8778991352793 facebook-8778991352793:latest
	docker export facebook-8778991352793 -o vm.tar.gz
	docker stop facebook-8778991352793