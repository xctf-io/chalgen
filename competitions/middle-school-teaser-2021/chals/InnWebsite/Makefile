build:
	@docker build . -t static_site-306012093 -q

run: build
	@docker run -p 8080:80 static_site-306012093

clean:
	@docker rm -f -v static_site-306012093

generate-img:
	@docker run -d --name static_site-306012093 static_site-306012093:latest
	@docker export static_site-306012093 -o vm.tar.gz
	@docker rm static_site-306012093
	@docker rmi static_site-306012093