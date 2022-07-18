DROP TABLE IF EXISTS peopleraw; 

CREATE TABLE `peopleraw` (
  `given_name` varchar(48) COLLATE utf8mb4_general_ci NOT NULL,
  `family_name` varchar(96) COLLATE utf8mb4_general_ci NOT NULL,
  `date_of_birth` date NOT NULL,
  `place_of_birth` varchar(96) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `given_name` (`given_name`,`family_name`,`date_of_birth`,`place_of_birth`),
  KEY `ix_peopleraw_place_of_birth` (`place_of_birth`)
) ;