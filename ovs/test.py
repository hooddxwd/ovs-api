from flow import FlowTable
flows = []
br_name = "s1"
table = FlowTable()
flows = table.dump_flow(br_name, flow_cond = None)
for e in flows:
	print e