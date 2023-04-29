build:
	@docker build . -t facebook-django-304900889 -q

run: build
	@docker run -p 8081:8000 facebook-django-304900889

clean:
	@docker rm -f -v facebook-django-304900889

generate-img:
	@docker run -d --name facebook-django-304900889 facebook-django-304900889:latest
	@docker export facebook-django-304900889 -o vm.tar.gz
	@docker rm facebook-django-304900889
	@docker rmi facebook-django-304900889