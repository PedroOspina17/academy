SELECT c.Name Course, t.lastName + ', ' + t.firstName Teacher, s.lastName + ', ' + s.firstName Student 
FROM Course c
INNER JOIN Person t ON c.AssignedTeacherId = t.DocumentId
INNER JOIN Enrollment e ON e.CourseId = e.CourseId
INNER JOIN Person s ON e.StudentId = s.DocumentId
ORDER BY s.lastName


SELECT c.Name Course, ROUND( COUNT(*)*100 /CONVERT(float,(SELECT COUNT(*) FROM Enrollment) ) , 2) 
FROM Enrollment e
INNER JOIN Course c ON e.CourseId = c.Id
WHERE Final >= 3
GROUP BY c.Name

