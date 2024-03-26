# Variables
IMAGE_NAME := issdsmidterm
TAG := latest

# Build Docker image
build:
	docker build --pull --rm -f "MidtermProject\dockerfile" -t $(IMAGE_NAME):$(TAG) "MidtermProject"

# Run Docker container
run:
	docker run -p 8000:8000 $(IMAGE_NAME):$(TAG)
