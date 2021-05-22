#!/usr/bin/gawk -f

BEGIN	{
	record=1;
	}

	{size+=$NF
	if($7=="Raw_IP"){
	r+=1
	}
	else if($7=="UDP"){
	u+=1
	}
	else{
	icmp+=1
	}
	
	pkts=100*record;
	if($1==pkts){
	 type=(r>u && r>icmp)?"Raw_IP":(u>icmp)?"UDP":"ICMP";
	 split($2,tt,":");
	 secs = tt[2]*60+tt[3];
	 printf(pkts "," secs "," int( size/100 ) ","type "\n") >> "implement_att.csv";
	 record++;
	 size=0;
 	 icmp=r=u=0
 	 }
	}
