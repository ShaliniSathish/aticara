import cql
from cassandra.cluster import Cluster
import os
cluster = Cluster(contact_points = ['24.132.64.45',], port='9042')
session = cluster.connect('e2e_db')

#session.execute("create table if not exists "+"cm_info_table"+" (CMTS text,REGION text,MAC_ADDRESS text,IP_ADDRESS text,US_Intf text,DS_Intf text,State text,Prim_SID text,Rx_Pwr text,Timing_offset text,Num_CPE text,BPI text,timeupdated text,PRIMARY KEY (MAC_ADDRESS));")


#os.system("./cassandra-loader -f /home/E2E_Development/csv_files/scm.csv_2018-05-16_08-16-33 -host 24.132.64.45 -schema 'e2e_db.cm_info_table(cmts,region,mac_address,ip_address,us_intf,ds_intf,state,prim_sid,rx_pwr,timing_offset,num_cpe,bpi,timeupdated)' -delim ';' -numThreads 10 ;")
#session.execute("./cassandra-loader -f /home/E2E_Development/csv_files/scm.csv_2018-05-09_06-03-49_2 -host 24.132.64.45 -schema "e2e_db.cm_info_table(id,cmts,region,mac_address,ip_address,us_intf,ds_intf,state,prim_sid,rx_pwr,timing_offset,num_cpe,bpi,timeupdated)" -delim ";" -numThreads 10 ;")


#session.execute("create table if not exists "+"partial_info_table"+" (CMTS text,REGION text,MAC_ADDRESS text,MAC_ID text,US_Intf text,DS_Intf text,US_SET text,DS_SET text,US_DS_Excluded text,timeupdated text,PRIMARY KEY (MAC_ADDRESS));")

#os.system("./cassandra-loader -f /home/E2E_Development/csv_files/partial.csv_2018-05-17_01-19-19 -host 24.132.64.45 -schema 'e2e_db.partial_info_table(CMTS,REGION,MAC_ADDRESS,MAC_ID,US_Intf,DS_Intf,US_SET,DS_SET,US_DS_Excluded,timeupdated)' -delim ';' -numThreads 10 ;")

#session.execute("create table if not exists "+"qos_info_table"+" (CMTS text,REGION text,MAC_ADDRESS text,Sfid text,Dir text,Curr_State text,Sid text,Sched_Type text,Prio text,MaxSusRate text,MaxBrst text,MinRsvRate text,PeakTrafRate text,Throughput text,ServiceClassName text,timeupdated text,PRIMARY KEY (MAC_ADDRESS));")


os.system("./cassandra-loader -f /home/E2E_Development/csv_files/qos.csv_2018-05-17_01-36-13 -host 24.132.64.45 -schema 'e2e_db.qos_info_table(CMTS,REGION,MAC_ADDRESS,Sfid,Dir,Curr_State,Sid,Sched_Type,Prio,MaxSusRate,MaxBrst,MinRsvRate,PeakTrafRate,Throughput,ServiceClassName,timeupdated)' -delim ';' -numThreads 10 ;")
