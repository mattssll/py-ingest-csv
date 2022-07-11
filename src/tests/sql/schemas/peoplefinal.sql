DROP TABLE IF EXISTS peoplefinal; 

CREATE TABLE `peoplefinal` (
  `given_name` varchar(48) COLLATE utf8mb4_general_ci NOT NULL,
  `family_name` varchar(96) COLLATE utf8mb4_general_ci NOT NULL,
  `date_of_birth` date NOT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `place_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `place_id` (`place_id`),
  CONSTRAINT `peoplefinal_ibfk_1` FOREIGN KEY (`place_id`) REFERENCES `places` (`id`)
) ;