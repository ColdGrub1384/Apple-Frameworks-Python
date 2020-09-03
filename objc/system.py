'''
Classes from the 'system' framework.
'''
    
try:
    from rubicon.objc import ObjCClass
except ValueError:
    def ObjCClass(name):
        return None
        
def _Class(name):
    try:
        return ObjCClass(name)
    except NameError:
        return None
    
    
OSLogCoder = _Class('OSLogCoder')
OS_xpc_payload = _Class('OS_xpc_payload')
OS_object = _Class('OS_object')
OS_os_eventlink = _Class('OS_os_eventlink')
OS_os_workgroup = _Class('OS_os_workgroup')
OS_os_workgroup_parallel = _Class('OS_os_workgroup_parallel')
OS_os_workgroup_interval = _Class('OS_os_workgroup_interval')
OS_xpc_event_publisher = _Class('OS_xpc_event_publisher')
OS_os_transaction = _Class('OS_os_transaction')
OS_voucher = _Class('OS_voucher')
OS_dispatch_object = _Class('OS_dispatch_object')
OS_dispatch_disk = _Class('OS_dispatch_disk')
OS_dispatch_operation = _Class('OS_dispatch_operation')
OS_dispatch_io = _Class('OS_dispatch_io')
OS_dispatch_mach_msg = _Class('OS_dispatch_mach_msg')
OS_dispatch_queue_attr = _Class('OS_dispatch_queue_attr')
OS_dispatch_group = _Class('OS_dispatch_group')
OS_dispatch_semaphore = _Class('OS_dispatch_semaphore')
OS_dispatch_mach = _Class('OS_dispatch_mach')
OS_dispatch_source = _Class('OS_dispatch_source')
OS_dispatch_channel = _Class('OS_dispatch_channel')
OS_dispatch_queue = _Class('OS_dispatch_queue')
OS_dispatch_queue_pthread_root = _Class('OS_dispatch_queue_pthread_root')
OS_dispatch_queue_global = _Class('OS_dispatch_queue_global')
OS_dispatch_queue_concurrent = _Class('OS_dispatch_queue_concurrent')
OS_dispatch_workloop = _Class('OS_dispatch_workloop')
OS_dispatch_queue_serial = _Class('OS_dispatch_queue_serial')
OS_dispatch_queue_mgr = _Class('OS_dispatch_queue_mgr')
OS_dispatch_queue_main = _Class('OS_dispatch_queue_main')
OS_dispatch_queue_runloop = _Class('OS_dispatch_queue_runloop')
OS_os_activity = _Class('OS_os_activity')
OS_os_log = _Class('OS_os_log')
OS_xpc_object = _Class('OS_xpc_object')
OS_xpc_uint64 = _Class('OS_xpc_uint64')
OS_xpc_int64 = _Class('OS_xpc_int64')
OS_xpc_file_transfer = _Class('OS_xpc_file_transfer')
OS_xpc_activity = _Class('OS_xpc_activity')
OS_xpc_service_instance = _Class('OS_xpc_service_instance')
OS_xpc_bundle = _Class('OS_xpc_bundle')
OS_xpc_mach_recv = _Class('OS_xpc_mach_recv')
OS_xpc_pipe = _Class('OS_xpc_pipe')
OS_xpc_serializer = _Class('OS_xpc_serializer')
OS_xpc_endpoint = _Class('OS_xpc_endpoint')
OS_xpc_error = _Class('OS_xpc_error')
OS_xpc_dictionary = _Class('OS_xpc_dictionary')
OS_xpc_array = _Class('OS_xpc_array')
OS_xpc_mach_send = _Class('OS_xpc_mach_send')
OS_xpc_shmem = _Class('OS_xpc_shmem')
OS_xpc_fd = _Class('OS_xpc_fd')
OS_xpc_uuid = _Class('OS_xpc_uuid')
OS_xpc_string = _Class('OS_xpc_string')
OS_xpc_data = _Class('OS_xpc_data')
OS_xpc_date = _Class('OS_xpc_date')
OS_xpc_pointer = _Class('OS_xpc_pointer')
OS_xpc_double = _Class('OS_xpc_double')
OS_xpc_bool = _Class('OS_xpc_bool')
OS_xpc_null = _Class('OS_xpc_null')
OS_xpc_service = _Class('OS_xpc_service')
OS_xpc_connection = _Class('OS_xpc_connection')
OS_dispatch_data = _Class('OS_dispatch_data')
OS_dispatch_data_empty = _Class('OS_dispatch_data_empty')