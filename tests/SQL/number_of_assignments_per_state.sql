-- Write query to get number of assignments for each state
SELECT state,count(state)
from assignments
group by state
order by state