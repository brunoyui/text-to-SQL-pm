def count_ok(df, columns):
  return df[df[columns] == 1].shape[0]

def count_ok_em(df, columns):
  return df[df[columns] == 'True'].shape[0]

def calculate_percentages_counts(df, columns, metric):
  total = df.shape[0]
  print(df)
  if metric == 'EX':
    total_ok = [count_ok(df, column) for column in columns]
  else:
    total_ok = [count_ok_em(df, column) for column in columns]
  percentages = [round(x / total * 100, 2) for x in total_ok]
  return percentages