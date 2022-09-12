default:
	echo $(args)
	docker run --rm -v $(shell pwd):/app bennythink/lipo-linux $(args)

docker:
	docker build -t bennythink/lipo-linux .
