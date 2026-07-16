---CTE (Common Table Expression - WITH) kullanımı, geçici tablo oluşturma

WITH ReleaseSummary AS(

SELECT

    release_id,

    COUNT(*) AS total_bugs

FROM Bugs

GROUP BY release_id

)

SELECT

    r.release_name,

    rs.total_bugs

FROM ReleaseSummary rs

JOIN Releases r

ON rs.release_id=r.release_id

ORDER BY rs.total_bugs DESC;