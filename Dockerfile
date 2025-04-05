# Use the latest Nginx image
FROM nginx:alpine
# Set the working directory
WORKDIR /opt
COPY ./index.html /usr/share/nginx/html/
COPY ./style.css /usr/share/nginx/html/
COPY ./script.js /usr/share/nginx/html/
# Expose the default Nginx HTTP port
EXPOSE 80
# Start the Nginx server
CMD ["nginx", "-g", "daemon off;"]
