# Get the NodeJS Erbium image from DockerHub
FROM node:12

# set working directory
WORKDIR /App

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# copy lock files to App
COPY package.json /App/
COPY yarn.lock /App/

# install app dependencies
RUN npm i && npm -g install react-scripts 

# add app
COPY . /App/

# start app
CMD ["yarn", "start"]