build:
	@docker build . -t facebook-django-309867125 -q

run: build
	@docker run -p 8081:8000 facebook-django-309867125

clean:
	@docker rm -f -v facebook-django-309867125

generate-img:
	@docker run -d --name facebook-django-309867125 facebook-django-309867125:latest
	@docker export facebook-django-309867125 -o vm.tar.gz
	@docker rm facebook-django-309867125
	@docker rmi facebook-django-309867125