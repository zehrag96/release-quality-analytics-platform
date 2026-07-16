--Her release için kapanan bug oranını hesaplamak.
SELECT
r.release_name,
count(b.bug_id) AS total_bug,

sum( 
	CASE	
		When b.status='Closed' Then 1
		Else 0
	END
) AS closed_bugs,

round (
	100.0 *
	sum ( CASE WHEN b.status='Closed' Then 1 Else 0 END )
	/ 
	count(b.bug_id),
	2
) AS closure_rate

from Releases r
join 
Bugs b
on r.release_id=b.release_id
group by r.release_name;
