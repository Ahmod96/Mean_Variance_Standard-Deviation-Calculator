import numpy as np

def calculate(list):
  if len(list) != 9:
      raise ValueError ('List must contain nine numbers.')
  else:
      array = np.array(list).reshape(3,3)
      calculations = {}
      mean_val = [np.mean(array, axis = 0).tolist(), np.mean(array, axis = 1).tolist(), np.mean(list)]
      var_val = [np.var(array, axis = 0).tolist(), np.var(array, axis = 1).tolist(), np.var(list)]
      std_val = [np.std(array, axis = 0).tolist(), np.std(array, axis = 1).tolist(), np.std(list)]
      max_val = [np.max(array, axis = 0).tolist(), np.max(array, axis = 1).tolist(), np.max(list)]
      min_val = [np. min(array, axis = 0).tolist(), np. min(array, axis = 1).tolist(), np. min(list)]
      sum_val = [np.sum(array, axis = 0).tolist(), np.sum(array, axis = 1).tolist(), np.sum(list)]
      calculations['mean'] = mean_val
      calculations['variance'] = var_val
      calculations['standard deviation'] = std_val
      calculations['max'] = max_val
      calculations['min'] = min_val
      calculations['sum'] = sum_val
      return calculations

