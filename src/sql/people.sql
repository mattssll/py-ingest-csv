DROP TABLE IF EXISTS people; 

CREATE TABLE `people` (
  `given_name` varchar(48) NOT NULL,
  `family_name` varchar(96) NOT NULL,
  `date_of_birth` varchar(32) NOT NULL,
  `place_of_birth` varchar(96) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `place_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `given_name` (`given_name`,`family_name`,`date_of_birth`,`place_of_birth`),
  KEY `place_id` (`place_id`),
  CONSTRAINT `people_ibfk_1` FOREIGN KEY (`place_id`) REFERENCES `places` (`id`)
) ;