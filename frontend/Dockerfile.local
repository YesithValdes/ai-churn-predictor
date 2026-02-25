# 1. Imagen base de Node
FROM node:20-alpine

WORKDIR /app

# 2. Copiamos archivos de dependencias
COPY package.json package-lock.json* ./

# 3. Instalamos dependencias
RUN npm install

# 4. Copiamos el resto del código
COPY . .

# 5. Exponemos el puerto de Next.js
EXPOSE 3000

# 6. Modo desarrollo (para que veas los cambios en vivo)
CMD ["npm", "run", "dev"]