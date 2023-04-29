build:
	@docker build . -t jekyll-blog-302476125 -q

run: build
	@docker run -p 8081:80 jekyll-blog-302476125

clean:
	@docker rm -f -v jekyll-blog-302476125

generate-img:
	@docker run -d --name jekyll-blog-302476125 jekyll-blog-302476125:latest
	@docker export jekyll-blog-302476125 -o vm.tar.gz
	@docker rm jekyll-blog-302476125
	@docker rmi jekyll-blog-302476125