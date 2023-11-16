build:
	@docker build  --platform linux/amd64 . -t facebook-django-343478729

run: build
	@docker run -p 8081:8000 facebook-django-343478729

clean:
	@docker rm -f -v facebook-django-343478729

generate-img:
	@docker run -d --name facebook-django-343478729 facebook-django-343478729:latest
	@docker export facebook-django-343478729 -o vm.tar.gz
	@docker rm facebook-django-343478729
	@docker rmi facebook-django-343478729