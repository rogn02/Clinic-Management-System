-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 28, 2022 at 04:31 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `clinic_database`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `GetPatientInfo` (IN `fname` TEXT)   BEGIN
SELECT
p.f_name, p.l_name, p.age, p.join_date, p.leave_date
FROM
patient as p
WHERE p.f_name = fname ;
END$$

--
-- Functions
--
CREATE DEFINER=`root`@`localhost` FUNCTION `isEligible` (`age` INTEGER) RETURNS VARCHAR(20) CHARSET utf8mb4 DETERMINISTIC BEGIN
IF age > 18 THEN
RETURN ("yes");
ELSE
RETURN ("No");
END IF;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `billing_department`
--

CREATE TABLE `billing_department` (
  `b_id` varchar(5) NOT NULL,
  `b_date` date DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `p_id` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `billing_department`
--

INSERT INTO `billing_department` (`b_id`, `b_date`, `amount`, `p_id`) VALUES
('B0001', '2022-06-14', 20000, 'P0001'),
('B0002', '2022-06-09', 13000, 'P0002'),
('B0003', '2022-06-15', 4000, 'P0003'),
('B0004', '2022-11-10', 50000, 'P0004'),
('B0005', '2022-11-16', 100000, 'P0005');

-- --------------------------------------------------------

--
-- Table structure for table `caregiver`
--

CREATE TABLE `caregiver` (
  `cg_id` varchar(5) NOT NULL,
  `f_name` text DEFAULT NULL,
  `l_name` text DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `phno` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `caregiver`
--

INSERT INTO `caregiver` (`cg_id`, `f_name`, `l_name`, `age`, `phno`) VALUES
('CG001', 'karthik', 'dev', 28, '9513339775'),
('CG002', 'surya', 'teja', 40, '9678154571'),
('CG003', 'Lakshman', 'raju', 56, '8618517806'),
('CG004', 'Robu', 'khare', 38, '8073666498'),
('CG005', 'thaniya', 'shabeer', 50, '2782739127');

-- --------------------------------------------------------

--
-- Table structure for table `hospital`
--

CREATE TABLE `hospital` (
  `h_id` varchar(5) NOT NULL,
  `h_name` text DEFAULT NULL,
  `ref_doc` text DEFAULT NULL,
  `ref_date` date DEFAULT NULL,
  `p_f_name` text DEFAULT NULL,
  `p_l_name` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hospital`
--

INSERT INTO `hospital` (`h_id`, `h_name`, `ref_doc`, `ref_date`, `p_f_name`, `p_l_name`) VALUES
('H0001', 'Changanur Specialty Hospital', 'Dr. Ravi Krishna', '2022-03-01', 'Savithri', 'Jayalaskshmi'),
('H0002', 'Satva clinic', 'Dr. Hari Verma', '2022-05-12', 'Rijul', 'Saxena'),
('H0003', 'Brightstone Multispecialty Hospital', 'Dr. Aston James', '2021-09-01', 'Rohan', 'Shetty'),
('H0004', 'Aster Hospital', 'Dr. Aston James', '2022-01-08', 'Dhwani', 'bagr'),
('H0005', 'Brigade Hospital', 'Dr. David Thomas', '2021-01-04', 'sprenzia', 'nadar');

-- --------------------------------------------------------

--
-- Table structure for table `patient`
--

CREATE TABLE `patient` (
  `p_id` varchar(5) NOT NULL,
  `f_name` text DEFAULT NULL,
  `l_name` text DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `join_date` date DEFAULT NULL,
  `leave_date` date DEFAULT NULL,
  `ps_id` varchar(5) DEFAULT NULL,
  `cg_id` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient`
--

INSERT INTO `patient` (`p_id`, `f_name`, `l_name`, `age`, `join_date`, `leave_date`, `ps_id`, `cg_id`) VALUES
('P0001', 'Savithri', 'Jayalaskshmi', 12, '2022-03-01', '2022-06-14', 'PS001', 'CG001'),
('P0002', 'Rijul', 'Saxena', 15, '2022-05-12', '2022-06-09', 'PS003', 'CG002'),
('P0003', 'Rohan', 'Shetty', 14, '2021-09-01', '2022-06-15', 'PS002', 'CG003'),
('P0004', 'Dhwani', 'bagr', 12, '2022-01-08', '2022-11-10', 'PS005', 'CG003'),
('P0005', 'sprenzia', 'nadar', 17, '2021-01-04', '2022-11-16', 'PS004', 'CG004');

--
-- Triggers `patient`
--
DELIMITER $$
CREATE TRIGGER `before_insert_patient` BEFORE INSERT ON `patient` FOR EACH ROW BEGIN
IF NEW.age > 18 THEN SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'This database is only for minors';
END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `psychologist`
--

CREATE TABLE `psychologist` (
  `ps_id` varchar(5) NOT NULL,
  `f_name` text DEFAULT NULL,
  `l_name` text DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `phno` varchar(10) DEFAULT NULL,
  `salary` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `psychologist`
--

INSERT INTO `psychologist` (`ps_id`, `f_name`, `l_name`, `age`, `phno`, `salary`) VALUES
('PS001', 'rohan', 'mehta', 34, '9513339771', 2000000),
('PS002', 'Jamal', 'hari', 50, '9606154571', 25000),
('PS003', 'rishab', 'ravi', 48, '8618518026', 1500000),
('PS004', 'sudarshan', 'raj', 32, '8073666420', 1200000),
('PS005', 'rohan', 'lakshman', 47, '1234567899', 75000);

-- --------------------------------------------------------

--
-- Table structure for table `reference_department`
--

CREATE TABLE `reference_department` (
  `r_id` varchar(5) NOT NULL,
  `r_date` date DEFAULT NULL,
  `description` text DEFAULT NULL,
  `h_id` varchar(5) DEFAULT NULL,
  `ps_id` varchar(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `reference_department`
--

INSERT INTO `reference_department` (`r_id`, `r_date`, `description`, `h_id`, `ps_id`) VALUES
('R0001', '2022-03-01', 'This was a special case, a problematic case, so heavy that we needed electrocute that face.', 'H0001', 'PS001'),
('R0002', '2022-05-12', 'Heavy problems', 'H0002', 'PS003'),
('R0003', '2021-09-01', 'suicidal', 'H0003', 'PS002'),
('R0004', '2022-01-08', 'anxiety ', 'H0004', 'PS005'),
('R0005', '2021-01-04', 'anxiety', 'H0005', 'PS004');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `billing_department`
--
ALTER TABLE `billing_department`
  ADD PRIMARY KEY (`b_id`),
  ADD KEY `p_id` (`p_id`);

--
-- Indexes for table `caregiver`
--
ALTER TABLE `caregiver`
  ADD PRIMARY KEY (`cg_id`);

--
-- Indexes for table `hospital`
--
ALTER TABLE `hospital`
  ADD PRIMARY KEY (`h_id`);

--
-- Indexes for table `patient`
--
ALTER TABLE `patient`
  ADD PRIMARY KEY (`p_id`),
  ADD KEY `ps_id` (`ps_id`),
  ADD KEY `cg_id` (`cg_id`);

--
-- Indexes for table `psychologist`
--
ALTER TABLE `psychologist`
  ADD PRIMARY KEY (`ps_id`);

--
-- Indexes for table `reference_department`
--
ALTER TABLE `reference_department`
  ADD PRIMARY KEY (`r_id`),
  ADD KEY `ps_id` (`ps_id`),
  ADD KEY `h_id` (`h_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `billing_department`
--
ALTER TABLE `billing_department`
  ADD CONSTRAINT `billing_department_ibfk_1` FOREIGN KEY (`p_id`) REFERENCES `patient` (`p_id`);

--
-- Constraints for table `patient`
--
ALTER TABLE `patient`
  ADD CONSTRAINT `patient_ibfk_1` FOREIGN KEY (`ps_id`) REFERENCES `psychologist` (`ps_id`),
  ADD CONSTRAINT `patient_ibfk_2` FOREIGN KEY (`cg_id`) REFERENCES `caregiver` (`cg_id`);

--
-- Constraints for table `reference_department`
--
ALTER TABLE `reference_department`
  ADD CONSTRAINT `reference_department_ibfk_1` FOREIGN KEY (`ps_id`) REFERENCES `psychologist` (`ps_id`),
  ADD CONSTRAINT `reference_department_ibfk_2` FOREIGN KEY (`h_id`) REFERENCES `hospital` (`h_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
