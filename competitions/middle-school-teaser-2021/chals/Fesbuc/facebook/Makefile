build:
	@docker build . -t facebook-django-317590381 -q

run: build
	@docker run -p 8081:8000 facebook-django-317590381

clean:
	@docker rm -f -v facebook-django-317590381

generate-img:
	@docker run -d --name facebook-django-317590381 facebook-django-317590381:latest
	@docker export facebook-django-317590381 -o vm.tar.gz
	@docker rm facebook-django-317590381
	@docker rmi facebook-django-317590381