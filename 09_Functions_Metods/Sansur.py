def sansur(cumlelistesi,yasaklikelime, yenikelime):
	for i in range(len(cumlelistesi)):
		cumlelistesi[i] = cumlelistesi[i].replace(yasaklikelime, yenikelime*len(yasaklikelime))
	
	return cumlelistesi