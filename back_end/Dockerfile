# Use an official Python runtime as an image
FROM nikolaik/python-nodejs:python3.6-nodejs12
# The EXPOSE instruction indicates the ports on which a container 
# will listen for connections
# Since Flask apps listen to port 5000  by default, we expose it
EXPOSE 5000

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction 
# creates a directory with this name if it doesn’t exist
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

WORKDIR /app/app/templates
#COPY /app/templates/package*.json ./
RUN npm install
# Run app.py when the container launches
WORKDIR /app
RUN git clone https://github.com/vishnubob/wait-for-it.git
CMD ["flask", "run", "--host=0.0.0.0"]