build:
	@docker build . -t jekyll-blog-302685485 -q

run: build
	@docker run -p 8081:80 jekyll-blog-302685485

clean:
	@docker rm -f -v jekyll-blog-302685485

generate-img:
	@docker run -d --name jekyll-blog-302685485 jekyll-blog-302685485:latest
	@docker export jekyll-blog-302685485 -o vm.tar.gz
	@docker rm jekyll-blog-302685485
	@docker rmi jekyll-blog-302685485