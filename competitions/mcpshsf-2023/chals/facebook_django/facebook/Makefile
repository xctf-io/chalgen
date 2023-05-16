build:
	@docker build . -t facebook-django-8791128483339 -q

run: build
	@docker run -p 8081:8000 facebook-django-8791128483339

clean:
	@docker rm -f -v facebook-django-8791128483339

generate-img:
	@docker run -d --name facebook-django-8791128483339 facebook-django-8791128483339:latest
	@docker export facebook-django-8791128483339 -o vm.tar.gz
	@docker rm facebook-django-8791128483339
	@docker rmi facebook-django-8791128483339