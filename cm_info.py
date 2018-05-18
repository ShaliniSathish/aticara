import lib_module_opt
import gc
gc.collect()
lib_module_opt.loader_function("show cable modem","casa_cmts_region.txt","eddb","K4b3lkutj3s!")
lib_module_opt.loader_function_for_parsing("casa_cmts_region.txt","casa_cable_modem_basic.textfsm","show cable modem")
cm_file = lib_module_opt.copy_files_with_same_extension(".csv_CASA_showcablemodem","all_scm.csv")
#lib_module_opt.cm_info_to_database("all_scm.csv", "CM_INFO_TABLE","mysql://root:test123@localhost/","E2E_DB")
gc.collect()
lib_module_opt.copy_file_to_hadoop('hdfs://24.132.64.49:8020',cm_file,'CASA_showcablemodem')
gc.collect()
#lib_module_opt.cm_geo_update("CM_GEO_MAP_TABLE","CM_INFO_TABLE","mysql://root:test123@localhost","E2E_DB")
