




# bc - An arbitrary precision calculator language
used=$(free | grep Mem | awk {'print $3'})
available=$(free | grep Mem | awk {'print $2'})
result=`echo $used / $available | bc -l` 
echo $result
