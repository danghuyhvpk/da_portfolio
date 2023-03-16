create table dim_customers as (
select 
	orders.customer_id as customer_id,
    orders.customer_name as customer_name,
    orders.segment as customer_segment,
    orders.country as country,
    orders.state as state,
    orders.`postal code` as postal_code,
    orders.region
from orders
group by Customer_id
)