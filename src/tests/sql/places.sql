DROP TABLE IF EXISTS places; 

CREATE TABLE `places` (
  `city` varchar(96) NOT NULL,
  `county` varchar(96) NOT NULL,
  `country` varchar(48) NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `city` (`city`,`county`,`country`)
) ;