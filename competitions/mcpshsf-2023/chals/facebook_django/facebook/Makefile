build:
	@docker build . -t facebook-django-8791529140815 -q

run: build
	@docker run -p 8081:8000 facebook-django-8791529140815

clean:
	@docker rm -f -v facebook-django-8791529140815

generate-img:
	@docker run -d --name facebook-django-8791529140815 facebook-django-8791529140815:latest
	@docker export facebook-django-8791529140815 -o vm.tar.gz
	@docker rm facebook-django-8791529140815
	@docker rmi facebook-django-8791529140815