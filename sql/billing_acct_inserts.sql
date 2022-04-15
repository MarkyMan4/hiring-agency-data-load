insert into agency_api_billingaccount (amt_paid, service_request_id)
select 
    0.00,
    id
from agency_api_servicerequest
order by id;
