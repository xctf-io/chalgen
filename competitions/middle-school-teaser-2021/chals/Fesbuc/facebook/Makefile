build:
	@docker build . -t facebook-django-307417861 -q

run: build
	@docker run -p 8081:8000 facebook-django-307417861

clean:
	@docker rm -f -v facebook-django-307417861

generate-img:
	@docker run -d --name facebook-django-307417861 facebook-django-307417861:latest
	@docker export facebook-django-307417861 -o vm.tar.gz
	@docker rm facebook-django-307417861
	@docker rmi facebook-django-307417861