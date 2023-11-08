build:
	@docker build . -t facebook-django-8758950106656

run: build
	@docker run -p 8081:8000 facebook-django-8758950106656

clean:
	@docker rm -f -v facebook-django-8758950106656

generate-img:
	@docker run -d --name facebook-django-8758950106656 facebook-django-8758950106656:latest
	@docker export facebook-django-8758950106656 -o vm.tar.gz
	@docker rm facebook-django-8758950106656
	@docker rmi facebook-django-8758950106656