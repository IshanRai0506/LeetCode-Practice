# Write your MySQL query statement below
WITH ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY student_id, subject
               ORDER BY exam_date
           ) AS rn1,
           ROW_NUMBER() OVER (
               PARTITION BY student_id, subject
               ORDER BY exam_date DESC
           ) AS rn2
    FROM Scores
)

SELECT
    f.student_id,
    f.subject,
    f.score AS first_score,
    l.score AS latest_score
FROM ranked f
JOIN ranked l
    ON f.student_id = l.student_id
   AND f.subject = l.subject
WHERE f.rn1 = 1
  AND l.rn2 = 1
  AND l.score > f.score
ORDER BY f.student_id, f.subject;