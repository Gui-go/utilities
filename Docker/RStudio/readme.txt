



# Build the image
sudo docker build . -t rstudio-custom:v20210526
sudo docker build -t rstudio-custom:v20240428 -f dockerfile.rstudio .

# Check the images
sudo docker images

# Inspect the IMAGE ID of rstudio-custom:v20210526
docker inspect rstudio-custom:v20210526 --format '{{ .ID }}' | cut -f2- -d:

# Turn it into a container
sudo docker run -d -e PASSWORD=minhasenha -p 8787:8787 -v $(pwd):/home/rstudio/ --name=rstudio_custom_container 4fc3047afdf3647ab202f828f456e859d592ed8e523a25b562da015f315c79af

# Check what's up
docker ps
