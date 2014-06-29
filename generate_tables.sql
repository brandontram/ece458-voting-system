-- MySQL Script generated by MySQL Workbench
-- Tue Jun 24 22:44:08 2014
-- Model: New Model    Version: 1.0
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema VotingSystemDb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `VotingSystemDb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `VotingSystemDb` ;

-- -----------------------------------------------------
-- Table `VotingSystemDb`.`Persons`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `VotingSystemDb`.`Persons` (
  `personId` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  PRIMARY KEY (`personId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `VotingSystemDb`.`Candidates`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `VotingSystemDb`.`Candidates` (
  `candidateId` INT NOT NULL,
  `candidateName` VARCHAR(45) NULL,
  `candidateParty` VARCHAR(45) NULL,
  PRIMARY KEY (`candidateId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `VotingSystemDb`.`Kiosks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `VotingSystemDb`.`Kiosks` (
  `kioskId` INT NOT NULL,
  `location` VARCHAR(45) NULL,
  PRIMARY KEY (`kioskId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `VotingSystemDb`.`Elections`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `VotingSystemDb`.`Elections` (
  `electionId` INT NOT NULL,
  `candidateId` INT NOT NULL,
  `electionYear` VARCHAR(45) NULL,
  PRIMARY KEY (`electionId`, `candidateId`),
  INDEX `candidateId_idx` (`candidateId` ASC),
  CONSTRAINT `candidateId`
    FOREIGN KEY (`candidateId`)
    REFERENCES `VotingSystemDb`.`Candidates` (`candidateId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `VotingSystemDb`.`Votes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `VotingSystemDb`.`Votes` (
  `voteId` INT NOT NULL,
  `candidateId` INT NULL,
  `timestamp` DATETIME NULL,
  `kioskId` INT NULL,
  `voterId` INT NULL,
  `electionId` INT NULL,
  PRIMARY KEY (`voteId`),
  INDEX `idVoter_idx` (`voterId` ASC),
  INDEX `candidateId_idx` (`candidateId` ASC),
  INDEX `kioskId_idx` (`kioskId` ASC),
  INDEX `electionId_idx` (`electionId` ASC),
  CONSTRAINT `voterId`
    FOREIGN KEY (`voterId`)
    REFERENCES `VotingSystemDb`.`Persons` (`personId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `candidateId_votes`
    FOREIGN KEY (`candidateId`)
    REFERENCES `VotingSystemDb`.`Candidates` (`candidateId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `kioskId`
    FOREIGN KEY (`kioskId`)
    REFERENCES `VotingSystemDb`.`Kiosks` (`kioskId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `electionId`
    FOREIGN KEY (`electionId`)
    REFERENCES `VotingSystemDb`.`Elections` (`electionId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
