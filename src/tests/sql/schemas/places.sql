DROP TABLE IF EXISTS places; 

CREATE TABLE `places` (
  `city` varchar(96) COLLATE utf8mb4_general_ci NOT NULL,
  `county` varchar(96) COLLATE utf8mb4_general_ci NOT NULL,
  `country` varchar(48) COLLATE utf8mb4_general_ci NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `city` (`city`,`county`,`country`)
) ;