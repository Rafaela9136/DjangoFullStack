def Second_Chance(pages,n):
	pages = pages.split() # List of pages that is going to be inserted into memory.
	pages_in_memory = n   # Lenght of the physical memory.
	sc_list = [] 		  # List containing the pages in physical memory.
	sc_page_fault = 0     # Amount of page faults.
	# Insertion of pages to memory and calculation of page faults.
	for i in range(len(pages)):
		page = pages[i]	# Page in virtual memory
		# Insert the first pages to physical memory.
		if len(sc_list) < pages_in_memory: 
			page_in_list = Page_Check(sc_list, page, len(sc_list)) 
			if not(page_in_list):
				sc_list.append(page)
				sc_page_fault += 1 # Page Fault.
		# Insert the remaining pages to memory.
		else:
			# Verify if the page to be inserted is not already in list.
			page_in_list = Page_Check(sc_list, page, pages_in_memory)
			# If page is in list remove it and put it in the bag of the list.
			if page_in_list:
				sc_list.remove(page)
				sc_list.append(page)
			# If page is not in list remove the page in the fist position and insert the
			# new one in the back of the list.
			else:
				sc_list.pop(0)
				sc_list.append(page)
				sc_page_fault += 1 # Page Fault
	return sc_page_fault
