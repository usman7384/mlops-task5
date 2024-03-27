# Use a lightweight web server image
FROM nginx:alpine

# Copy the HTML files to the nginx web server directory
COPY index.html /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start nginx when the container starts
CMD ["nginx", "-g", "daemon off;"]

