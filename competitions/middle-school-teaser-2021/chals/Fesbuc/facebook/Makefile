build:
	@docker build . -t facebook-django-304889537 -q

run: build
	@docker run -p 8081:8000 facebook-django-304889537

clean:
	@docker rm -f -v facebook-django-304889537

generate-img:
	@docker run -d --name facebook-django-304889537 facebook-django-304889537:latest
	@docker export facebook-django-304889537 -o vm.tar.gz
	@docker rm facebook-django-304889537
	@docker rmi facebook-django-304889537