build:
	@docker build . -t facebook-django-306015941 -q

run: build
	@docker run -p 8081:8000 facebook-django-306015941

clean:
	@docker rm -f -v facebook-django-306015941

generate-img:
	@docker run -d --name facebook-django-306015941 facebook-django-306015941:latest
	@docker export facebook-django-306015941 -o vm.tar.gz
	@docker rm facebook-django-306015941
	@docker rmi facebook-django-306015941