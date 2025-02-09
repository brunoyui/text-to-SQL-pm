from execute_analysis_by_model import execute
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sql_complexity", type=str)
    parser.add_argument("--metric", type=str)
    parser.add_argument("--lang", type=str)
    parser.add_argument("--file", type=str)

    args = parser.parse_args()

    if args.metric == "EX":
        metric_label = 'Execution Acc. (%)'
    else:
        metric_label = 'Exact Match Acc. (%)'

    #execute(args.lang, args.metric, args.sql_complexity, args.file, metric_label)
    execute(args.sql_complexity, args.file)