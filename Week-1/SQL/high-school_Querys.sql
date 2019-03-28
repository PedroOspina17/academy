/*
4) List students and teachers for a given course. The output format should be:

 Course: <course-name>
 Teacher: <last-name>, <first-name>
 Students:
   <last-name>, <first-name> (ordered by alphabetically by last name)
*/ 
DECLARE @Course1 INT
SET @Course1 = 1
SELECT c.Name Course, t.lastName + ', ' + t.firstName Teacher, s.lastName + ', ' + s.firstName Student 
FROM Course c
INNER JOIN Person t ON c.AssignedTeacherId = t.DocumentId
INNER JOIN Enrollment e ON e.CourseId = e.CourseId
INNER JOIN Person s ON e.StudentId = s.DocumentId
WHERE c.Id = @Course1
ORDER BY s.lastName

/*
	5) Percentage of students that passed/failed a given course.
*/
DECLARE @Course2 INT
SET @Course2 = 1
SELECT c.Name Course, CONCAT(ROUND( COUNT(*)*100 /CONVERT(float,(SELECT COUNT(*) FROM Enrollment) ) , 2) ,' %')
FROM Enrollment e
INNER JOIN Course c ON e.CourseId = c.Id
WHERE Final >= 3 AND  c.Id = @Course2
GROUP BY c.Name

/*
	6) For a given teacher, list the timeline for each course that he is assigned to (ordered by date), and the course name. The format should be:

 Teacher: <last-name>, <first-name>
 Schedule:
   Monday 09:00 - 11:00: <course-name>
   Monday 15:00 - 17:30: <course-name>
   Friday 08:45 - 10:40: <course-name>

   
SELECT * FROM Person WHERE IsStudent = 0

*/

DECLARE @Teacher BIGINT
SET @Teacher = 951652844
SELECT t.lastName + ', ' + t.firstName Teacher,s.ClassDay + ' ' + ClassHours  +  ': ' + c.Name Schedule FROM Course c
INNER JOIN Schedule s ON c.Id = s.CourseId
INNER JOIN Person t ON c.AssignedTeacherId = t.DocumentId
WHERE c.AssignedTeacherId = @Teacher

