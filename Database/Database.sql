-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: student_data
-- ------------------------------------------------------
-- Server version	8.0.34

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `emp_id` varchar(20) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `emp_id` (`emp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
INSERT INTO `admins` VALUES (1,'Admin','Adm@#321','Shiva','101','2024-05-07 11:38:14'),(2,'Shivaa','Shiv@#$1','Shivvva','102','2024-05-07 15:02:57'),(3,'Don','Don@311w','DonDON','103','2024-05-07 15:55:21'),(4,'YTsv','YTfs@314','Ytsfsg','10342','2024-05-07 16:00:40'),(6,'Yadhd','yavD#422','Yadha','107','2024-05-07 16:21:21'),(7,'Ajay','Aga@#112','Ajay A','103421','2024-05-13 02:26:26');
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `dep` varchar(50) DEFAULT NULL,
  `course` varchar(50) DEFAULT NULL,
  `year1` int DEFAULT NULL,
  `sem` varchar(10) DEFAULT NULL,
  `id` int NOT NULL,
  `sname` varchar(100) DEFAULT NULL,
  `usn` varchar(20) NOT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `paddress` varchar(255) DEFAULT NULL,
  `taddress` varchar(255) DEFAULT NULL,
  `photo` varchar(50) DEFAULT NULL,
  `deg` varchar(100) DEFAULT NULL,
  `graduYear` varchar(10) DEFAULT NULL,
  `cgpa` decimal(3,2) DEFAULT NULL,
  `awards` varchar(200) DEFAULT NULL,
  `projTitle` varchar(255) DEFAULT NULL,
  `projDesc` varchar(500) DEFAULT NULL,
  `projGrade` varchar(20) DEFAULT NULL,
  `internCom` varchar(100) DEFAULT NULL,
  `internDur` varchar(10) DEFAULT NULL,
  `internRole` varchar(100) DEFAULT NULL,
  `extraCurri` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('CSE','2020',4,'8',2900,'shashank','4hg20cs024','Male','sghh@gmail.com','9700777542','ghkss,djjd','ghkss,djjd','','BE','2020-2024',6.75,'best stud','Photo Based Student Information Retrivel System','PBSIR System','A','Web Tech.','30 Days','Intern','Active in Studying new Things!!'),('CSE','2020',4,'8',2901,'shashank','4HG20CS025','Male','sghh@gmail.com','9700777542','ghkss,djjd','ghkss,djjd','','Select Degree','2020-2024',6.75,'best stud','Photo Based Student Information Retrivel System','PBSIR System','A','Web Tech.','60 Days','Interns','Active in SJUIYCC GHK'),('CSE','2020',3,'6',2907,'shashank','4hg20cs025','Female','sghh@gmail.com','9700777542','ghkss,djjd','ghkss,djjd','','BE','2020-2024',6.75,'best stud','Photo Based Student Information Retrivel System','PBSIR System','A','Web Tech.','30 Days','Intern',''),('CSE','2020',4,'8',2909,'shashank','4hg20cs025','Female','sghh@gmail.com','9700777542','ghkss,djjd','ghkss,djjd','','BE','2020-2024',6.75,'best stud','Photo Based Student Information Retrivel System','PBSIR System','A','Web Tech.','30 Days','Intern','./PP[-9= JKBG,'),('CSE','2020',3,'6',2911,'Arjun','4hg20cs025','Male','Arjun@gmail.com','7542638829','fgataaj.aaka','fgataaj.aaka','','BE','2020-2024',6.92,'best stud','face System Information Retrivel System','face System','A','Arc.','30 Days','Intern','Active in Studying new Things!!'),('CSE','2021',3,'6',29021,'shashank','4HG20CS029','Female','sghh@gmail.com','97007775422','ghkss,djjd','ghkss,djjd','','BE','2020-2024',6.75,'best stud','Photo Based Student Information Retrivel System','PBSIR System','A','Web Tech.','30 Days','Intern',''),('CSE','2020',4,'8',290032,'shashank','4HG20CS024','Male','sghh@gmail.com','9700777542','ghkss,djjd','ghkss,djjd','','BE','2020-2024',6.75,'best stud','Photo Based Student Information Retrivel System','PBSIR System','A','Web Tech.','30 Days','Intern','Active in Studying new Things!!'),('CSE','2021',2,'4',290164,'shashank','4HG20CS074','Male','sghh@gmail.com','9700777542','ghkss,djjd','ghkss,djjd','1','BE','2020-2024',6.75,'best stud','Photo Based Student Information Retrivel System','PBSIR System','A','Web Tech.','60 Days','Intern','Active in SJUIYCC GHK'),('CSE','2021',4,'8',2902111,'shashank','4HG20CS492','Female','sghh@gmail.com','9700798249','ghkss,djjd','ghkss,djjd','','BE','2020-2024',6.75,'best stud','Photo Based Student Information Retrivel System','PBSIR System','A','Web Tech.','30 Days','Intern',''),('CSE','2021',3,'6',2902112,'Suresh','4HG20CS024','Male','sghh@gmail.com','9700777542','ghkss,djjd','ghkss,djjd','','BE','2020-2024',6.75,'best stud','Photo Based Student Information Retrivel System','PBSIR System','A','Web Tech.','30 Days','Intern','Active in Studying new Things!!'),('CSE','2020',4,'8',48700001,'Shivaraddi','4HG22CS492','Male','shiva@gmail.com','9700797189','ghkss,djjd','ghkss,djjd','','BE','2020-2024',6.75,'best stud','Photo Based Student Information Retrivel System','PBSIR System','A','Web Tech.','30 Days','Intern','Active New Things!!'),('CSE','2020',4,'8',48700002,'Shiva R M','4HG22CS072','Male','shiva@gmail.com','9700787189','ghkss,djjd','ghkss,djjd','','BE','2020-2024',6.89,'best stud','PBSIRS','PBSIR System','A','Web Tech.','30 Days','Intern','Active New Things!!');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_info`
--

DROP TABLE IF EXISTS `student_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_info` (
  `dep` varchar(45) DEFAULT NULL,
  `course` varchar(45) DEFAULT NULL,
  `year` varchar(20) DEFAULT NULL,
  `semester` varchar(45) DEFAULT NULL,
  `id` int NOT NULL,
  `name` varchar(80) DEFAULT NULL,
  `usn` varchar(10) NOT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `p_address` varchar(200) DEFAULT NULL,
  `t_address` varchar(200) DEFAULT NULL,
  `photo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_info`
--

LOCK TABLES `student_info` WRITE;
/*!40000 ALTER TABLE `student_info` DISABLE KEYS */;
INSERT INTO `student_info` VALUES ('CSE','2020','4','8',2,'Shivaraddi','4HG20CS067','Male','rama@gmail.com','9876543211','Bharath','hksuiiaa',''),('CSE','2021','4','8',4,'Shivaraddi R M','4HG20CS024','Male','Ramm@gmail.com','9876541010','Bharat','fgauiaak',''),('CSE','2020','4','8',48700001,'Shivaraddi R. M','4HG21CS022','Male','rama@gmail.com','9876543121','India','Karnataka, India','1'),('CSE','2021','3','6',48700002,'Harsha','4HG20CS402','Male','ramm@gmail.com','8737100320','India','fgauiaak',''),('CSE','2021','3','6',48700003,'Shivaraddi','4HG20CS410','Male','raamm@gmail.com','9817841017','India','fgauiaak','1'),('CSE','2022','2','4',48700004,'Harsha H k','4HG20CS412','Male','ramm@gmail.com','8737100320','India','fgauiaak','1'),('CSE','2020','4','8',48700005,'Savitri','4HG21CS426','Female','savitri@gmail.com','4446366666','haauua','akkiaiia','1'),('CSE','2020','4','8',48700006,'Prakruthi H K','4HG20CS017','Female','prakruthi@gmail.com','3434444243','gajualJJSYA','yyyyyy','1'),('CSE','2021','4','8',48700007,'Indushree K T','4HG21CS410','Female','indushree@gmail.com','7777777262','abcdkak','yyyyy','1');
/*!40000 ALTER TABLE `student_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `name` varchar(100) NOT NULL,
  `usn` varchar(10) NOT NULL,
  `student_id` int NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `usn` (`usn`),
  UNIQUE KEY `student_id` (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Shiva','Shiv@311','Shivaraddi','4HG20CS024',48700001,'2024-05-07 10:16:10'),(2,'asd','Asd!1234','ASDD','4HG21CV000',48700002,'2024-05-08 17:02:22'),(3,'Ram','Ram@3211','Ramesh','4HG22CS411',48700003,'2024-05-10 05:37:18'),(4,'Shaua','Shi@#322','Shambu','4HG21CS021',48700004,'2024-05-11 17:15:04');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-29 21:58:56
