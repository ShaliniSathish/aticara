import lib_module_opt
import gc
import time
print "create csv and log files for show cable modem command. And also combine all files into a single file."
lib_module_opt.loader_function("show cable modem","casa_cmts_region.txt","eddb","K4b3lkutj3s!")
lib_module_opt.loader_function_for_parsing("casa_cmts_region.txt","casa_cable_modem_basic.textfsm","show cable modem")
lib_module_opt.copy_files_with_same_extension(".csv_CASA_showcablemodem","all_scm.csv")
#lib_module_opt.cm_info_to_database("all_scm.csv", "CM_INFO_TABLE","mysql://root:test123@localhost/","E2E_DB")

gc.collect()
 
print "create csv and log files for show cable modem vendor.And also combine file into single file."
lib_module_opt.loader_function("show cable modem vendor","casa_cmts_region.txt","eddb","K4b3lkutj3s!")
lib_module_opt.loader_function_for_parsing("casa_cmts_region.txt","casa_cable_modem_vendor.textfsm","show cable modem vendor")
lib_module_opt.copy_files_with_same_extension(".csv_CASA_showcablemodemvendor","all_scm_with_oui.csv")
lib_module_opt.loader_function_for_parsing("casa_cmts_region.txt","casa_cmts_without_oui_vendor.textfsm","show cable modem vendor")
lib_module_opt.copy_files_with_same_extension(".csv_CASA_showcablemodemvendor","all_scm_with_vendor.csv")
lib_module_opt.vendor_map_func("all_scm_with_oui.csv","all_scm_with_vendor.csv")

gc.collect()

print "to merge cm information and vendor mappings information into single csv."
lib_module_opt.cm_vendor_map("all_scm.csv","vendor_mapping.csv")

print "To get csv and log files for show cable modem mac.and also merge it with cm_vendor information"
lib_module_opt.loader_function("show cable modem mac","casa_cmts_region.txt","eddb","K4b3lkutj3s!")
lib_module_opt.loader_function_for_parsing("casa_cmts_region.txt","casa_cable_modem_mac.textfsm","show cable modem mac")
lib_module_opt.copy_files_with_same_extension(".csv_CASA_showcablemodemmac","all_scm_mac.csv")

gc.collect()
print "this function merges vendor and docsis informations into a single csv file[cm_vendor_docsis_info.csv]"
lib_module_opt.cm_vendor_docsis_map("cm_vendor_info.csv","all_scm_mac.csv")

gc.collect()
lib_module_opt.cm_vendor_docsis_brio_map("cm_vendor_docsis_info.csv","geocode.csv")

gc.collect()
print "this will add vendor docsis info to db."
#lib_module_opt.vendor_docsis_info_to_db("mysql://root:test123@localhost/","E2E_DB","CM_VENDOR_DOCSIS_INFO","cm_vendor_docsis_info.csv")

gc.collect()

print "this creates a CM_GEO_MAP_TABLE."
#lib_module_opt.create_geo_table("cm_vendor_docsis_brio_info.csv","mysql://root:test123@localhost","E2E_DB","CM_GEO_MAP_TABLE")

gc.collect()
