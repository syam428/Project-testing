/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - e_commerce
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`e_commerce` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `e_commerce`;

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `shop_id` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `complaint` varchar(500) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  `date_time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`user_id`,`shop_id`,`type`,`complaint`,`reply`,`date_time`) values 
(25,1,'2','Products related','for electtrica issue','pending','2023-02-07 18:24:14'),
(26,5,'BM','BrightMart Website related','show unordered items in my ordered history','sorry machaa....okke seryaakki tharaaa','2023-02-07 20:37:00'),
(15,1,'1','Shop related','adsa','pending','2023-02-06 23:04:54'),
(16,1,'1','Products related','sd','pending','2023-02-06 23:05:10'),
(17,1,'1','Products related','sadsad','pending','2023-02-06 23:05:46'),
(18,1,'1','Shop related','qwertrew','pending','2023-02-06 23:06:02'),
(19,1,'2','Products related','cdsf','pending','2023-02-06 23:10:13'),
(20,1,'BM','Products related','ghghghg','pending','2023-02-06 23:14:35'),
(24,1,'1','Products related','For edumart issue','pending','2023-02-07 18:22:54'),
(21,1,'BM','Shop related','bad product ever!','pending','2023-02-07 17:45:49'),
(22,1,'1','Shop related','1111','pending','2023-02-07 17:48:47'),
(23,1,'2','Products related','1111111111111111111','pending','2023-02-07 17:49:01');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `user_type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`user_type`) values 
(1,'admin','admin','admin'),
(2,'edumart@gmail.com','edumart','shop'),
(3,'john@gmail.com','john','user'),
(4,'jessy@gmail.com','jessy','user'),
(5,'radhaKrishnan@gmail.com','radha','user'),
(6,'electrica@gmail.com','electrica','shop'),
(7,'jitheshkarathoor26@gmail.com','Apple123','user'),
(8,'zsdf@sd','As12345566778','pending'),
(9,'jitheshkarathoor@gmail.com','Apple123','shop');

/*Table structure for table `order_details` */

DROP TABLE IF EXISTS `order_details`;

