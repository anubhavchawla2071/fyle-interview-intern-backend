-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
SELECT COUNT(*) AS num_grade_a
FROM assignments
WHERE teacher_id = (
    SELECT teacher_id
    FROM assignments
    WHERE grade IS NOT NULL
    GROUP BY teacher_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
  )
  AND grade = 'A';
