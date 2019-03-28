CREATE TABLE Person(
	DocumentId BIGINT PRIMARY KEY,
	firstName VARCHAR(50), 
	lastName VARCHAR(50),	
	dateOfBirth DATE,
	IsStudent BIT
)
GO

CREATE TABLE Course(
	Id INT PRIMARY KEY IDENTITY(1,1),
	Name VARCHAR(50),
	AssignedTeacherId BIGINT FOREIGN KEY REFERENCES Person(DocumentId)	
)
GO

CREATE TABLE Schedule(
	Id INT PRIMARY KEY IDENTITY(1,1),
	CourseId INT FOREIGN KEY REFERENCES Course(Id),
	ClassDay VARCHAR(50),
	ClassHours VARCHAR(50),
)
GO

CREATE TABLE Enrollment(
	Id INT PRIMARY KEY IDENTITY(1,1),
	StudentId BIGINT FOREIGN KEY REFERENCES Person(DocumentId),
	CourseId INT FOREIGN KEY REFERENCES Course(Id),
	Note1 float,
	Note2 float,
	Note3 float,
	Final float
)
GO