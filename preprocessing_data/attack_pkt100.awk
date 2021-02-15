#!/usr/bin/gawk -f

BEGIN	{
	record=1;
	}

	{
	pkts=100*record;
	if($1==pkts){
	 split($2,tt,":");
	 secs = tt[2]*60+tt[3];
	 #split($0,tot," ")
	 printf(pkts "," secs "," $7 "," $(NF) "\n") >> "new_att_1.csv";
	 record++;
 	 }
	}
		


