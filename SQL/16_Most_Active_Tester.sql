---En aktif tester (Window Function), dense rank aynı değerde sıralamaya değer gelebilme ihtimali olduğu için kullanıldı

SELECT

    full_name,

    executed_tests,

    DENSE_RANK()

    OVER(

        ORDER BY executed_tests DESC

    ) AS tester_rank

FROM(

SELECT

    u.full_name,

    COUNT(t.testcase_id) AS executed_tests

FROM Users u

JOIN TestCases t

ON u.user_id=t.executed_by

GROUP BY u.full_name

);