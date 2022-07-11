DROP TABLE IF EXISTS peopleraw; 

CREATE TABLE `peopleraw` (
  `given_name` varchar(48) NOT NULL,
  `family_name` varchar(96) NOT NULL,
  `date_of_birth` varchar(32) NOT NULL,
  `place_of_birth` varchar(96) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `given_name` (`given_name`,`family_name`,`date_of_birth`,`place_of_birth`),
  KEY `ix_peopleraw_place_of_birth` (`place_of_birth`)
) ;