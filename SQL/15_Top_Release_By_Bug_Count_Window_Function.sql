---En çok bug bulunan release (Window Function)

select release_name,
total_bugs,
rank() over( order by total_bugs desc) AS ranking

from (

select r.release_name,
	count (b.bug_id) AS total_bugs

from releases r 
join bugs b
on r.release_id=b.release_id
group by r.release_name

	);