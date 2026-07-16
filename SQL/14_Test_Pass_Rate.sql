---Her release'in test başarı oranını hesaplamak.

select r.release_name,
	count (t.testcase_id) AS total_tests,
	
	SUM (
		CASE WHEN t.status='Passed' Then 1 Else 0 END) AS passed_tests,
		
	round ( 100.0 * sum (CASE WHEN t.status='Passed' Then 1 Else 0 END) / count(t.testcase_id), 2 ) AS pass_rate


from releases r
join TestCases t
on r.release_id=t.release_id
group by r.release_name;