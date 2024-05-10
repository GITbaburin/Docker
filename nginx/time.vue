services:
  frontend:
    build: ./frontend
    restart: always
    ports:
      - "3000:3000"
    volumes:
      - /app/node_modules   
      - ./frontend:/app
    environment:
      CHOKIDAR_USEPOLLING: "true"  
  api:
    build: ./api
    restart: always
    ports:
      - "5555:5000"
    volumes:
      - /app/node_modules
      - ./api:/app
    depends_on:
      - mysql
    environment:
      CHOKIDAR_USEPOLLING: "true" 