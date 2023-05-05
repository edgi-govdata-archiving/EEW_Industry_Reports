import numpy as np
def metrics(echo):
  print("FAC_PERCENT_MINORITY:")
  print("Mean "+str(np.mean(echo['FAC_PERCENT_MINORITY'])))
  print("Median "+str(np.nanmedian(echo['FAC_PERCENT_MINORITY'])))

  print("FAC_TOTAL_PENALTIES")
  print("Mean "+str(np.mean(echo['FAC_TOTAL_PENALTIES'])))
  print("Median "+str(np.nanmedian(echo['FAC_TOTAL_PENALTIES'])))

  print("FAC_PENALTY_COUNT")
  print("Mean "+str(np.mean(echo['FAC_PENALTY_COUNT'])))
  print("Median "+str(np.nanmedian(echo['FAC_PENALTY_COUNT'])))

  print("FAC_QTRS_WITH_NC")
  print("Mean "+str(np.mean(echo['FAC_QTRS_WITH_NC'])))
  print("Median "+str(np.nanmedian(echo['FAC_QTRS_WITH_NC'])))

  print("FAC_INSPECTION_COUNT")
  print("Mean "+str(np.mean(echo['FAC_INSPECTION_COUNT'])))
  print("Median "+str(np.nanmedian(echo['FAC_INSPECTION_COUNT'])))

  print("FAC_DAYS_LAST_INSPECTION")
  print("Mean "+str(np.mean(echo['FAC_DAYS_LAST_INSPECTION'])))
  print("Median "+str(np.nanmedian(echo['FAC_DAYS_LAST_INSPECTION'])))

  print("FAC_INFORMAL_COUNT")
  print("Mean "+str(np.mean(echo['FAC_INFORMAL_COUNT'])))
  print("Median "+str(np.nanmedian(echo['FAC_INFORMAL_COUNT'])))

  print("FAC_FORMAL_ACTION_COUNT")
  print("Mean "+str(np.mean(echo['FAC_FORMAL_ACTION_COUNT'])))
  print("Median "+str(np.nanmedian(echo['FAC_FORMAL_ACTION_COUNT'])))