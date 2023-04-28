build:
	@docker build . -t facebook-django-302303001 -q

run: build
	@docker run -p 8081:8000 facebook-django-302303001

clean:
	@docker rm -f -v facebook-django-302303001

generate-img:
	@docker run -d --name facebook-django-302303001 facebook-django-302303001:latest
	@docker export facebook-django-302303001 -o vm.tar.gz
	@docker rm facebook-django-302303001
	@docker rmi facebook-django-302303001