CREATE TABLE `order_details` (
  `order_details_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_master_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `quantity` varchar(30) DEFAULT NULL,
  `amount` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`order_details_id`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=latin1;

/*Data for the table `order_details` */

insert  into `order_details`(`order_details_id`,`order_master_id`,`product_id`,`quantity`,`amount`) values 
(1,1,1,'35','140000'),
(2,2,1,'40','140000'),
(3,3,10,'34','14000'),
(4,4,1,'34','140000'),
(5,5,2,'34','55000'),
(6,6,2,'33','55000'),
(7,7,11,'33','78666'),
(8,8,3,'35','149'),
(9,9,1,'34','140000'),
(10,9,2,'21','55000'),
(11,10,1,'22','140000'),
(12,11,2,'20','55000'),
(13,12,1,'31','140000'),
(14,12,2,'21','55000'),
(15,13,1,'20','140000'),
(16,14,1,'21','140000'),
(17,15,1,'21','140000'),
(18,16,10,'11','14000'),
(19,16,3,'9','149'),
(20,16,1,'2','140000'),
(21,17,1,'9','140000'),
(22,18,1,'22','140000'),
(23,19,1,'1','140000'),
(24,19,2,'4','55000'),
(25,20,17,'3','1500000'),
(26,21,1,'1','140000'),
(27,22,2,'3','55000'),
(28,23,10,'8','14000'),
(29,24,18,'3','24000'),
(30,24,1,'1','140000');

/*Table structure for table `order_master` */

DROP TABLE IF EXISTS `order_master`;

CREATE TABLE `order_master` (
  `order_master_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `shop_id` int(11) DEFAULT NULL,
  `date_time` varchar(30) DEFAULT NULL,
  `total` varchar(30) DEFAULT NULL,
  `status` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`order_master_id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

/*Data for the table `order_master` */

insert  into `order_master`(`order_master_id`,`user_id`,`shop_id`,`date_time`,`total`,`status`) values 
(1,5,NULL,'2023-02-02 12:36:27',NULL,'delivered'),
(2,5,NULL,'2023-02-02 15:00:10',NULL,'delivered'),
(3,6,NULL,'2023-02-02 15:08:08',NULL,'delivered'),
(4,5,NULL,'2023-02-02 15:54:53',NULL,'delivered'),
(5,5,NULL,'2023-02-02 20:38:14',NULL,'delivered'),
(6,5,NULL,'2023-02-02 21:30:11',NULL,'Out For Delivery'),
(7,7,NULL,'2023-02-03 12:12:04',NULL,'Out For Delivery'),
(8,6,NULL,'2023-02-03 20:19:27',NULL,'Out For Delivery'),
(9,6,NULL,'2023-02-05 12:53:15',NULL,'Out For Delivery'),
(10,6,NULL,'2023-02-05 13:11:08',NULL,'Out For Delivery'),
(11,6,NULL,'2023-02-05 13:19:27',NULL,'Out For Delivery'),
(12,6,NULL,'2023-02-05 13:22:21',NULL,'Out For Delivery'),
(13,6,NULL,'2023-02-05 13:54:52',NULL,'Out For Delivery'),
(14,6,NULL,'2023-02-05 13:56:26',NULL,'Out For Delivery'),
(15,6,NULL,'2023-02-05 13:58:49',NULL,'Out For Delivery'),
(16,6,NULL,'2023-02-05 14:00:08',NULL,'Out For Delivery'),
(17,6,NULL,'2023-02-05 14:24:04',NULL,'Out For Delivery'),
(18,6,NULL,'2023-02-05 14:56:16',NULL,'Out For Delivery'),
(19,6,NULL,'2023-02-06 12:57:55',NULL,'paid'),
(20,1,NULL,'2023-02-06 18:09:47',NULL,'Out For Delivery'),
(21,1,NULL,'2023-02-06 19:34:17',NULL,'paid'),
(22,5,NULL,'2023-02-07 20:30:18',NULL,'paid'),
(23,5,NULL,'2023-02-07 20:32:40',NULL,'paid'),
(24,5,NULL,'2023-02-07 21:09:35',NULL,'Out For Delivery');

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) DEFAULT NULL,
  `shop_id` int(11) DEFAULT NULL,
  `product_name` varchar(30) DEFAULT NULL,
  `details` varchar(50) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `image` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`product_id`,`category_id`,`shop_id`,`product_name`,`details`,`price`,`image`) values 
(1,12,10,'Iphone 14 pro','Iphone 14 pro max','140000','static/5828573e-2c14-44c4-91f6-4827b051ab3eiphone.jpg'),
(2,2,10,'MSI Lap','New arrival','55000','static/dc504bf5-1dea-4dea-8b98-aaea2c5f5836msi.jpg'),
(3,13,10,'wall sticker','water proof and stainless','149','static/6295ef36-ea92-4207-9f00-617d796e6608sticker.jpg'),
(10,15,10,'Titan max q1','Military grade titan q1 ultra','14000','static/85749f55-0ffd-467b-b941-a42af2bb67b3titan.jpg'),
(17,12,1,'Iphone 14 pro','New I phone 14 pro','1500000','static/6dbaad47-a6ce-4ea2-a822-40c32298b690mob3.jpeg'),
(18,28,25,'fridge','Samsung\r\n','24000','static/6f9e9117-0bfd-4f1f-a86e-86504f7ea4fdfridge.avif'),
(15,25,10,'RealMe','Note X6','35000','static/0ec5c994-d68a-4e6f-a384-45a4b67234eb');

/*Table structure for table `product_category` */

DROP TABLE IF EXISTS `product_category`;

CREATE TABLE `product_category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;

/*Data for the table `product_category` */

insert  into `product_category`(`category_id`,`category_name`) values 
(28,'elecronics'),
(12,'Mobiles'),
(20,'Kitchen Items'),
(15,'Watches'),
(19,'Cosmetics');

/*Table structure for table `ratings` */

DROP TABLE IF EXISTS `ratings`;

CREATE TABLE `ratings` (
  `rating_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `rate` varchar(50) DEFAULT NULL,
  `review` varchar(500) DEFAULT NULL,
  `date_time` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`rating_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `ratings` */

insert  into `ratings`(`rating_id`,`user_id`,`product_id`,`rate`,`review`,`date_time`) values 
(1,5,1,'Excellent','wonderfull product',NULL),
(5,7,11,'Excellent','nice product','2023-02-03 12:12:27'),
(13,1,17,'Good','hah','2023-02-06 23:39:49'),
(14,5,18,'Good','uuuuu','2023-02-07 21:11:44'),
(12,1,17,'Excellent','Nice Product! Well packed and more over your customer support is amazing, thanku EduMart','2023-02-06 18:11:06');

/*Table structure for table `shop` */

DROP TABLE IF EXISTS `shop`;

CREATE TABLE `shop` (
  `shop_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `shop_name` varchar(20) DEFAULT NULL,
  `District` varchar(30) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `landmark` varchar(20) DEFAULT NULL,
  `phone` varchar(13) NOT NULL,
  `email` varchar(30) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`shop_id`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

/*Data for the table `shop` */

insert  into `shop`(`shop_id`,`login_id`,`shop_name`,`District`,`place`,`landmark`,`phone`,`email`,`status`) values 
(1,2,'Edumart','Thrissur','MN junction','Near shakthan','8765431456','edumart@gmail.com','Accepted'),
(2,6,'Electrica','Idukki','Vazhoor','Kamarattam','9876789898','electrica@gmail.com','Accepted'),
(10,27,'Amazon','Ernakulam','Kalamashery','Metro piller ','9876787654','amazon@gmail.com','Accepted'),
(24,8,'qwe','Kannur','adf','df','9999999999','zsdf@sd','pending'),
(25,9,'J and J','Malappuram','Tirur','Tirur','1234567890','jitheshkarathoor@gmail.com','Accepted'),
(21,45,'TedMart','Kozhikode','Town','Near KSRTC','8590762127','TedMart@gmail.com','pending'),
(17,38,'flipkart','Malappuram','Karathoor','Central','6754267731','flipkart@gmail.com','pending'),
(23,48,'Riss','Alappuzha','Punnamada','Finishing point','9496373730','Riss@gmail.com','pending');

/*Table structure for table `stocks` */

DROP TABLE IF EXISTS `stocks`;

CREATE TABLE `stocks` (
  `stock_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` int(11) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `date_time` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`stock_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `stocks` */

insert  into `stocks`(`stock_id`,`product_id`,`quantity`,`date_time`) values 
(1,1,'97','2023-02-06 12:56:46'),
(2,2,'9','2023-02-02 12:25:11'),
(3,3,'44','2023-02-02 14:23:15'),
(4,4,'0','2023-02-02 11:44:10'),
(5,11,'3999','2023-02-03 11:44:12'),
(11,17,'97','2023-02-06 18:09:09'),
(6,12,'0','2023-02-05 21:17:40'),
(7,13,'0','2023-02-05 21:17:42'),
(8,14,'0','2023-02-05 21:21:27'),
(9,15,'0','2023-02-05 21:23:02'),
(10,16,'0','2023-02-05 21:23:50'),
(12,18,'7','2023-02-07 21:08:00');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(30) DEFAULT NULL,
  `last_name` varchar(30) DEFAULT NULL,
  `house_name` varchar(30) DEFAULT NULL,
  `District` varchar(30) DEFAULT NULL,
  `place` varchar(30) DEFAULT NULL,
  `landmark` varchar(30) DEFAULT NULL,
  `pincode` varchar(30) DEFAULT NULL,
  `phone` varchar(30) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`first_name`,`last_name`,`house_name`,`District`,`place`,`landmark`,`pincode`,`phone`,`email`) values 
(1,3,'John','Manual','JM Vila','Calicut','Beach','West Hill','673655','9876543210','john@gmail.com'),
(2,4,'Jessy','Sam','Iris garden','Ernakulam','North Paravoor','Church','6543212','9896564332','jessy@gmail.com'),
(3,5,'RadhaKrishnan','M','Bavani Nivas','Kottayam','Varittiapra','West RB Plantation','6341257','9989778654','radhaKrishnan@gmail.com'),
(5,7,'jithesh','c p','chakkalaparabil(h)','Malappuram','Tirur','CSI mission hospital','676108','9495923285','jitheshkarathoor26@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
