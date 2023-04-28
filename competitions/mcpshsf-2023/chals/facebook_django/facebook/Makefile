build:
	@docker build . -t facebook-django-302686057 -q

run: build
	@docker run -p 8081:8000 facebook-django-302686057

clean:
	@docker rm -f -v facebook-django-302686057

generate-img:
	@docker run -d --name facebook-django-302686057 facebook-django-302686057:latest
	@docker export facebook-django-302686057 -o vm.tar.gz
	@docker rm facebook-django-302686057
	@docker rmi facebook-django-302686057