build:
	@docker build . -t facebook-django-8793343019015 -q

run: build
	@docker run -p 8081:8000 facebook-django-8793343019015

clean:
	@docker rm -f -v facebook-django-8793343019015

generate-img:
	@docker run -d --name facebook-django-8793343019015 facebook-django-8793343019015:latest
	@docker export facebook-django-8793343019015 -o vm.tar.gz
	@docker rm facebook-django-8793343019015
	@docker rmi facebook-django-8793343019015