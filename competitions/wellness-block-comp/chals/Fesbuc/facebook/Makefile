build:
	@docker build . -t facebook-django-379461261

run: build
	@docker run -p 8081:8000 facebook-django-379461261

clean:
	@docker rm -f -v facebook-django-379461261

generate-img:
	@docker run -d --name facebook-django-379461261 facebook-django-379461261:latest
	@docker export facebook-django-379461261 -o vm.tar.gz
	@docker rm facebook-django-379461261
	@docker rmi facebook-django-379461261