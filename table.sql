CREATE DATABASE `stori` /*!40100 DEFAULT CHARACTER SET utf8 */

CREATE TABLE `transaction` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `created_at` DATETIME NOT NULL,
  `amount` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_date` (`created_at`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
