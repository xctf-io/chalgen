build:
	@docker build . -t facebook-django-306548621 -q

run: build
	@docker run -p 8081:8000 facebook-django-306548621

clean:
	@docker rm -f -v facebook-django-306548621

generate-img:
	@docker run -d --name facebook-django-306548621 facebook-django-306548621:latest
	@docker export facebook-django-306548621 -o vm.tar.gz
	@docker rm facebook-django-306548621
	@docker rmi facebook-django-306548621