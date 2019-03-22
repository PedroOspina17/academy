INSERT INTO Course(Name, AssignedTeacherId) VALUES ('Mathematics', 48156552)
INSERT INTO Course(Name, AssignedTeacherId) VALUES ('English', 951652844)
INSERT INTO Course(Name, AssignedTeacherId) VALUES ('Computers', 3215465255)
GO

INSERT INTO Schedule(CourseId, ClassDay, ClassHours) VALUES (1, 'Monday', '09:00 - 11:00')
INSERT INTO Schedule(CourseId, ClassDay, ClassHours) VALUES (1, 'Monday', '16:00 - 19:00')
INSERT INTO Schedule(CourseId, ClassDay, ClassHours) VALUES (2, 'Friday', '06:00 - 10:00')
INSERT INTO Schedule(CourseId, ClassDay, ClassHours) VALUES (2, 'Friday', '12:00 - 15:00')
INSERT INTO Schedule(CourseId, ClassDay, ClassHours) VALUES (3, 'Monday', '06:00 - 08:00')
INSERT INTO Schedule(CourseId, ClassDay, ClassHours) VALUES (3, 'Friday', '06:00 - 08:00')
INSERT INTO Schedule(CourseId, ClassDay, ClassHours) VALUES (3, 'Saturday', '08:00 - 10:00')
GO
