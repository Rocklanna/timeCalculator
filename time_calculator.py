def add_time(start, duration, startday="none"):
  new_time="";
  newtime_ampm="";
  am_pm={
    "AM":"PM",
    "PM":"AM"
  }
  days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
  start_day=startday.lower();
  start_day=start_day[0:1].upper()+start_day[1:];
  index_day=0;
  count=0;
  startdivider= start.index(":");
  starthrs=int(start[0:startdivider]);
  startmins = int(start[startdivider+1:startdivider+3]);
  divider =duration.index(":");
  addhrs = int(duration[0:divider]);
  addmins = int(duration[divider+1:]);
  totalhrs=starthrs+addhrs;
  totalmins=startmins+addmins
  newtime_ampm=start[-2:];
  if(totalhrs%2!=0):
    newtime_ampm=am_pm[start[-2:]];
  if(totalmins>59):
    totalhrs+=1;
    totalmins-=60
  totalmins=str(totalmins);
  if(len(totalmins)<2):
      totalmins ="0"+totalmins;
  hrs_for_day = totalhrs;
  newtime_ampm=get_am_pm(totalhrs,start[-2:]);
  if(totalhrs>12): 
     totalhrs=totalhrs-(totalhrs//12)*12;  
     if(totalhrs==0):
     	  totalhrs=12;
  totalhrs=str(totalhrs);
  new_time=totalhrs+":"+totalmins+" "+newtime_ampm;
  if(startday!="none"):
    index_day=days.index(start_day);
  if(start[-2:]=="PM" and hrs_for_day>=12)or(hrs_for_day>23):
      if(start[-2:]=="PM" and hrs_for_day>=12):
           hrs_for_day = hrs_for_day-12;
           if(index_day+1>6):
               start_day=days[0]
           else:  
               start_day=days[index_day+1];
           index_day+=1;
           count+=1;
      while hrs_for_day>23:
        if(index_day+1>6):
         start_day=days[0]
        else:  
         start_day=days[index_day+1];
        index_day+=1;
        count+=1;
        hrs_for_day-=24;
  if(count==1):
  		count="(next day)";
  elif(count>1):
  	  count="("+str(count)+ " days later)"	
  if(startday!="none")and (count!=0):
     new_time=new_time+", "+start_day+" "+count;
  elif(startday!="none")and (count==0):
     new_time=new_time+", "+start_day;   
  elif (count!=0):
     new_time=new_time+" "+count;    	
  

 
  return new_time

def get_am_pm(totalhrs,dayperiod):
    am_pm={
          "AM":"PM",
          "PM":"AM"
          }
    if(totalhrs<12):
        return dayperiod;
    while totalhrs>=12:
        totalhrs-=11;
        if(totalhrs<12):
          dayperiod=am_pm[dayperiod];
          return dayperiod;
        dayperiod=am_pm[dayperiod]; 
