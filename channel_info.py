import lib_module_opt

lib_module_opt.loader_function("show cable channel utilization","casa_cmts_region.txt","eddb","K4b3lkutj3s!")
lib_module_opt.loader_function_for_parsing("casa_cmts_region.txt","casa_cable_channel_utilization.textfsm","show cable channel utilization")
file = lib_module_opt.copy_files_with_same_extension(".csv_CASA_showcablechannelutilization","all_sccu.csv")
lib_module_opt.copy_file_to_hadoop('hdfs://24.132.64.49:8020',file,'CASA_showcablechannelutilization')



#lib_module_opt.channel_utilization_info_to_db("all_sccu.csv", "CM_CHANNEL_INFO_TABLE","mysql://root:test123@localhost","E2E_DB")
