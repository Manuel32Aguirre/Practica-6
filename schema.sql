-- ============================================
-- Schema SQL para el proyecto Menu
-- ============================================

-- Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS menu_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Usar la base de datos
USE menu_db;

-- Crear la tabla menu si no existe
CREATE TABLE IF NOT EXISTS menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    costo FLOAT NOT NULL,
    precio FLOAT NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    ingredientes VARCHAR(255),
    url_imagen VARCHAR(255),
    INDEX idx_tipo (tipo),
    INDEX idx_nombre (nombre)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ============================================
-- Datos de ejemplo (opcional - puedes comentar/borrar si no los necesitas)
-- ============================================

INSERT INTO menu (nombre, costo, precio, tipo, ingredientes, url_imagen) VALUES
('Tacos al Pastor', 25.00, 45.00, 'Platillo Principal', 'Tortilla, Carne de cerdo, Piña, Cilantro, Cebolla', 'https://example.com/tacos.jpg'),
('Quesadilla de Queso', 15.00, 30.00, 'Entrada', 'Tortilla, Queso Oaxaca', 'https://example.com/quesadilla.jpg'),
('Agua de Horchata', 8.00, 20.00, 'Bebida', 'Arroz, Canela, Azúcar', 'https://example.com/horchata.jpg'),
('Flan Napolitano', 12.00, 35.00, 'Postre', 'Leche, Huevos, Azúcar, Vainilla', 'https://example.com/flan.jpg')
ON DUPLICATE KEY UPDATE nombre=nombre;

-- ============================================
-- Fin del Schema
-- ============================================
