build:
	@docker build . -t facebook-django-363759121 -q

run: build
	@docker run -p 8081:8000 facebook-django-363759121

clean:
	@docker rm -f -v facebook-django-363759121

generate-img:
	@docker run -d --name facebook-django-363759121 facebook-django-363759121:latest
	@docker export facebook-django-363759121 -o vm.tar.gz
	@docker rm facebook-django-363759121
	@docker rmi facebook-django-363759121