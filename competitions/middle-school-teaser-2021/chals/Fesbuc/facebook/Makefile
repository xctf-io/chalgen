build:
	@docker build . -t facebook-django-8773403318056 -q

run: build
	@docker run -p 8081:8000 facebook-django-8773403318056

clean:
	@docker rm -f -v facebook-django-8773403318056

generate-img:
	@docker run -d --name facebook-django-8773403318056 facebook-django-8773403318056:latest
	@docker export facebook-django-8773403318056 -o vm.tar.gz
	@docker rm facebook-django-8773403318056
	@docker rmi facebook-django-8773403318056