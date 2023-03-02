


-- In the master database context, execute the following command to add a new server-level firewall rule:
Execute sp_set_firewall_rule @name = N'Work',
@start_ip_address = '115.118.1.0',
@end_ip_address = '115.118.16.255'


-- To delete firewall_rule
Execute sp_delete_firewall_rule @name= N'Work'



SELECT DB_NAME()
SELECT GETDATE()
SELECT USER_NAME()

