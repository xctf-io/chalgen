build:
	@docker build . -t jekyll-blog-8791128436280 -q

run: build
	@docker run -p 8081:80 jekyll-blog-8791128436280

clean:
	@docker rm -f -v jekyll-blog-8791128436280

generate-img:
	@docker run -d --name jekyll-blog-8791128436280 jekyll-blog-8791128436280:latest
	@docker export jekyll-blog-8791128436280 -o vm.tar.gz
	@docker rm jekyll-blog-8791128436280
	@docker rmi jekyll-blog-8791128436280