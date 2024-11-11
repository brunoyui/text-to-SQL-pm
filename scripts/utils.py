def count_ok(df, columns):
  return df[df[columns] == 1].shape[0]

def calculate_percentages_counts(df, columns):
  total = df.shape[0]
  total_ok = [count_ok(df, column) for column in columns]
  percentages = [round(x / total * 100, 2) for x in df[columns].sum().tolist()]
  return percentages