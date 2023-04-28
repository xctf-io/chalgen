build:
	@docker build . -t facebook-django-304554977 -q

run: build
	@docker run -p 8081:8000 facebook-django-304554977

clean:
	@docker rm -f -v facebook-django-304554977

generate-img:
	@docker run -d --name facebook-django-304554977 facebook-django-304554977:latest
	@docker export facebook-django-304554977 -o vm.tar.gz
	@docker rm facebook-django-304554977
	@docker rmi facebook-django-304554977