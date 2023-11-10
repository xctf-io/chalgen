build:
	@docker build . -t facebook-django-377491353

run: build
	@docker run -p 8081:8000 facebook-django-377491353

clean:
	@docker rm -f -v facebook-django-377491353

generate-img:
	@docker run -d --name facebook-django-377491353 facebook-django-377491353:latest
	@docker export facebook-django-377491353 -o vm.tar.gz
	@docker rm facebook-django-377491353
	@docker rmi facebook-django-377491353