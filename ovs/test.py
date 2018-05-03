from flow import FlowTable
flows = []
br_name = "s1"
table = FlowTable()
sum = 0
flows = table.dump_flow(br_name, flow_cond = None)
for e in flows:
	#print e
	if 'tp_src' in e: 
		#print 'port: ' + e['tp_src']
		if e['tp_src'] == '5692':
			sum = sum + int(e['n_packets'])
print sum
