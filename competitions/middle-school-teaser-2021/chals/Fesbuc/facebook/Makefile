build:
	@docker build . -t facebook-django-312225445 -q

run: build
	@docker run -p 8081:8000 facebook-django-312225445

clean:
	@docker rm -f -v facebook-django-312225445

generate-img:
	@docker run -d --name facebook-django-312225445 facebook-django-312225445:latest
	@docker export facebook-django-312225445 -o vm.tar.gz
	@docker rm facebook-django-312225445
	@docker rmi facebook-django-312225445